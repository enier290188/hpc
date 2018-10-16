# -*- coding: utf-8 -*-
from src.application.security import ldap, models, tasks, utils
from django import forms
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

___FIELD___CREATED___ = forms.DateField(
    label=_('APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_SECURITY___LDAPUSERREQUEST___CREATED'),
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
    label=_('APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_SECURITY___LDAPUSERREQUEST___MODIFIED'),
    required=False,
    widget=forms.DateInput(
        attrs={
            'id': 'modified',
            'aria-describedby': 'modified_icon',
            'icon': 'glyphicon glyphicon-time',
        },
    ),
)
___FIELD___FIRST_NAME___ = forms.CharField(
    label=_('APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_SECURITY___LDAPUSERREQUEST___FIRST_NAME'),
    required=False,
    min_length=1,
    max_length=100,
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
    label=_('APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_SECURITY___LDAPUSERREQUEST___LAST_NAME'),
    required=False,
    min_length=1,
    max_length=100,
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
    label=_('APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_SECURITY___LDAPUSERREQUEST___IDENTIFIER'),
    required=True,
    min_length=1,
    max_length=100,
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
    label=_('APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_SECURITY___LDAPUSERREQUEST___EMAIL'),
    required=True,
    min_length=1,
    max_length=150,
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
    label=_('APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_SECURITY___LDAPUSERREQUEST___DETAIL'),
    required=True,
    min_length=1,
    max_length=1024,
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
    label=_('APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_SECURITY___LDAPUSERREQUEST___INSTITUTE'),
    required=True,
    min_length=1,
    max_length=300,
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
    label=_('APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_SECURITY___LDAPUSERREQUEST___RESEARCH_FIELD'),
    required=True,
    min_length=1,
    max_length=300,
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
    label=_('APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_SECURITY___LDAPUSERREQUEST___RESEARCH_GROUP'),
    required=True,
    min_length=1,
    max_length=300,
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
    label=_('APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_SECURITY___LDAPUSERREQUEST___USER_PROFILE'),
    required=True,
    choices=[
        ('Teacher', _("APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_SECURITY___LDAPUSERREQUEST___USER_PROFILE___OPTION___TEACHER")),
        ('Investigator', _("APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_SECURITY___LDAPUSERREQUEST___USER_PROFILE___OPTION___INVESTIGATOR")),
        ('Undergraduate student', _("APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_SECURITY___LDAPUSERREQUEST___USER_PROFILE___OPTION___UNDERGRADUATE_STUDENT")),
        ('Master\'s student', _("APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_SECURITY___LDAPUSERREQUEST___USER_PROFILE___OPTION____MASTER'S_STUDENT")),
        ('PhD student', _("APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_SECURITY___LDAPUSERREQUEST___USER_PROFILE___OPTION___PHD_STUDENT")),
        ('Other', _("APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_SECURITY___LDAPUSERREQUEST___USER_PROFILE___OPTION___OTHER")),
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


def ___field___attribute___placeholder___locale___reload__(field, locale):
    field.widget.attrs['placeholder'] = '- %s -' % (_(locale),)


def ___field___attribute___help_text___locale___reload__(field, locale):
    field.help_text = '\"%s\"' % (_(locale),)


class LDAPUserRequestDetail(forms.ModelForm):
    created = ___FIELD___CREATED___
    modified = ___FIELD___MODIFIED___
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
        model = models.LDAPUserRequest
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super().__init__(*args, **kwargs)


class LDAPUserRequestApprove(forms.ModelForm):
    class Meta:
        model = models.LDAPUserRequest
        fields = ['id', ]

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super().__init__(*args, **kwargs)

    def ___approve___(self):
        instance_mirror = models.LDAPUser.objects.create(
            first_name=self.instance.first_name,
            last_name=self.instance.last_name,
            identifier=self.instance.identifier,
            email=self.instance.email,
            password=self.instance.password,
            detail=self.instance.detail,
            institute=self.instance.institute,
            researchField=self.instance.researchField,
            researchGroup=self.instance.researchGroup,
            userProfile=self.instance.userProfile
        )
        # Send email
        tasks.___task___application___security___login___request___approve___send_mail___.apply_async(
            args=[],
            kwargs={
                'string___user_model': utils.___APPLICATION___SECURITY___USER___MODEL___LDAPUSER___TEXT___,
                'string___first_name': instance_mirror.first_name,
                'string___last_name': instance_mirror.last_name,
                'string___identifier': '%s_%s' % (settings.LDAP_SERVER_GROUPS_GROUP_CN.lower(), instance_mirror.identifier,),
                'string___email': instance_mirror.email,
                'string___detail': instance_mirror.detail,
                'string___institute': instance_mirror.institute,
                'string___research_field': instance_mirror.researchField,
                'string___research_group': instance_mirror.researchGroup,
                'string___user_profile': instance_mirror.userProfile,
            },
            serializer='json'
        )
        # LDAP
        ldap.___void___action___ldapuser_instance_create___(instance=instance_mirror)
        return instance_mirror


class LDAPUserRequestDisapprove(forms.ModelForm):
    class Meta:
        model = models.LDAPUserRequest
        fields = ['id', ]

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super().__init__(*args, **kwargs)

    def ___disapprove___(self):
        tasks.___task___application___security___login___request___disapprove___send_mail___.apply_async(
            args=[],
            kwargs={
                'string___user_model': utils.___APPLICATION___SECURITY___USER___MODEL___LDAPUSER___TEXT___,
                'string___first_name': self.instance.first_name,
                'string___last_name': self.instance.last_name,
                'string___identifier': '%s_%s' % (settings.LDAP_SERVER_GROUPS_GROUP_CN.lower(), self.instance.identifier,),
                'string___email': self.instance.email,
                'string___detail': self.instance.detail,
                'string___institute': self.instance.institute,
                'string___research_field': self.instance.researchField,
                'string___research_group': self.instance.researchGroup,
                'string___user_profile': self.instance.userProfile,
            },
            serializer='json'
        )
