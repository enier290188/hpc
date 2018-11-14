# -*- coding: utf-8 -*-
from src.application.security import models
from django import forms
from django.utils.translation import ugettext_lazy as _
import os
import shutil

___FIELD___IS_ACTIVE___ = forms.BooleanField(
    label=_('APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_SECURITY___LDAPUSERIMPORTED___IS_ACTIVE'),
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
    label=_('APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_SECURITY___LDAPUSERIMPORTED___CREATED'),
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
    label=_('APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_SECURITY___LDAPUSERIMPORTED___MODIFIED'),
    required=False,
    widget=forms.DateInput(
        attrs={
            'id': 'modified',
            'aria-describedby': 'modified_icon',
            'icon': 'glyphicon glyphicon-time',
        },
    ),
)
___FIELD___AVATAR___ = forms.ImageField(
    label=_('APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_SECURITY___LDAPUSERIMPORTED___AVATAR'),
    required=False,
    widget=forms.FileInput(
        attrs={
            'id': 'avatar',
            'icon': 'glyphicon glyphicon-picture',
            'button_upload_id': 'avatar___button_upload_id',
            'img_upload_id': 'avatar___img_upload_id',
            'style': 'display: none;',
        },
    ),
)
___FIELD___FIRST_NAME___ = forms.CharField(
    label=_('APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_SECURITY___LDAPUSERIMPORTED___FIRST_NAME'),
    required=False,
    widget=forms.TextInput(
        attrs={
            'id': 'first_name',
            'class': 'form-control',
            'aria-describedby': 'first_name_icon',
            'icon': 'glyphicon glyphicon-globe',
        },
    ),
)
___FIELD___LAST_NAME___ = forms.CharField(
    label=_('APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_SECURITY___LDAPUSERIMPORTED___LAST_NAME'),
    required=False,
    widget=forms.TextInput(
        attrs={
            'id': 'last_name',
            'class': 'form-control',
            'aria-describedby': 'last_name_icon',
            'icon': 'glyphicon glyphicon-globe',
        },
    ),
)
___FIELD___IDENTIFIER___ = forms.CharField(
    label=_('APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_SECURITY___LDAPUSERIMPORTED___IDENTIFIER'),
    required=False,
    widget=forms.TextInput(
        attrs={
            'id': 'identifier',
            'class': 'form-control',
            'aria-describedby': 'identifier_icon',
            'icon': 'glyphicon glyphicon-user',
        },
    ),
)
___FIELD___EMAIL___ = forms.EmailField(
    label=_('APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_SECURITY___LDAPUSERIMPORTED___EMAIL'),
    required=False,
    widget=forms.EmailInput(
        attrs={
            'id': 'email',
            'class': 'form-control',
            'aria-describedby': 'email_icon',
            'icon': 'glyphicon glyphicon-envelope',
        },
    ),
)
___FIELD___DETAIL___ = forms.CharField(
    label=_('APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_SECURITY___LDAPUSERIMPORTED___DETAIL'),
    required=False,
    widget=forms.Textarea(
        attrs={
            'id': 'detail',
            'class': 'form-control',
            'aria-describedby': 'detail_icon',
            'icon': 'glyphicon glyphicon-globe',
            'rows': 5,
        },
    ),
)
___FIELD___INSTITUTE___ = forms.CharField(
    label=_('APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_SECURITY___LDAPUSERIMPORTED___INSTITUTE'),
    required=True,
    min_length=1,
    max_length=256,
    widget=forms.TextInput(
        attrs={
            'id': 'institute',
            'class': 'form-control',
            'aria-describedby': 'institute_icon',
            'icon': 'glyphicon glyphicon-globe',
        },
    ),
)
___FIELD___RESEARCH_FIELD___ = forms.CharField(
    label=_('APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_SECURITY___LDAPUSERIMPORTED___RESEARCH_FIELD'),
    required=True,
    min_length=1,
    max_length=256,
    widget=forms.TextInput(
        attrs={
            'id': 'researchField',
            'class': 'form-control',
            'aria-describedby': 'researchField_icon',
            'icon': 'glyphicon glyphicon-globe',
        },
    ),
)
___FIELD___RESEARCH_GROUP___ = forms.CharField(
    label=_('APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_SECURITY___LDAPUSERIMPORTED___RESEARCH_GROUP'),
    required=True,
    min_length=1,
    max_length=256,
    widget=forms.TextInput(
        attrs={
            'id': 'researchGroup',
            'class': 'form-control',
            'aria-describedby': 'researchGroup_icon',
            'icon': 'glyphicon glyphicon-globe',
        },
    ),
)
___FIELD___USER_PROFILE___ = forms.ChoiceField(
    label=_('APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_SECURITY___LDAPUSERIMPORTED___USER_PROFILE'),
    required=True,
    choices=[
        ('Teacher', _("APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_SECURITY___LDAPUSERIMPORTED___USER_PROFILE___OPTION___TEACHER")),
        ('Investigator', _("APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_SECURITY___LDAPUSERIMPORTED___USER_PROFILE___OPTION___INVESTIGATOR")),
        ('Undergraduate student', _("APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_SECURITY___LDAPUSERIMPORTED___USER_PROFILE___OPTION___UNDERGRADUATE_STUDENT")),
        ('Master\'s student', _("APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_SECURITY___LDAPUSERIMPORTED___USER_PROFILE___OPTION____MASTER'S_STUDENT")),
        ('PhD student', _("APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_SECURITY___LDAPUSERIMPORTED___USER_PROFILE___OPTION___PHD_STUDENT")),
        ('Other', _("APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_SECURITY___LDAPUSERIMPORTED___USER_PROFILE___OPTION___OTHER")),
    ],
    initial='Teacher',
    widget=forms.Select(
        attrs={
            'id': 'userProfile_register',
            'class': 'form-control',
            'aria-describedby': 'userProfile_icon',
            'icon': 'glyphicon glyphicon-list',
        },
    ),
)
___FIELD___TUTOR_INSTITUTION___ = forms.CharField(
    label=_('APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_SECURITY___LDAPUSERIMPORTED___TUTOR_INSTITUTION'),
    required=False,
    min_length=1,
    max_length=256,
    widget=forms.TextInput(
        attrs={
            'id': 'tutorInstitution',
            'class': 'form-control',
            'aria-describedby': 'tutorInstitution_icon',
            'icon': 'glyphicon glyphicon-globe',
        },
    ),
)
___FIELD___TUTOR_MAIL___ = forms.EmailField(
    label=_('APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_SECURITY___LDAPUSERIMPORTED___TUTOR_MAIL'),
    required=False,
    min_length=1,
    max_length=256,
    widget=forms.EmailInput(
        attrs={
            'id': 'tutorMail',
            'class': 'form-control',
            'aria-describedby': 'tutorMail_icon',
            'icon': 'glyphicon glyphicon-envelope',
        },
    ),
)
___FIELD___TUTOR_NAME___ = forms.CharField(
    label=_('APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_SECURITY___LDAPUSERIMPORTED___TUTOR_NAME'),
    required=False,
    min_length=1,
    max_length=256,
    widget=forms.TextInput(
        attrs={
            'id': 'tutorName',
            'class': 'form-control',
            'aria-describedby': 'tutorName_icon',
            'icon': 'glyphicon glyphicon-globe',
        },
    ),
)


