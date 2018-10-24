# -*- coding: utf-8 -*-
from . import ldap, models
from captcha.fields import CaptchaField
from django import forms
from django.conf import settings
from django.core import validators
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
import os
import random
import shutil
import string

___FIELD___LOGIN___IDENTIFIER___ = forms.CharField(
    label=_('APPLICATION___SECURITY___LOGIN___IDENTIFIER'),
    required=True,
    min_length=1,
    max_length=100,
    widget=forms.TextInput(
        attrs={
            'id': 'identifier',
            'class': 'form-control',
            'aria-describedby': 'identifier_icon',
            'icon': 'glyphicon glyphicon-user',
            'autofocus': True,
        },
    ),
)
___FIELD___LOGIN___PASSWORD___ = forms.CharField(
    label=_('APPLICATION___SECURITY___LOGIN___PASSWORD'),
    required=False,
    max_length=32,
    widget=forms.PasswordInput(
        attrs={
            'id': 'password',
            'class': 'form-control',
            'aria-describedby': 'password_icon',
            'icon': 'glyphicon glyphicon-lock',
        },
        render_value=False,
    ),
)
___FIELD___LOGIN___FORGOT_CREDENTIALS___EMAIL___ = forms.EmailField(
    label=_('APPLICATION___SECURITY___LOGIN___FORGOT_CREDENTIALS___EMAIL'),
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
___FIELD___LOGIN___FORGOT_CREDENTIALS___CODE_CONFIRMATION___ = forms.CharField(
    label=_('APPLICATION___SECURITY___LOGIN___FORGOT_CREDENTIALS___CODE_CONFIRMATION'),
    required=True,
    min_length=1,
    max_length=100,
    widget=forms.TextInput(
        attrs={
            'id': 'code_confirmation',
            'class': 'form-control',
            'aria-describedby': 'code_confirmation_icon',
            'icon': 'glyphicon glyphicon-globe',
        },
    ),
)
___FIELD___LOGIN___FORGOT_CREDENTIALS___PASSWORD___ = forms.CharField(
    label=_('APPLICATION___SECURITY___LOGIN___FORGOT_CREDENTIALS___PASSWORD'),
    required=False,
    max_length=32,
    widget=forms.PasswordInput(
        attrs={
            'id': 'password',
            'class': 'form-control',
            'aria-describedby': 'password_icon',
            'icon': 'glyphicon glyphicon-lock',
        },
        render_value=False,
    ),
)
___FIELD___LOGIN___FORGOT_CREDENTIALS___PASSWORD_CONFIRMATION___ = forms.CharField(
    label=_('APPLICATION___SECURITY___LOGIN___FORGOT_CREDENTIALS___PASSWORD_CONFIRMATION'),
    required=False,
    max_length=32,
    widget=forms.PasswordInput(
        attrs={
            'id': 'password_confirmation',
            'class': 'form-control',
            'aria-describedby': 'password_confirmation_icon',
            'icon': 'glyphicon glyphicon-lock',
        },
        render_value=False,
    ),
)
___FIELD___LOGIN___REQUEST___FIRST_NAME___ = forms.CharField(
    label=_('APPLICATION___SECURITY___LOGIN___REQUEST___FIRST_NAME'),
    required=True,
    min_length=1,
    max_length=100,
    validators=[
        validators.RegexValidator('^[\w .\-_]+$', message=_('APPLICATION___SECURITY___LOGIN___REQUEST___VALIDATION Only letters, numbers and special characters dot, -, _ and space.')),
    ],
    widget=forms.TextInput(
        attrs={
            'id': 'first_name',
            'class': 'form-control',
            'aria-describedby': 'first_name_icon',
            'icon': 'glyphicon glyphicon-globe',
        },
    ),
)
___FIELD___LOGIN___REQUEST___LAST_NAME___ = forms.CharField(
    label=_('APPLICATION___SECURITY___LOGIN___REQUEST___LAST_NAME'),
    required=True,
    min_length=1,
    max_length=100,
    validators=[
        validators.RegexValidator('^[\w .\-_]+$', message=_('APPLICATION___SECURITY___LOGIN___REQUEST___VALIDATION Only letters, numbers and special characters dot, -, _ and space.')),
    ],
    widget=forms.TextInput(
        attrs={
            'id': 'last_name',
            'class': 'form-control',
            'aria-describedby': 'last_name_icon',
            'icon': 'glyphicon glyphicon-globe',
        },
    ),
)
___FIELD___LOGIN___REQUEST___IDENTIFIER___ = forms.CharField(
    label=_('APPLICATION___SECURITY___LOGIN___REQUEST___IDENTIFIER'),
    required=True,
    min_length=1,
    max_length=100,
    validators=[
        validators.RegexValidator('^[\w_]+$', message=_('APPLICATION___SECURITY___LOGIN___REQUEST___VALIDATION Only letters, numbers and the special character _.')),
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
___FIELD___LOGIN___REQUEST___EMAIL___ = forms.EmailField(
    label=_('APPLICATION___SECURITY___LOGIN___REQUEST___EMAIL'),
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
___FIELD___LOGIN___REQUEST___PASSWORD___ = forms.CharField(
    label=_('APPLICATION___SECURITY___LOGIN___REQUEST___PASSWORD'),
    required=False,
    max_length=32,
    widget=forms.PasswordInput(
        attrs={
            'id': 'password',
            'class': 'form-control',
            'aria-describedby': 'password_icon',
            'icon': 'glyphicon glyphicon-lock',
        },
        render_value=False,
    ),
)
___FIELD___LOGIN___REQUEST___PASSWORD_CONFIRMATION___ = forms.CharField(
    label=_('APPLICATION___SECURITY___LOGIN___REQUEST___PASSWORD_CONFIRMATION'),
    required=False,
    max_length=32,
    widget=forms.PasswordInput(
        attrs={
            'id': 'password_confirmation',
            'class': 'form-control',
            'aria-describedby': 'password_confirmation_icon',
            'icon': 'glyphicon glyphicon-lock',
        },
        render_value=False,
    ),
)
___FIELD___LOGIN___REQUEST___DETAIL___ = forms.CharField(
    label=_('APPLICATION___SECURITY___LOGIN___REQUEST___DETAIL'),
    required=True,
    min_length=1,
    max_length=1024,
    widget=forms.Textarea(
        attrs={
            'id': 'detail',
            'class': 'form-control',
            'rows': 5,
        },
    ),
)
___FIELD___LOGIN___REQUEST___INSTITUTE___ = forms.CharField(
    label=_('APPLICATION___SECURITY___LOGIN___REQUEST___INSTITUTE'),
    required=True,
    min_length=1,
    max_length=300,
    validators=[
        validators.RegexValidator('^[\w .\-_]+$', message=_('APPLICATION___SECURITY___LOGIN___REQUEST___VALIDATION Only letters, numbers and special characters dot, -, _ and space.')),
    ],
    widget=forms.TextInput(
        attrs={
            'id': 'institute',
            'class': 'form-control',
            'aria-describedby': 'institute_icon',
            'icon': 'glyphicon glyphicon-globe',
        },
    ),
)
___FIELD___LOGIN___REQUEST___RESEARCH_FIELD___ = forms.CharField(
    label=_('APPLICATION___SECURITY___LOGIN___REQUEST___RESEARCH_FIELD'),
    required=True,
    min_length=1,
    max_length=300,
    validators=[
        validators.RegexValidator('^[\w .\-_]+$', message=_('APPLICATION___SECURITY___LOGIN___REQUEST___VALIDATION Only letters, numbers and special characters dot, -, _ and space.')),
    ],
    widget=forms.TextInput(
        attrs={
            'id': 'researchField',
            'class': 'form-control',
            'aria-describedby': 'researchField_icon',
            'icon': 'glyphicon glyphicon-globe',
        },
    ),
)
___FIELD___LOGIN___REQUEST___RESEARCH_GROUP___ = forms.CharField(
    label=_('APPLICATION___SECURITY___LOGIN___REQUEST___RESEARCH_GROUP'),
    required=True,
    min_length=1,
    max_length=300,
    validators=[
        validators.RegexValidator('^[\w .\-_]+$', message=_('APPLICATION___SECURITY___LOGIN___REQUEST___VALIDATION Only letters, numbers and special characters dot, -, _ and space.')),
    ],
    widget=forms.TextInput(
        attrs={
            'id': 'researchGroup',
            'class': 'form-control',
            'aria-describedby': 'researchGroup_icon',
            'icon': 'glyphicon glyphicon-globe',
        },
    ),
)
___FIELD___LOGIN___REQUEST___USER_PROFILE___ = forms.ChoiceField(
    label=_('APPLICATION___SECURITY___LOGIN___REQUEST___USER_PROFILE'),
    required=True,
    choices=[
        ('Teacher', _("APPLICATION___SECURITY___LOGIN___REQUEST___USER_PROFILE___OPTION___TEACHER")),
        ('Investigator', _("APPLICATION___SECURITY___LOGIN___REQUEST___USER_PROFILE___OPTION___INVESTIGATOR")),
        ('Undergraduate student', _("APPLICATION___SECURITY___LOGIN___REQUEST___USER_PROFILE___OPTION___UNDERGRADUATE_STUDENT")),
        ('Master\'s student', _("APPLICATION___SECURITY___LOGIN___REQUEST___USER_PROFILE___OPTION____MASTER'S_STUDENT")),
        ('PhD student', _("APPLICATION___SECURITY___LOGIN___REQUEST___USER_PROFILE___OPTION___PHD_STUDENT")),
        ('Other', _("APPLICATION___SECURITY___LOGIN___REQUEST___USER_PROFILE___OPTION___OTHER")),
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
___FIELD___PROFILE___AVATAR___ = forms.ImageField(
    label=_('APPLICATION___SECURITY___PROFILE___AVATAR'),
    required=False,
    widget=forms.FileInput(
        attrs={
            'id': 'avatar',
            'button_upload_id': 'avatar___button_upload_id',
            'img_upload_id': 'avatar___img_upload_id',
            'style': 'display: none;',
        },
    ),
)
___FIELD___PROFILE___FIRST_NAME___ = forms.CharField(
    label=_('APPLICATION___SECURITY___PROFILE___FIRST_NAME'),
    required=False,
    min_length=1,
    max_length=100,
    validators=[
        validators.RegexValidator('^[\w .\-_]+$', message=_('APPLICATION___SECURITY___PROFILE___VALIDATION Only letters, numbers and special characters dot, -, _ and space.')),
    ],
    widget=forms.TextInput(
        attrs={
            'id': 'first_name',
            'class': 'form-control',
            'aria-describedby': 'first_name_icon',
            'icon': 'glyphicon glyphicon-globe',
        },
    ),
)
___FIELD___PROFILE___LAST_NAME___ = forms.CharField(
    label=_('APPLICATION___SECURITY___PROFILE___LAST_NAME'),
    required=False,
    min_length=1,
    max_length=100,
    validators=[
        validators.RegexValidator('^[\w .\-_]+$', message=_('APPLICATION___SECURITY___PROFILE___VALIDATION Only letters, numbers and special characters dot, -, _ and space.')),
    ],
    widget=forms.TextInput(
        attrs={
            'id': 'last_name',
            'class': 'form-control',
            'aria-describedby': 'last_name_icon',
            'icon': 'glyphicon glyphicon-globe',
        },
    ),
)
___FIELD___PROFILE___IDENTIFIER___ = forms.CharField(
    label=_('APPLICATION___SECURITY___PROFILE___IDENTIFIER'),
    required=True,
    min_length=1,
    max_length=100,
    validators=[
        validators.RegexValidator('^[\w_]+$', message=_('APPLICATION___SECURITY___PROFILE___VALIDATION Only letters, numbers and the special character _.')),
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
___FIELD___PROFILE___EMAIL___ = forms.EmailField(
    label=_('APPLICATION___SECURITY___PROFILE___EMAIL'),
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
___FIELD___PROFILE___PASSWORD___ = forms.CharField(
    label=_('APPLICATION___SECURITY___PROFILE___PASSWORD'),
    required=False,
    max_length=32,
    widget=forms.PasswordInput(
        attrs={
            'id': 'password',
            'class': 'form-control',
            'aria-describedby': 'password_icon',
            'icon': 'glyphicon glyphicon-lock',
        },
        render_value=False,
    ),
)
___FIELD___PROFILE___PASSWORD_CONFIRMATION___ = forms.CharField(
    label=_('APPLICATION___SECURITY___PROFILE___PASSWORD_CONFIRMATION'),
    required=False,
    max_length=32,
    widget=forms.PasswordInput(
        attrs={
            'id': 'password_confirmation',
            'class': 'form-control',
            'aria-describedby': 'password_confirmation_icon',
            'icon': 'glyphicon glyphicon-lock',
        },
        render_value=False,
    ),
)


def ___field___attribute___placeholder___locale___reload__(field, locale):
    field.widget.attrs['placeholder'] = '- %s -' % (_(locale),)


def ___field___attribute___help_text___locale___reload__(field, locale):
    field.help_text = '\"%s\"' % (_(locale),)


class LOCALUserLogin(forms.Form):
    local_identifier = ___FIELD___LOGIN___IDENTIFIER___
    local_password = ___FIELD___LOGIN___PASSWORD___

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super().__init__(*args, **kwargs)
        #
        # identifier
        ___field___attribute___placeholder___locale___reload__(field=self.fields['local_identifier'], locale='APPLICATION___SECURITY___LOGIN___IDENTIFIER')
        self.fields['local_identifier'].widget.attrs['id'] = 'local_identifier'
        self.fields['local_identifier'].widget.attrs['aria-describedby'] = 'local_identifier_icon'
        # password
        ___field___attribute___placeholder___locale___reload__(field=self.fields['local_password'], locale='APPLICATION___SECURITY___LOGIN___PASSWORD')
        self.fields['local_password'].widget.attrs['id'] = 'local_password'
        self.fields['local_password'].widget.attrs['aria-describedby'] = 'local_password_icon'


class LOCALUserLoginForgotCredentials1(forms.ModelForm):
    email = ___FIELD___LOGIN___FORGOT_CREDENTIALS___EMAIL___

    class Meta:
        model = models.LOCALUserForgotCredentials
        fields = ['email', ]

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super().__init__(*args, **kwargs)
        #
        # email
        ___field___attribute___placeholder___locale___reload__(field=self.fields['email'], locale='APPLICATION___SECURITY___LOGIN___FORGOT_CREDENTIALS___EMAIL')
        ___field___attribute___help_text___locale___reload__(field=self.fields['email'], locale='APPLICATION___SECURITY___LOGIN___FORGOT_CREDENTIALS___EMAIL___HELP_TEXT')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            models.LOCALUser.objects.get(email=email)
        except models.LOCALUser.DoesNotExist:
            raise forms.ValidationError(_('APPLICATION___SECURITY___LOGIN___FORGOT_CREDENTIALS___VALIDATION This email address is not subscribed to any account.'))
        try:
            instance = models.LOCALUserForgotCredentials.objects.get(email=email)
        except models.LOCALUserForgotCredentials.DoesNotExist:
            return email
        minutes = instance.___int___time_of_existence___()
        minutes_max = instance.___INT___MAXIMUM_TIME_OF_EXISTENCE___
        if minutes_max <= minutes + 1:
            raise forms.ValidationError(_('APPLICATION___SECURITY___LOGIN___FORGOT_CREDENTIALS___VALIDATION In a few seconds you can try to recover your account.'))
        else:
            raise forms.ValidationError(_('APPLICATION___SECURITY___LOGIN___FORGOT_CREDENTIALS___VALIDATION It is been %(minutes)s minutes since you tried to recover your account, you should wait about %(minutes_max)s minutes.') % {'minutes': minutes, 'minutes_max': minutes_max, })

    def save(self, commit=True):
        instance = super(LOCALUserLoginForgotCredentials1, self).save(commit=False)
        #
        if commit:
            # code
            string___timezone = timezone.now().strftime('%Y%m%d%H%M%S')
            string___letters_digits = string.ascii_letters + string.digits
            string___code = string___timezone + ''.join([random.choice(string___letters_digits) for x in range(86)])  # 100 characteres = 14 + 86
            instance.code = string___code
            # save to data base
            instance.save()
        return instance


class LOCALUserLoginForgotCredentials2(forms.ModelForm):
    email = ___FIELD___LOGIN___FORGOT_CREDENTIALS___EMAIL___
    code_confirmation = ___FIELD___LOGIN___FORGOT_CREDENTIALS___CODE_CONFIRMATION___

    class Meta:
        model = models.LOCALUserForgotCredentials
        fields = ['email', ]

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super().__init__(*args, **kwargs)
        #
        # email
        ___field___attribute___placeholder___locale___reload__(field=self.fields['email'], locale='APPLICATION___SECURITY___LOGIN___FORGOT_CREDENTIALS___EMAIL')
        self.fields['email'].widget.attrs['readonly'] = True
        # code_confirmation
        ___field___attribute___placeholder___locale___reload__(field=self.fields['code_confirmation'], locale='APPLICATION___SECURITY___LOGIN___FORGOT_CREDENTIALS___CODE_CONFIRMATION')
        ___field___attribute___help_text___locale___reload__(field=self.fields['code_confirmation'], locale='APPLICATION___SECURITY___LOGIN___FORGOT_CREDENTIALS___CODE_CONFIRMATION___HELP_TEXT')

    def clean_email(self):
        return self.instance.email

    def clean_code_confirmation(self):
        code_confirmation = self.cleaned_data.get('code_confirmation')
        try:
            models.LOCALUserForgotCredentials.objects.get(email=self.instance.email, code=code_confirmation)
        except models.LOCALUserForgotCredentials.DoesNotExist:
            raise forms.ValidationError(_('APPLICATION___SECURITY___LOGIN___FORGOT_CREDENTIALS___VALIDATION This code is not correct.'))
        return code_confirmation

    def save(self, commit=True):
        instance = super(LOCALUserLoginForgotCredentials2, self).save(commit=False)
        #
        if commit:
            # save to data base
            instance.save()
        return instance


class LOCALUserLoginForgotCredentials3(forms.ModelForm):
    password = ___FIELD___LOGIN___FORGOT_CREDENTIALS___PASSWORD___
    password_confirmation = ___FIELD___LOGIN___FORGOT_CREDENTIALS___PASSWORD_CONFIRMATION___

    class Meta:
        model = models.LOCALUserForgotCredentials
        fields = ['password', ]

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        self.instance_mirror = kwargs.pop('instance_mirror')
        super().__init__(*args, **kwargs)
        #
        # password
        ___field___attribute___placeholder___locale___reload__(field=self.fields['password'], locale='APPLICATION___SECURITY___LOGIN___FORGOT_CREDENTIALS___PASSWORD')
        # password_confirmation
        ___field___attribute___placeholder___locale___reload__(field=self.fields['password_confirmation'], locale='APPLICATION___SECURITY___LOGIN___FORGOT_CREDENTIALS___PASSWORD_CONFIRMATION')

    def clean(self):
        ___clean___ = super(LOCALUserLoginForgotCredentials3, self).clean()
        # password and password_confirmation
        password = self.cleaned_data.get('password')
        password_confirmation = self.cleaned_data.get('password_confirmation')
        if password != password_confirmation:
            self.add_error('password', _('APPLICATION___SECURITY___LOGIN___FORGOT_CREDENTIALS___VALIDATION The password and your confirmation do not match.'))
            self.add_error('password_confirmation', _('APPLICATION___SECURITY___LOGIN___FORGOT_CREDENTIALS___VALIDATION The password and your confirmation do not match.'))
        return ___clean___

    def save(self, commit=True):
        instance = super(LOCALUserLoginForgotCredentials3, self).save(commit=False)
        #
        if commit:
            # password
            password = self.cleaned_data.get('password')
            instance.___void___encrypt_password___(password=password)
            self.instance_mirror.___void___encrypt_password___(password=password)
            # save to data base
            instance.save()
            self.instance_mirror.save()
        return instance


class LOCALUserLoginRequest(forms.ModelForm):
    first_name = ___FIELD___LOGIN___REQUEST___FIRST_NAME___
    last_name = ___FIELD___LOGIN___REQUEST___LAST_NAME___
    identifier = ___FIELD___LOGIN___REQUEST___IDENTIFIER___
    email = ___FIELD___LOGIN___REQUEST___EMAIL___
    password = ___FIELD___LOGIN___REQUEST___PASSWORD___
    password_confirmation = ___FIELD___LOGIN___REQUEST___PASSWORD_CONFIRMATION___
    detail = ___FIELD___LOGIN___REQUEST___DETAIL___

    class Meta:
        model = models.LOCALUserRequest
        fields = ['first_name', 'last_name', 'identifier', 'email', 'password', 'detail', ]

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super().__init__(*args, **kwargs)
        #
        # first_name
        ___field___attribute___placeholder___locale___reload__(field=self.fields['first_name'], locale='APPLICATION___SECURITY___LOGIN___REQUEST___FIRST_NAME')
        self.fields['first_name'].widget.attrs['autofocus'] = True
        # last name
        ___field___attribute___placeholder___locale___reload__(field=self.fields['last_name'], locale='APPLICATION___SECURITY___LOGIN___REQUEST___LAST_NAME')
        # identifier
        ___field___attribute___placeholder___locale___reload__(field=self.fields['identifier'], locale='APPLICATION___SECURITY___LOGIN___REQUEST___IDENTIFIER')
        # email
        ___field___attribute___placeholder___locale___reload__(field=self.fields['email'], locale='APPLICATION___SECURITY___LOGIN___REQUEST___EMAIL')
        # password
        ___field___attribute___placeholder___locale___reload__(field=self.fields['password'], locale='APPLICATION___SECURITY___LOGIN___REQUEST___PASSWORD')
        # password_confirmation
        ___field___attribute___placeholder___locale___reload__(field=self.fields['password_confirmation'], locale='APPLICATION___SECURITY___LOGIN___REQUEST___PASSWORD_CONFIRMATION')
        # detail
        ___field___attribute___placeholder___locale___reload__(field=self.fields['detail'], locale='APPLICATION___SECURITY___LOGIN___REQUEST___DETAIL')
        ___field___attribute___help_text___locale___reload__(field=self.fields['detail'], locale='APPLICATION___SECURITY___LOGIN___REQUEST___DETAIL___HELP_TEXT')

    def clean_identifier(self):
        identifier = self.cleaned_data.get('identifier')
        try:
            models.LOCALUser.objects.get(identifier=identifier)
        except models.LOCALUser.DoesNotExist:
            try:
                models.LOCALUserRequest.objects.get(identifier=identifier)
            except models.LOCALUserRequest.DoesNotExist:
                return identifier
        raise forms.ValidationError(_('APPLICATION___SECURITY___LOGIN___REQUEST___VALIDATION This identifier has already been chosen.'))

    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            models.LOCALUser.objects.get(email=email)
        except models.LOCALUser.DoesNotExist:
            try:
                models.LOCALUserRequest.objects.get(email=email)
            except models.LOCALUserRequest.DoesNotExist:
                return email
        raise forms.ValidationError(_('APPLICATION___SECURITY___LOGIN___REQUEST___VALIDATION This email has already been chosen.'))

    def clean(self):
        ___clean___ = super(LOCALUserLoginRequest, self).clean()
        # password and password_confirmation
        password = self.cleaned_data.get('password')
        password_confirmation = self.cleaned_data.get('password_confirmation')
        if password != password_confirmation:
            self.add_error('password', _('APPLICATION___SECURITY___LOGIN___REQUEST___VALIDATION The password and your confirmation do not match.'))
            self.add_error('password_confirmation', _('APPLICATION___SECURITY___LOGIN___REQUEST___VALIDATION The password and your confirmation do not match.'))
        return ___clean___

    def save(self, commit=True):
        instance = super(LOCALUserLoginRequest, self).save(commit=False)
        #
        if commit:
            # password
            password = self.cleaned_data.get('password')
            if password is not '':
                instance.___void___encrypt_password___(password=password)
            # save to data base
            instance.save()
        return instance


class LOCALUserProfile(forms.ModelForm):
    avatar = ___FIELD___PROFILE___AVATAR___
    first_name = ___FIELD___PROFILE___FIRST_NAME___
    last_name = ___FIELD___PROFILE___LAST_NAME___
    identifier = ___FIELD___PROFILE___IDENTIFIER___
    email = ___FIELD___PROFILE___EMAIL___
    password = ___FIELD___PROFILE___PASSWORD___
    password_confirmation = ___FIELD___PROFILE___PASSWORD_CONFIRMATION___

    class Meta:
        model = models.LOCALUser
        fields = ['avatar', 'first_name', 'last_name', 'identifier', 'email', 'password', ]

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        self.instance_current = kwargs.pop('instance_current')
        super().__init__(*args, **kwargs)
        #
        # first_name
        ___field___attribute___placeholder___locale___reload__(field=self.fields['first_name'], locale='APPLICATION___SECURITY___PROFILE___FIRST_NAME')
        self.fields['first_name'].widget.attrs['autofocus'] = True
        # last name
        ___field___attribute___placeholder___locale___reload__(field=self.fields['last_name'], locale='APPLICATION___SECURITY___PROFILE___LAST_NAME')
        # identifier
        ___field___attribute___placeholder___locale___reload__(field=self.fields['identifier'], locale='APPLICATION___SECURITY___PROFILE___IDENTIFIER')
        # email
        ___field___attribute___placeholder___locale___reload__(field=self.fields['email'], locale='APPLICATION___SECURITY___PROFILE___EMAIL')
        # password
        ___field___attribute___placeholder___locale___reload__(field=self.fields['password'], locale='APPLICATION___SECURITY___PROFILE___PASSWORD')
        # password_confirmation
        ___field___attribute___placeholder___locale___reload__(field=self.fields['password_confirmation'], locale='APPLICATION___SECURITY___PROFILE___PASSWORD_CONFIRMATION')

    def clean_avatar(self):
        avatar = self.cleaned_data.get('avatar')
        if self.files.get('avatar'):
            if len(self.files.get('avatar')) > 1 * 1024 * 1024:  # 1MB
                raise forms.ValidationError(_('APPLICATION___SECURITY___PROFILE___VALIDATION The avatar should not be beggear than %(weight)s.') % {'weight': '1mb', })
        return avatar

    def clean_identifier(self):
        identifier = self.cleaned_data.get('identifier')
        try:
            instance = models.LOCALUser.objects.get(identifier=identifier)
        except models.LOCALUser.DoesNotExist:
            return identifier
        if instance.identifier == self.instance_current.identifier:
            return identifier
        raise forms.ValidationError(_('APPLICATION___SECURITY___PROFILE___VALIDATION This identifier has already been chosen.'))

    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            instance = models.LOCALUser.objects.get(email=email)
        except models.LOCALUser.DoesNotExist:
            return email
        if instance.email == self.instance_current.email:
            return email
        raise forms.ValidationError(_('APPLICATION___SECURITY___PROFILE___VALIDATION This email has already been chosen.'))

    def clean(self):
        ___clean___ = super(LOCALUserProfile, self).clean()
        # password and password_confirmation
        password = self.cleaned_data.get('password')
        password_confirmation = self.cleaned_data.get('password_confirmation')
        if password != password_confirmation:
            self.add_error('password', _('APPLICATION___SECURITY___PROFILE___VALIDATION The password and your confirmation do not match.'))
            self.add_error('password_confirmation', _('APPLICATION___SECURITY___PROFILE___VALIDATION The password and your confirmation do not match.'))
        return ___clean___

    def save(self, commit=True):
        instance = super(LOCALUserProfile, self).save(commit=False)
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
                        instance.avatar = '%s/%s/%s.jpg' % (models.___LOCALUSER_FOLDER_PATH___, instance.identifier, instance.identifier,)
                        if os.path.exists(self.instance_current.avatar.path) and os.path.exists(self.instance_current.___string___folder_path___()):
                            os.rename(self.instance_current.avatar.path, '%s/%s.jpg' % (self.instance_current.___string___folder_path___(), instance.identifier,))
                            os.rename(self.instance_current.___string___folder_path___(), self.instance.___string___folder_path___())
            # password
            password = self.cleaned_data.get('password')
            if password is not '':
                instance.___void___encrypt_password___(password=password)
            else:
                instance.password = self.instance_current.password
            # save to data base
            instance.save()
        return instance


class LDAPUserLogin(forms.Form):
    ldap_group = forms.CharField(
        label=_('APPLICATION___SECURITY___LOGIN___LDAP_GROUP'),
        required=True,
        widget=forms.Select(
            attrs={
                'id': 'ldap_group',
                'class': 'form-control',
                'aria-describedby': 'ldap_group_icon',
                'icon': 'fa fa-object-group',
            },
        ),
    )
    ldap_identifier = ___FIELD___LOGIN___IDENTIFIER___
    ldap_password = ___FIELD___LOGIN___PASSWORD___

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super().__init__(*args, **kwargs)
        #
        # ldap_group
        choices = list()
        for group in settings.LDAP_SERVER_GROUPS_LIST:
            choices.append((group, group.upper()))
        self.fields['ldap_group'].widget.choices = tuple(choices)
        # identifier
        ___field___attribute___placeholder___locale___reload__(field=self.fields['ldap_identifier'], locale='APPLICATION___SECURITY___LOGIN___IDENTIFIER')
        self.fields['ldap_identifier'].widget.attrs['id'] = 'ldap_identifier'
        self.fields['ldap_identifier'].widget.attrs['aria-describedby'] = 'ldap_identifier_icon'
        # password
        ___field___attribute___placeholder___locale___reload__(field=self.fields['ldap_password'], locale='APPLICATION___SECURITY___LOGIN___PASSWORD')
        self.fields['ldap_password'].widget.attrs['id'] = 'ldap_password'
        self.fields['ldap_password'].widget.attrs['aria-describedby'] = 'ldap_password_icon'


class LDAPUserLoginForgotCredentials1(forms.ModelForm):
    email = ___FIELD___LOGIN___FORGOT_CREDENTIALS___EMAIL___

    class Meta:
        model = models.LDAPUserForgotCredentials
        fields = ['email', ]

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super().__init__(*args, **kwargs)
        #
        # email
        ___field___attribute___placeholder___locale___reload__(field=self.fields['email'], locale='APPLICATION___SECURITY___LOGIN___FORGOT_CREDENTIALS___EMAIL')
        ___field___attribute___help_text___locale___reload__(field=self.fields['email'], locale='APPLICATION___SECURITY___LOGIN___FORGOT_CREDENTIALS___EMAIL___HELP_TEXT')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            models.LDAPUser.objects.get(email=email)
        except models.LDAPUser.DoesNotExist:
            raise forms.ValidationError(_('APPLICATION___SECURITY___LOGIN___FORGOT_CREDENTIALS___VALIDATION This email address is not subscribed to any account.'))
        try:
            instance = models.LDAPUserForgotCredentials.objects.get(email=email)
        except models.LDAPUserForgotCredentials.DoesNotExist:
            return email
        minutes = instance.___int___time_of_existence___()
        minutes_max = instance.___INT___MAXIMUM_TIME_OF_EXISTENCE___
        if minutes_max <= minutes + 1:
            raise forms.ValidationError(_('APPLICATION___SECURITY___LOGIN___FORGOT_CREDENTIALS___VALIDATION In a few seconds you can try to recover your account.'))
        else:
            raise forms.ValidationError(_('APPLICATION___SECURITY___LOGIN___FORGOT_CREDENTIALS___VALIDATION It is been %(minutes)s minutes since you tried to recover your account, you should wait about %(minutes_max)s minutes.') % {'minutes': minutes, 'minutes_max': minutes_max, })

    def save(self, commit=True):
        instance = super(LDAPUserLoginForgotCredentials1, self).save(commit=False)
        #
        if commit:
            # code
            string___timezone = timezone.now().strftime('%Y%m%d%H%M%S')
            string___letters_digits = string.ascii_letters + string.digits
            string___code = string___timezone + ''.join([random.choice(string___letters_digits) for x in range(86)])  # 100 characteres = 14 + 86
            instance.code = string___code
            # save to data base
            instance.save()
        return instance


class LDAPUserLoginForgotCredentials2(forms.ModelForm):
    email = ___FIELD___LOGIN___FORGOT_CREDENTIALS___EMAIL___
    code_confirmation = ___FIELD___LOGIN___FORGOT_CREDENTIALS___CODE_CONFIRMATION___

    class Meta:
        model = models.LDAPUserForgotCredentials
        fields = ['email', ]

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super().__init__(*args, **kwargs)
        #
        # email
        ___field___attribute___placeholder___locale___reload__(field=self.fields['email'], locale='APPLICATION___SECURITY___LOGIN___FORGOT_CREDENTIALS___EMAIL')
        self.fields['email'].widget.attrs['readonly'] = True
        # code_confirmation
        ___field___attribute___placeholder___locale___reload__(field=self.fields['code_confirmation'], locale='APPLICATION___SECURITY___LOGIN___FORGOT_CREDENTIALS___CODE_CONFIRMATION')
        ___field___attribute___help_text___locale___reload__(field=self.fields['code_confirmation'], locale='APPLICATION___SECURITY___LOGIN___FORGOT_CREDENTIALS___CODE_CONFIRMATION___HELP_TEXT')

    def clean_email(self):
        return self.instance.email

    def clean_code_confirmation(self):
        code_confirmation = self.cleaned_data.get('code_confirmation')
        try:
            models.LDAPUserForgotCredentials.objects.get(email=self.instance.email, code=code_confirmation)
        except models.LDAPUserForgotCredentials.DoesNotExist:
            raise forms.ValidationError(_('APPLICATION___SECURITY___LOGIN___FORGOT_CREDENTIALS___VALIDATION This code is not correct.'))
        return code_confirmation

    def save(self, commit=True):
        instance = super(LDAPUserLoginForgotCredentials2, self).save(commit=False)
        #
        if commit:
            # save to data base
            instance.save()
        return instance


class LDAPUserLoginForgotCredentials3(forms.ModelForm):
    password = ___FIELD___LOGIN___FORGOT_CREDENTIALS___PASSWORD___
    password_confirmation = ___FIELD___LOGIN___FORGOT_CREDENTIALS___PASSWORD_CONFIRMATION___

    class Meta:
        model = models.LDAPUserForgotCredentials
        fields = ['password', ]

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        self.instance_mirror = kwargs.pop('instance_mirror')
        super().__init__(*args, **kwargs)
        #
        # password
        ___field___attribute___placeholder___locale___reload__(field=self.fields['password'], locale='APPLICATION___SECURITY___LOGIN___FORGOT_CREDENTIALS___PASSWORD')
        self.fields['password'].required = True
        # password_confirmation
        ___field___attribute___placeholder___locale___reload__(field=self.fields['password_confirmation'], locale='APPLICATION___SECURITY___LOGIN___FORGOT_CREDENTIALS___PASSWORD_CONFIRMATION')
        self.fields['password_confirmation'].required = True

    def clean(self):
        ___clean___ = super(LDAPUserLoginForgotCredentials3, self).clean()
        # password and password_confirmation
        password = str(self.cleaned_data.get('password')).strip()
        password_confirmation = str(self.cleaned_data.get('password_confirmation')).strip()
        if password != password_confirmation:
            self.add_error('password', _('APPLICATION___SECURITY___LOGIN___FORGOT_CREDENTIALS___VALIDATION The password and your confirmation do not match.'))
            self.add_error('password_confirmation', _('APPLICATION___SECURITY___LOGIN___FORGOT_CREDENTIALS___VALIDATION The password and your confirmation do not match.'))
        return ___clean___

    def save(self, commit=True):
        instance = super(LDAPUserLoginForgotCredentials3, self).save(commit=False)
        #
        if commit:
            # password
            password = str(self.cleaned_data.get('password')).strip()
            instance.___void___encrypt_password___(password=password)
            self.instance_mirror.___void___encrypt_password___(password=password)
            # save to data base
            instance.save()
            self.instance_mirror.save()
            #
            # LDAP
            ldap.___void___action___ldapuser_instance_update___(instance=self.instance_mirror)
        return instance


class LDAPUserLoginRequest(forms.ModelForm):
    first_name = ___FIELD___LOGIN___REQUEST___FIRST_NAME___
    last_name = ___FIELD___LOGIN___REQUEST___LAST_NAME___
    identifier = ___FIELD___LOGIN___REQUEST___IDENTIFIER___
    email = ___FIELD___LOGIN___REQUEST___EMAIL___
    password = ___FIELD___LOGIN___REQUEST___PASSWORD___
    password_confirmation = ___FIELD___LOGIN___REQUEST___PASSWORD_CONFIRMATION___
    detail = ___FIELD___LOGIN___REQUEST___DETAIL___
    institute = ___FIELD___LOGIN___REQUEST___INSTITUTE___
    researchField = ___FIELD___LOGIN___REQUEST___RESEARCH_FIELD___
    researchGroup = ___FIELD___LOGIN___REQUEST___RESEARCH_GROUP___
    userProfile = ___FIELD___LOGIN___REQUEST___USER_PROFILE___
    captcha = CaptchaField(label='CAPTCHA')

    class Meta:
        model = models.LDAPUserRequest
        fields = ['first_name', 'last_name', 'identifier', 'email', 'password', 'detail', 'institute', 'researchField', 'researchGroup', 'userProfile', ]

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super().__init__(*args, **kwargs)
        #
        # first_name
        ___field___attribute___placeholder___locale___reload__(field=self.fields['first_name'], locale='APPLICATION___SECURITY___LOGIN___REQUEST___FIRST_NAME')
        self.fields['first_name'].widget.attrs['autofocus'] = True
        # last name
        ___field___attribute___placeholder___locale___reload__(field=self.fields['last_name'], locale='APPLICATION___SECURITY___LOGIN___REQUEST___LAST_NAME')
        # identifier
        ___field___attribute___placeholder___locale___reload__(field=self.fields['identifier'], locale='APPLICATION___SECURITY___LOGIN___REQUEST___IDENTIFIER')
        # email
        ___field___attribute___placeholder___locale___reload__(field=self.fields['email'], locale='APPLICATION___SECURITY___LOGIN___REQUEST___EMAIL')
        # password
        ___field___attribute___placeholder___locale___reload__(field=self.fields['password'], locale='APPLICATION___SECURITY___LOGIN___REQUEST___PASSWORD')
        self.fields['password'].required = True
        # password_confirmation
        ___field___attribute___placeholder___locale___reload__(field=self.fields['password_confirmation'], locale='APPLICATION___SECURITY___LOGIN___REQUEST___PASSWORD_CONFIRMATION')
        self.fields['password_confirmation'].required = True
        # detail
        ___field___attribute___placeholder___locale___reload__(field=self.fields['detail'], locale='APPLICATION___SECURITY___LOGIN___REQUEST___DETAIL')
        ___field___attribute___help_text___locale___reload__(field=self.fields['detail'], locale='APPLICATION___SECURITY___LOGIN___REQUEST___DETAIL___HELP_TEXT')
        # institute
        ___field___attribute___placeholder___locale___reload__(field=self.fields['institute'], locale='APPLICATION___SECURITY___LOGIN___REQUEST___INSTITUTE')
        # researchField
        ___field___attribute___placeholder___locale___reload__(field=self.fields['researchField'], locale='APPLICATION___SECURITY___LOGIN___REQUEST___RESEARCH_FIELD')
        # researchGroup
        ___field___attribute___placeholder___locale___reload__(field=self.fields['researchGroup'], locale='APPLICATION___SECURITY___LOGIN___REQUEST___RESEARCH_GROUP')
        #  userProfile
        ___field___attribute___placeholder___locale___reload__(field=self.fields['userProfile'], locale='APPLICATION___SECURITY___LOGIN___REQUEST___USER_PROFILE')

    def clean_identifier(self):
        identifier = self.cleaned_data.get('identifier')
        try:
            models.LDAPUser.objects.get(identifier=identifier)
        except models.LDAPUser.DoesNotExist:
            try:
                models.LDAPUserRequest.objects.get(identifier=identifier)
            except models.LDAPUserRequest.DoesNotExist:
                return identifier
        raise forms.ValidationError(_('APPLICATION___SECURITY___LOGIN___REQUEST___VALIDATION This identifier has already been chosen.'))

    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            models.LDAPUser.objects.get(email=email)
        except models.LDAPUser.DoesNotExist:
            try:
                models.LDAPUserRequest.objects.get(email=email)
            except models.LDAPUserRequest.DoesNotExist:
                return email
        raise forms.ValidationError(_('APPLICATION___SECURITY___LOGIN___REQUEST___VALIDATION This email has already been chosen.'))

    def clean(self):
        ___clean___ = super(LDAPUserLoginRequest, self).clean()
        # password and password_confirmation
        identifier = str(self.cleaned_data.get('identifier')).lower()
        password = str(self.cleaned_data.get('password')).strip()
        password_confirmation = str(self.cleaned_data.get('password_confirmation')).strip()
        if password != password_confirmation:
            self.add_error('password', _('APPLICATION___SECURITY___LOGIN___REQUEST___VALIDATION The password and your confirmation do not match.'))
            self.add_error('password_confirmation', _('APPLICATION___SECURITY___LOGIN___REQUEST___VALIDATION The password and your confirmation do not match.'))
        return ___clean___

    def save(self, commit=True):
        instance = super(LDAPUserLoginRequest, self).save(commit=False)
        #
        if commit:
            # password
            password = str(self.cleaned_data.get('password')).strip()
            if password is not '':
                instance.___void___encrypt_password___(password=password)
            # save to data base
            instance.save()
        return instance


class LDAPUserProfile(forms.ModelForm):
    avatar = ___FIELD___PROFILE___AVATAR___
    first_name = ___FIELD___PROFILE___FIRST_NAME___
    last_name = ___FIELD___PROFILE___LAST_NAME___
    identifier = ___FIELD___PROFILE___IDENTIFIER___
    email = ___FIELD___PROFILE___EMAIL___
    password = ___FIELD___PROFILE___PASSWORD___
    password_confirmation = ___FIELD___PROFILE___PASSWORD_CONFIRMATION___

    class Meta:
        model = models.LDAPUser
        fields = ['avatar', 'first_name', 'last_name', 'identifier', 'email', 'password', ]

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        self.instance_current = kwargs.pop('instance_current')
        super().__init__(*args, **kwargs)
        #
        # first_name
        ___field___attribute___placeholder___locale___reload__(field=self.fields['first_name'], locale='APPLICATION___SECURITY___PROFILE___FIRST_NAME')
        self.fields['first_name'].widget.attrs['autofocus'] = True
        # last name
        ___field___attribute___placeholder___locale___reload__(field=self.fields['last_name'], locale='APPLICATION___SECURITY___PROFILE___LAST_NAME')
        # identifier
        ___field___attribute___placeholder___locale___reload__(field=self.fields['identifier'], locale='APPLICATION___SECURITY___PROFILE___IDENTIFIER')
        self.fields['identifier'].widget.attrs['readonly'] = 'readonly'
        # email
        ___field___attribute___placeholder___locale___reload__(field=self.fields['email'], locale='APPLICATION___SECURITY___PROFILE___EMAIL')
        # password
        ___field___attribute___placeholder___locale___reload__(field=self.fields['password'], locale='APPLICATION___SECURITY___PROFILE___PASSWORD')
        # password_confirmation
        ___field___attribute___placeholder___locale___reload__(field=self.fields['password_confirmation'], locale='APPLICATION___SECURITY___PROFILE___PASSWORD_CONFIRMATION')

    def clean_avatar(self):
        avatar = self.cleaned_data.get('avatar')
        if self.files.get('avatar'):
            if len(self.files.get('avatar')) > 1 * 1024 * 1024:  # 1MB
                raise forms.ValidationError(_('APPLICATION___SECURITY___PROFILE___VALIDATION The avatar should not be beggear than %(weight)s.') % {'weight': '1mb', })
        return avatar

    def clean_identifier(self):
        # identifier = self.cleaned_data.get('identifier')
        # try:
        #     instance = models.LDAPUser.objects.get(identifier=identifier)
        # except models.LDAPUser.DoesNotExist:
        #     return identifier
        # if instance.identifier == self.instance_current.identifier:
        #     return identifier
        # raise forms.ValidationError(_('APPLICATION___SECURITY___PROFILE___VALIDATION This identifier has already been chosen.'))
        identifier = self.instance_current.identifier
        return identifier

    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            instance = models.LDAPUser.objects.get(email=email)
        except models.LDAPUser.DoesNotExist:
            return email
        if instance.email == self.instance_current.email:
            return email
        raise forms.ValidationError(_('APPLICATION___SECURITY___PROFILE___VALIDATION This email has already been chosen.'))

    def clean(self):
        ___clean___ = super(LDAPUserProfile, self).clean()
        # password and password_confirmation
        password = str(self.cleaned_data.get('password')).strip()
        password_confirmation = str(self.cleaned_data.get('password_confirmation')).strip()
        if password != password_confirmation:
            self.add_error('password', _('APPLICATION___SECURITY___PROFILE___VALIDATION The password and your confirmation do not match.'))
            self.add_error('password_confirmation', _('APPLICATION___SECURITY___PROFILE___VALIDATION The password and your confirmation do not match.'))
        return ___clean___

    def save(self, commit=True):
        instance = super(LDAPUserProfile, self).save(commit=False)
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
                        instance.avatar = '%s/%s/%s.jpg' % (models.___LDAPUSER_FOLDER_PATH___, instance.identifier, instance.identifier,)
                        if os.path.exists(self.instance_current.avatar.path) and os.path.exists(self.instance_current.___string___folder_path___()):
                            os.rename(self.instance_current.avatar.path, '%s/%s.jpg' % (self.instance_current.___string___folder_path___(), instance.identifier,))
                            os.rename(self.instance_current.___string___folder_path___(), self.instance.___string___folder_path___())
            # password
            password = str(self.cleaned_data.get('password')).strip()
            if password is not '':
                instance.___void___encrypt_password___(password=password)
            else:
                instance.password = self.instance_current.password
            # save to data base
            instance.save()
            #
            # LDAP
            ldap.___void___action___ldapuser_instance_update___(instance=instance)
        return instance


class LDAPUserImportedProfile(forms.ModelForm):
    avatar = ___FIELD___PROFILE___AVATAR___
    first_name = ___FIELD___PROFILE___FIRST_NAME___
    last_name = ___FIELD___PROFILE___LAST_NAME___
    identifier = ___FIELD___PROFILE___IDENTIFIER___
    email = ___FIELD___PROFILE___EMAIL___

    class Meta:
        model = models.LDAPUserImported
        fields = ['avatar', 'first_name', 'last_name', 'identifier', 'email', ]

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        self.instance_current = kwargs.pop('instance_current')
        super().__init__(*args, **kwargs)
        #
        # first_name
        ___field___attribute___placeholder___locale___reload__(field=self.fields['first_name'], locale='APPLICATION___SECURITY___PROFILE___FIRST_NAME')
        self.fields['first_name'].widget.attrs['autofocus'] = True
        self.fields['first_name'].widget.attrs['readonly'] = 'readonly'
        # last name
        ___field___attribute___placeholder___locale___reload__(field=self.fields['last_name'], locale='APPLICATION___SECURITY___PROFILE___LAST_NAME')
        self.fields['last_name'].widget.attrs['readonly'] = 'readonly'
        # identifier
        ___field___attribute___placeholder___locale___reload__(field=self.fields['identifier'], locale='APPLICATION___SECURITY___PROFILE___IDENTIFIER')
        self.fields['identifier'].widget.attrs['readonly'] = 'readonly'
        # email
        ___field___attribute___placeholder___locale___reload__(field=self.fields['email'], locale='APPLICATION___SECURITY___PROFILE___EMAIL')
        self.fields['email'].widget.attrs['readonly'] = 'readonly'

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

    def clean_avatar(self):
        avatar = self.cleaned_data.get('avatar')
        if self.files.get('avatar'):
            if len(self.files.get('avatar')) > 1 * 1024 * 1024:  # 1MB
                raise forms.ValidationError(_('APPLICATION___SECURITY___PROFILE___VALIDATION The avatar should not be beggear than %(weight)s.') % {'weight': '1mb', })
        return avatar

    def save(self, commit=True):
        instance = super(LDAPUserImportedProfile, self).save(commit=False)
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
                        instance.avatar = '%s/%s/%s.jpg' % (models.___LDAPUSERIMPORTED_FOLDER_PATH___, instance.identifier, instance.identifier,)
                        if os.path.exists(self.instance_current.avatar.path) and os.path.exists(self.instance_current.___string___folder_path___()):
                            os.rename(self.instance_current.avatar.path, '%s/%s.jpg' % (self.instance_current.___string___folder_path___(), instance.identifier,))
                            os.rename(self.instance_current.___string___folder_path___(), self.instance.___string___folder_path___())
            # save to data base
            instance.save()
        return instance
