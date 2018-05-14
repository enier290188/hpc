# -*- coding: utf-8 -*-
from django import forms
from django.core.validators import ValidationError
from django.utils.translation import ugettext_lazy as _


class GenericForm(forms.Form):
    generic = forms.CharField(
        required=False,
        max_length=200,
        widget=forms.TextInput(
            attrs={
                'class': 'input-sm form-control'
            }
        ),
    )

    def __init__(self, *args, **kwargs):
        self.option = kwargs.pop('option', None)
        super().__init__(*args, **kwargs)
        if self.option == 'rename':
            self.fields['generic'].widget.attrs['placeholder'] = "- Especifique el nuevo nombre del elemento -"
        elif self.option == 'folder':
            self.fields['generic'].widget.attrs['placeholder'] = "- Especifique el nombre del directorio -"
        elif self.option == 'file':
            self.fields['generic'].widget.attrs['placeholder'] = "- Especifique el nombre del archivo -"


class FileEditForm(forms.Form):
    file_content = forms.CharField(
        required=True,
        widget=forms.Textarea(
            attrs={
                'rows': '6',
                'class': 'form-control'
            }
        ),
    )

    def __init__(self, *args, **kwargs):
        self.content = kwargs.pop('content', None)
        super().__init__(*args, **kwargs)
        if self.content:
            self.fields['file_content'].initial = self.content


class UploadMultipleFilesForm(forms.Form):
    files = forms.FileField(
        widget=forms.ClearableFileInput(
            attrs={
                'id': 'files',
                'multiple': True
            }
        )
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class MultiFileInput(forms.FileInput):
    def render(self, name, value, attrs=None):
        attrs['id'] = 'files'
        attrs['multiple'] = 'multiple'
        # attrs['style'] = 'display:none'
        return super(MultiFileInput, self).render(name, None, attrs=attrs)

    def value_from_datadict(self, data, files, name):
        if hasattr(files, 'getlist'):
            return files.getlist(name)
        else:
            return [files.get(name)]


class MultiFileField(forms.FileField):
    widget = MultiFileInput

    def __init__(self, *args, **kwargs):
        self.min_num = kwargs.pop('min_num', 0)
        self.max_num = kwargs.pop('max_num', None)
        self.maximum_file_size = kwargs.pop('maximum_file_size', None)
        super(MultiFileField, self).__init__(*args, **kwargs)

    def to_python(self, data):
        ret = []
        for item in data:
            ret.append(super(MultiFileField, self).to_python(item))
        return ret

    def validate(self, data):
        super(MultiFileField, self).validate(data)
        num_files = len(data)
        if len(data) and not data[0]:
            num_files = 0
        if num_files < self.min_num:
            raise ValidationError(_('BASE_APPLICATION_CLUSTER_USER_HOME_FORM_ERROR_MIN %(min_num)s %(num_files)s') % {'min_num': self.min_num, 'num_files': num_files})
        elif self.max_num and num_files > self.max_num:
            raise ValidationError(_('BASE_APPLICATION_CLUSTER_USER_HOME_FORM_ERROR_MAX %(max_num)s %(num_files)s') % {'max_num': self.max_num, 'num_files': num_files})
        for uploaded_file in data:
            if uploaded_file.size > self.maximum_file_size:
                raise ValidationError(_('BASE_APPLICATION_CLUSTER_USER_HOME_FORM_ERROR_FILE_SIZE %(uploaded_file_name)s') % {'uploaded_file_name': uploaded_file.name})


class UploadFilesForm(forms.Form):
    files = MultiFileField(max_num=10, min_num=1, maximum_file_size=1024*1024*40)