def ___field___attribute___placeholder___locale___reload__(field, locale):
    field.widget.attrs['placeholder'] = '- %s -' % (_(locale),)


def ___field___attribute___help_text___locale___reload__(field, locale):
    field.help_text = '\"%s\"' % (_(locale),)


class LDAPUserImportedDetail(forms.ModelForm):
    is_active = ___FIELD___IS_ACTIVE___
    created = ___FIELD___CREATED___
    modified = ___FIELD___MODIFIED___
    avatar = ___FIELD___AVATAR___
    first_name = ___FIELD___FIRST_NAME___
    last_name = ___FIELD___LAST_NAME___
    identifier = ___FIELD___IDENTIFIER___
    email = ___FIELD___EMAIL___
    detail = ___FIELD___DETAIL___
    institute = ___FIELD___INSTITUTE___
    researchField = ___FIELD___RESEARCH_FIELD___
    researchGroup = ___FIELD___RESEARCH_GROUP___
    userProfile = ___FIELD___USER_PROFILE___
    tutorInstitution = ___FIELD___TUTOR_INSTITUTION___
    tutorMail = ___FIELD___TUTOR_MAIL___
    tutorName = ___FIELD___TUTOR_NAME___

    class Meta:
        model = models.LDAPUserImported
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super().__init__(*args, **kwargs)


