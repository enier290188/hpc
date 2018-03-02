from src.application.security import models
from django import forms
from django.core import validators
from django.utils.translation import ugettext_lazy as _

___FIELD___IS_ACTIVE___ = forms.BooleanField(
    label=_('APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_SECURITY___PERMISSION___IS_ACTIVE'),
    required=False,
    widget=forms.CheckboxInput(
        attrs={
            'id': 'is_active',
            'aria-describedby': 'is_active_icon',
            'icon': 'glyphicon glyphicon-check',
        },
    ),
)
___FIELD___CREATED___ = forms.DateField(
    label=_('APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_SECURITY___PERMISSION___CREATED'),
    required=False,
    widget=forms.DateInput(
        attrs={
            'id': 'created',
            'aria-describedby': 'created_icon',
            'icon': 'glyphicon glyphicon-time',
        },
    ),
)
___FIELD___MODIFIED___ = forms.DateField(
    label=_('APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_SECURITY___PERMISSION___MODIFIED'),
    required=False,
    widget=forms.DateInput(
        attrs={
            'id': 'modified',
            'aria-describedby': 'modified_icon',
            'icon': 'glyphicon glyphicon-time',
        },
    ),
)
___FIELD___NAME___ = forms.CharField(
    label=_('APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_SECURITY___PERMISSION___NAME'),
    required=True,
    min_length=1,
    max_length=100,
    validators=[
        validators.RegexValidator('^[\w .\-_]+$', message=_('APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_SECURITY___PERMISSION___VALIDATION Only letters, numbers and special characters dot, -, _ and space.')),
    ],
    widget=forms.TextInput(
        attrs={
            'id': 'name',
            'class': 'form-control',
            'aria-describedby': 'name_icon',
            'icon': 'glyphicon glyphicon-globe',
        },
    ),
)
___FIELD___IDENTIFIER___ = forms.CharField(
    label=_('APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_SECURITY___PERMISSION___IDENTIFIER'),
    required=True,
    min_length=1,
    max_length=100,
    validators=[
        validators.RegexValidator('^[\w.]+$', message=_('APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_SECURITY___PERMISSION___VALIDATION Only letters, numbers and the special character dot.')),
    ],
    widget=forms.TextInput(
        attrs={
            'id': 'identifier',
            'class': 'form-control',
            'aria-describedby': 'identifier_icon',
            'icon': 'glyphicon glyphicon-user',
        },
    ),
)


def ___field___attribute___placeholder___locale___reload__(field, locale):
    field.widget.attrs['placeholder'] = '- %s -' % (_(locale),)


def ___field___attribute___help_text___locale___reload__(field, locale):
    field.help_text = '\"%s\"' % (_(locale),)


class PermissionDetail(forms.ModelForm):
    is_active = ___FIELD___IS_ACTIVE___
    created = ___FIELD___CREATED___
    modified = ___FIELD___MODIFIED___
    name = ___FIELD___NAME___
    identifier = ___FIELD___IDENTIFIER___

    class Meta:
        model = models.Permission
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super().__init__(*args, **kwargs)


class PermissionUpdate(forms.ModelForm):
    is_active = ___FIELD___IS_ACTIVE___
    name = ___FIELD___NAME___
    identifier = ___FIELD___IDENTIFIER___

    class Meta:
        model = models.Permission
        fields = ['is_active', 'name', 'identifier', ]

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        self.instance_current = kwargs.pop('instance_current')
        super().__init__(*args, **kwargs)
        #
        # is_active
        ___field___attribute___help_text___locale___reload__(field=self.fields['is_active'], locale='APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_SECURITY___PERMISSION___IS_ACTIVE___HELP_TEXT')
        # name
        ___field___attribute___placeholder___locale___reload__(field=self.fields['name'], locale='APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_SECURITY___PERMISSION___NAME')
        self.fields['name'].widget.attrs['autofocus'] = True
        # identifier
        ___field___attribute___placeholder___locale___reload__(field=self.fields['identifier'], locale='APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_SECURITY___PERMISSION___IDENTIFIER')
        self.fields['identifier'].widget.attrs['readonly'] = 'readonly'

    def clean_name(self):
        name = self.cleaned_data.get('name')
        name = ' '.join(name.split())
        try:
            instance = models.Permission.objects.get(name=name)
        except models.Permission.DoesNotExist:
            return name
        if instance.name == self.instance_current.name:
            return name
        raise forms.ValidationError(_('APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_SECURITY___PERMISSION___VALIDATION This name has already been chosen.'))

    def clean_identifier(self):
        identifier = self.instance_current.identifier
        return identifier

    def save(self, commit=True):
        instance = super(PermissionUpdate, self).save(commit=False)
        #
        if commit:
            # save to data base
            instance.save()
        return instance