class LDAPUserImportedUpdate(forms.ModelForm):
    is_active = ___FIELD___IS_ACTIVE___
    avatar = ___FIELD___AVATAR___
    first_name = ___FIELD___FIRST_NAME___
    last_name = ___FIELD___LAST_NAME___
    identifier = ___FIELD___IDENTIFIER___
    email = ___FIELD___EMAIL___
    detail = ___FIELD___DETAIL___
    institute = ___FIELD___INSTITUTE___
    researchField = ___FIELD___RESEARCH_FIELD___
    researchGroup = ___FIELD___RESEARCH_GROUP___
    userProfile = ___FIELD___USER_PROFILE___

    class Meta:
        model = models.LDAPUserImported
        fields = ['is_active', 'avatar', 'first_name', 'last_name', 'identifier', 'email', 'detail', 'institute', 'researchField', 'researchGroup', 'userProfile', 'tutorInstitution', 'tutorMail', 'tutorName', ]

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        self.instance_current = kwargs.pop('instance_current')
        super().__init__(*args, **kwargs)
        #
        # is_active
        ___field___attribute___help_text___locale___reload__(field=self.fields['is_active'], locale='APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_SECURITY___LDAPUSERIMPORTED___IS_ACTIVE___HELP_TEXT')
        # first_name
        ___field___attribute___placeholder___locale___reload__(field=self.fields['first_name'], locale='APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_SECURITY___LDAPUSERIMPORTED___FIRST_NAME')
        self.fields['first_name'].widget.attrs['readonly'] = 'readonly'
        self.fields['first_name'].widget.attrs['autofocus'] = True
        # last name
        ___field___attribute___placeholder___locale___reload__(field=self.fields['last_name'], locale='APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_SECURITY___LDAPUSERIMPORTED___LAST_NAME')
        self.fields['last_name'].widget.attrs['readonly'] = 'readonly'
        # identifier
        ___field___attribute___placeholder___locale___reload__(field=self.fields['identifier'], locale='APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_SECURITY___LDAPUSERIMPORTED___IDENTIFIER')
        self.fields['identifier'].widget.attrs['readonly'] = 'readonly'
        # email
        ___field___attribute___placeholder___locale___reload__(field=self.fields['email'], locale='APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_SECURITY___LDAPUSERIMPORTED___EMAIL')
        self.fields['email'].widget.attrs['readonly'] = 'readonly'
        # detail
        ___field___attribute___placeholder___locale___reload__(field=self.fields['detail'], locale='APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_SECURITY___LDAPUSERIMPORTED___DETAIL')
        ___field___attribute___help_text___locale___reload__(field=self.fields['detail'], locale='APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_SECURITY___LDAPUSERIMPORTED___DETAIL___HELP_TEXT')
        self.fields['detail'].widget.attrs['readonly'] = 'readonly'
        # institute
        ___field___attribute___placeholder___locale___reload__(field=self.fields['institute'], locale='APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_SECURITY___LDAPUSERIMPORTED___INSTITUTE')
        self.fields['institute'].widget.attrs['readonly'] = 'readonly'
        # researchField
        ___field___attribute___placeholder___locale___reload__(field=self.fields['researchField'], locale='APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_SECURITY___LDAPUSERIMPORTED___RESEARCH_FIELD')
        self.fields['researchField'].widget.attrs['readonly'] = 'readonly'
        # researchGroup
        ___field___attribute___placeholder___locale___reload__(field=self.fields['researchGroup'], locale='APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_SECURITY___LDAPUSERIMPORTED___RESEARCH_GROUP')
        self.fields['researchGroup'].widget.attrs['readonly'] = 'readonly'
        # userProfile
        ___field___attribute___placeholder___locale___reload__(field=self.fields['userProfile'], locale='APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_SECURITY___LDAPUSERIMPORTED___USER_PROFILE')
        self.fields['userProfile'].widget.attrs['readonly'] = 'readonly'
        # tutorInstitution
        ___field___attribute___placeholder___locale___reload__(field=self.fields['tutorInstitution'], locale='APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_SECURITY___LDAPUSERIMPORTED___TUTOR_INSTITUTION')
        # tutorMail
        ___field___attribute___placeholder___locale___reload__(field=self.fields['tutorMail'], locale='APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_SECURITY___LDAPUSERIMPORTED___TUTOR_MAIL')
        # tutorName
        ___field___attribute___placeholder___locale___reload__(field=self.fields['tutorName'], locale='APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_SECURITY___LDAPUSERIMPORTED___TUTOR_NAME')

    def clean_avatar(self):
        avatar = self.cleaned_data.get('avatar')
        if self.files.get('avatar'):
            if len(self.files.get('avatar')) > 1 * 1024 * 1024:  # 1MB
                raise forms.ValidationError(_('APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_SECURITY___LDAPUSERIMPORTED___VALIDATION The avatar should not be beggear than %(weight)s.') % {'weight': '1mb', })
        return avatar

    def clean_first_name(self):
        first_name = self.instance_current.first_name
        return first_name

    def clean_last_name(self):
        last_name = self.instance_current.last_name
        return last_name

    def clean_identifier(self):
        identifier = self.instance_current.identifier
        return identifier

    def clean_email(self):
        email = self.instance_current.email
        return email

    def clean_detail(self):
        detail = self.instance_current.detail
        return detail

    def clean_institute(self):
        institute = self.instance_current.institute
        return institute

    def clean_researchField(self):
        researchField = self.instance_current.researchField
        return researchField

    def clean_researchGroup(self):
        researchGroup = self.instance_current.researchGroup
        return researchGroup

    def clean_userProfile(self):
        userProfile = self.instance_current.userProfile
        return userProfile

    def clean_tutorInstitution(self):
        tutorInstitution = self.instance_current.tutorInstitution
        return tutorInstitution

    def clean_tutorMail(self):
        tutorMail = self.instance_current.tutorMail
        return tutorMail

    def clean_tutorName(self):
        tutorName = self.instance_current.tutorName
        return tutorName

    def save(self, commit=True):
        instance = super(LDAPUserImportedUpdate, self).save(commit=False)
        #
        if commit:
            # avatar
            if self.instance_current.avatar is not None and self.instance_current.avatar != '' and instance.avatar is not None and instance.avatar != '':
                if self.instance_current.avatar != instance.avatar:
                    if os.path.exists(self.instance_current.avatar.path):
                        os.remove(self.instance_current.avatar.path)
                if self.instance_current.identifier != instance.identifier:
                    if self.instance_current.avatar != instance.avatar:
                        if os.path.exists(self.instance_current.___string___folder_path___()):
                            shutil.rmtree(self.instance_current.___string___folder_path___())
                    else:
                        instance.avatar = '%s/%s/%s/%s.jpg' % (models.___LDAPUSERIMPORTED_FOLDER_PATH___, instance.ldap_group, instance.identifier, instance.identifier,)
                        if os.path.exists(self.instance_current.avatar.path) and os.path.exists(self.instance_current.___string___folder_path___()):
                            os.rename(self.instance_current.avatar.path, '%s/%s.jpg' % (self.instance_current.___string___folder_path___(), instance.identifier,))
                            os.rename(self.instance_current.___string___folder_path___(), self.instance.___string___folder_path___())
            # save to data base
            instance.save()
        return instance


class LDAPUserImportedDelete(forms.ModelForm):
    class Meta:
        model = models.LDAPUserImported
        fields = ['id', ]

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super().__init__(*args, **kwargs)

    def ___delete___(self):
        # avatar
        if os.path.exists(self.instance.___string___folder_path___()):
            shutil.rmtree(self.instance.___string___folder_path___())
        self.instance.delete()
