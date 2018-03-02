# -*- coding: utf-8 -*-
from src.application.security import ldap, models
from django import forms
from django.core import validators
from django.utils.translation import ugettext_lazy as _
import os
import shutil

___FIELD___IS_ACTIVE___ = forms.BooleanField(
    label=_('APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_SECURITY___LDAPUSER___IS_ACTIVE'),
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
    label=_('APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_SECURITY___LDAPUSER___CREATED'),
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
    label=_('APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_SECURITY___LDAPUSER___MODIFIED'),
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
    label=_('APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_SECURITY___LDAPUSER___AVATAR'),
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
    label=_('APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_SECURITY___LDAPUSER___FIRST_NAME'),
    required=False,
    min_length=1,
    max_length=100,
    validators=[
        validators.RegexValidator('^[\w .\-_]+$', message=_('APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_SECURITY___LDAPUSER___VALIDATION Only letters, numbers and special characters dot, -, _ and space.')),
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
___FIELD___LAST_NAME___ = forms.CharField(
    label=_('APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_SECURITY___LDAPUSER___LAST_NAME'),
    required=False,
    min_length=1,
    max_length=100,
    validators=[
        validators.RegexValidator('^[\w .\-_]+$', message=_('APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_SECURITY___LDAPUSER___VALIDATION Only letters, numbers and special characters dot, -, _ and space.')),
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
___FIELD___IDENTIFIER___ = forms.CharField(
    label=_('APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_SECURITY___LDAPUSER___IDENTIFIER'),
    required=True,
    min_length=1,
    max_length=100,
    validators=[
        validators.RegexValidator('^[\w_]+$', message=_('APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_SECURITY___LDAPUSER___VALIDATION Only letters, numbers and the special character _.')),
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
___FIELD___EMAIL___ = forms.EmailField(
    label=_('APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_SECURITY___LDAPUSER___EMAIL'),
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
___FIELD___PASSWORD___ = forms.CharField(
    label=_('APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_SECURITY___LDAPUSER___PASSWORD'),
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
___FIELD___PASSWORD_CONFIRMATION___ = forms.CharField(
    label=_('APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_SECURITY___LDAPUSER___PASSWORD_CONFIRMATION'),
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
___FIELD___DETAIL___ = forms.CharField(
    label=_('APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_SECURITY___LDAPUSER___DETAIL'),
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
___FIELD___GROUPS___ = forms.ModelMultipleChoiceField(
    label=_('APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_SECURITY___LDAPUSER___GROUPS'),
    required=False,
    widget=forms.CheckboxSelectMultiple(
        attrs={
            'id': 'groups',
            'class': 'form-control',
            'aria-describedby': 'groups_icon',
            'icon': 'fa fa-object-group',
        },
    ),
    queryset=models.Group.objects.all(),
)
___FIELD___PERMISSIONS___ = forms.ModelMultipleChoiceField(
    label=_('APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_SECURITY___LDAPUSER___PERMISSIONS'),
    required=False,
    widget=forms.CheckboxSelectMultiple(
        attrs={
            'id': 'permissions',
            'class': 'form-control',
            'aria-describedby': 'permissions_icon',
            'icon': 'fa fa-unlock',
        },
    ),
    queryset=models.Permission.objects.all(),
)


def ___field___attribute___placeholder___locale___reload__(field, locale):
    field.widget.attrs['placeholder'] = '- %s -' % (_(locale),)


def ___field___attribute___help_text___locale___reload__(field, locale):
    field.help_text = '\"%s\"' % (_(locale),)


class LDAPUserCreate(forms.ModelForm):
    is_active = ___FIELD___IS_ACTIVE___
    first_name = ___FIELD___FIRST_NAME___
    last_name = ___FIELD___LAST_NAME___
    identifier = ___FIELD___IDENTIFIER___
    email = ___FIELD___EMAIL___
    password = ___FIELD___PASSWORD___
    password_confirmation = ___FIELD___PASSWORD_CONFIRMATION___
    detail = ___FIELD___DETAIL___
    groups = ___FIELD___GROUPS___
    permissions = ___FIELD___PERMISSIONS___

    class Meta:
        model = models.LDAPUser
        fields = ['is_active', 'first_name', 'last_name', 'identifier', 'email', 'password', 'detail', 'groups', 'permissions', ]

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super().__init__(*args, **kwargs)
        #
        # is_active
        ___field___attribute___help_text___locale___reload__(field=self.fields['is_active'], locale='APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_SECURITY___LDAPUSER___IS_ACTIVE___HELP_TEXT')
        self.fields['is_active'].initial = True
        # first_name
        ___field___attribute___placeholder___locale___reload__(field=self.fields['first_name'], locale='APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_SECURITY___LDAPUSER___FIRST_NAME')
        self.fields['first_name'].widget.attrs['autofocus'] = True
        # last name
        ___field___attribute___placeholder___locale___reload__(field=self.fields['last_name'], locale='APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_SECURITY___LDAPUSER___LAST_NAME')
        # identifier
        ___field___attribute___placeholder___locale___reload__(field=self.fields['identifier'], locale='APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_SECURITY___LDAPUSER___IDENTIFIER')
        # email
        ___field___attribute___placeholder___locale___reload__(field=self.fields['email'], locale='APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_SECURITY___LDAPUSER___EMAIL')
        # password
        ___field___attribute___placeholder___locale___reload__(field=self.fields['password'], locale='APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_SECURITY___LDAPUSER___PASSWORD')
        # password_confirmation
        ___field___attribute___placeholder___locale___reload__(field=self.fields['password_confirmation'], locale='APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_SECURITY___LDAPUSER___PASSWORD_CONFIRMATION')
        # detail
        ___field___attribute___placeholder___locale___reload__(field=self.fields['detail'], locale='APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_SECURITY___LDAPUSER___DETAIL')
        ___field___attribute___help_text___locale___reload__(field=self.fields['detail'], locale='APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_SECURITY___LDAPUSER___DETAIL___HELP_TEXT')
        # groups
        self.groups_choices = models.Group.objects.all()
        # permissions
        self.permissions_choices = models.Permission.objects.all()

    def clean_identifier(self):
        identifier = self.cleaned_data.get('identifier')
        try:
            models.LDAPUser.objects.get(identifier=identifier)
        except models.LDAPUser.DoesNotExist:
            try:
                models.LDAPUserRequest.objects.get(identifier=identifier)
            except models.LDAPUserRequest.DoesNotExist:
                return identifier
        raise forms.ValidationError(_('APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_SECURITY___LDAPUSER___VALIDATION This identifier has already been chosen.'))

    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            models.LDAPUser.objects.get(email=email)
        except models.LDAPUser.DoesNotExist:
            try:
                models.LDAPUserRequest.objects.get(email=email)
            except models.LDAPUserRequest.DoesNotExist:
                return email
        raise forms.ValidationError(_('APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_SECURITY___LDAPUSER___VALIDATION This email has already been chosen.'))

    def clean(self):
        ___clean___ = super(LDAPUserCreate, self).clean()
        # password and password_confirmation
        password = self.cleaned_data.get('password')
        password_confirmation = self.cleaned_data.get('password_confirmation')
        if password != password_confirmation:
            self.add_error('password', _('APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_SECURITY___LDAPUSER___VALIDATION The password and your confirmation do not match.'))
            self.add_error('password_confirmation', _('APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_SECURITY___LDAPUSER___VALIDATION The password and your confirmation do not match.'))
        return ___clean___

    def save(self, commit=True):
        instance = super(LDAPUserCreate, self).save(commit=False)
        #
        if commit:
            # password
            password = self.cleaned_data.get('password')
            instance.___void___encrypt_password___(password=password)
            # save to data base
            instance.save()
            #
            # groups
            # groups seleccionados en el formulario
            groups_selected = self.cleaned_data.get('groups')
            # to add groups
            for group_selected in groups_selected:
                instance___ldapusergroup = models.LDAPUserGroup(ldapuser=instance, group=group_selected)
                instance___ldapusergroup.save()
            # permissions
            # permissions seleccionados en el formulario
            permissions_selected = self.cleaned_data.get('permissions')
            # to add permissions
            for permission_selected in permissions_selected:
                instance___ldapuserpermission = models.LDAPUserPermission(ldapuser=instance, permission=permission_selected)
                instance___ldapuserpermission.save()
            #
            # LDAP
            ldap.___void___action___ldapuser_instance_create___(instance=instance)
        return instance


class LDAPUserDetail(forms.ModelForm):
    is_active = ___FIELD___IS_ACTIVE___
    created = ___FIELD___CREATED___
    modified = ___FIELD___MODIFIED___
    avatar = ___FIELD___AVATAR___
    first_name = ___FIELD___FIRST_NAME___
    last_name = ___FIELD___LAST_NAME___
    identifier = ___FIELD___IDENTIFIER___
    email = ___FIELD___EMAIL___
    detail = ___FIELD___DETAIL___
    groups = ___FIELD___GROUPS___
    permissions = ___FIELD___PERMISSIONS___

    class Meta:
        model = models.LDAPUser
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super().__init__(*args, **kwargs)

    def ___detail___(self):
        #
        # LDAP
        ldap.___void___action___ldapuser_instance_update___(instance=self.instance)


class LDAPUserUpdate(forms.ModelForm):
    is_active = ___FIELD___IS_ACTIVE___
    avatar = ___FIELD___AVATAR___
    first_name = ___FIELD___FIRST_NAME___
    last_name = ___FIELD___LAST_NAME___
    identifier = ___FIELD___IDENTIFIER___
    email = ___FIELD___EMAIL___
    password = ___FIELD___PASSWORD___
    password_confirmation = ___FIELD___PASSWORD_CONFIRMATION___
    detail = ___FIELD___DETAIL___
    groups = ___FIELD___GROUPS___
    permissions = ___FIELD___PERMISSIONS___

    class Meta:
        model = models.LDAPUser
        fields = ['is_active', 'avatar', 'first_name', 'last_name', 'identifier', 'email', 'password', 'detail', 'groups', 'permissions', ]

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        self.instance_current = kwargs.pop('instance_current')
        super().__init__(*args, **kwargs)
        #
        # is_active
        ___field___attribute___help_text___locale___reload__(field=self.fields['is_active'], locale='APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_SECURITY___LDAPUSER___IS_ACTIVE___HELP_TEXT')
        # first_name
        ___field___attribute___placeholder___locale___reload__(field=self.fields['first_name'], locale='APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_SECURITY___LDAPUSER___FIRST_NAME')
        self.fields['first_name'].widget.attrs['autofocus'] = True
        # last name
        ___field___attribute___placeholder___locale___reload__(field=self.fields['last_name'], locale='APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_SECURITY___LDAPUSER___LAST_NAME')
        # identifier
        ___field___attribute___placeholder___locale___reload__(field=self.fields['identifier'], locale='APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_SECURITY___LDAPUSER___IDENTIFIER')
        # email
        ___field___attribute___placeholder___locale___reload__(field=self.fields['email'], locale='APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_SECURITY___LDAPUSER___EMAIL')
        # password
        ___field___attribute___placeholder___locale___reload__(field=self.fields['password'], locale='APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_SECURITY___LDAPUSER___PASSWORD')
        # password_confirmation
        ___field___attribute___placeholder___locale___reload__(field=self.fields['password_confirmation'], locale='APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_SECURITY___LDAPUSER___PASSWORD_CONFIRMATION')
        # detail
        ___field___attribute___placeholder___locale___reload__(field=self.fields['detail'], locale='APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_SECURITY___LDAPUSER___DETAIL')
        ___field___attribute___help_text___locale___reload__(field=self.fields['detail'], locale='APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_SECURITY___LDAPUSER___DETAIL___HELP_TEXT')
        # groups
        self.groups_choices = models.Group.objects.all()
        # permissions
        self.permissions_choices = models.Permission.objects.all()

    def clean_avatar(self):
        avatar = self.cleaned_data.get('avatar')
        if self.files.get('avatar'):
            if len(self.files.get('avatar')) > 1 * 1024 * 1024:  # 1MB
                raise forms.ValidationError(_('APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_SECURITY___LDAPUSER___VALIDATION The avatar should not be beggear than %(weight)s.') % {'weight': '1mb', })
        return avatar

    def clean_identifier(self):
        identifier = self.cleaned_data.get('identifier')
        try:
            instance = models.LDAPUser.objects.get(identifier=identifier)
        except models.LDAPUser.DoesNotExist:
            try:
                instance = models.LDAPUserRequest.objects.get(identifier=identifier)
            except models.LDAPUserRequest.DoesNotExist:
                return identifier
        if instance.identifier == self.instance_current.identifier:
            return identifier
        raise forms.ValidationError(_('APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_SECURITY___LDAPUSER___VALIDATION This identifier has already been chosen.'))

    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            instance = models.LDAPUser.objects.get(email=email)
        except models.LDAPUser.DoesNotExist:
            try:
                instance = models.LDAPUserRequest.objects.get(email=email)
            except models.LDAPUserRequest.DoesNotExist:
                return email
        if instance.email == self.instance_current.email:
            return email
        raise forms.ValidationError(_('APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_SECURITY___LDAPUSER___VALIDATION This email has already been chosen.'))

    def clean(self):
        ___clean___ = super(LDAPUserUpdate, self).clean()
        # password and password_confirmation
        password = self.cleaned_data.get('password')
        password_confirmation = self.cleaned_data.get('password_confirmation')
        if password != password_confirmation:
            self.add_error('password', _('APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_SECURITY___LDAPUSER___VALIDATION The password and your confirmation do not match.'))
            self.add_error('password_confirmation', _('APPLICATION___ADMINISTRATION___CONTENT___ADMINISTRATION_SECURITY___LDAPUSER___VALIDATION The password and your confirmation do not match.'))
        return ___clean___

    def save(self, commit=True):
        instance = super(LDAPUserUpdate, self).save(commit=False)
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
            password = self.cleaned_data.get('password')
            if password is not '':
                instance.___void___encrypt_password___(password=password)
            # groups
            # groups a los que pertenece
            instances___group = instance.groups.all()
            # groups seleccionados en el formulario
            groups_selected = self.cleaned_data.get('groups')
            # groups que tenian que no se seleccionaron ahora
            instances___group_to_delete = [x for x in instances___group if x not in groups_selected]
            # groups que se seleccionaron ahora que no tenia
            instances___group_to_add = [x for x in groups_selected if x not in instances___group]
            # to delete groups
            for instance___group_to_delete in instances___group_to_delete:
                instance___ldapusergroup = models.LDAPUserGroup.objects.get(ldapuser=instance, group=instance___group_to_delete)
                instance___ldapusergroup.delete()
            # to add groups
            for instance___group_to_add in instances___group_to_add:
                instance___ldapusergroup = models.LDAPUserGroup(ldapuser=instance, group=instance___group_to_add)
                instance___ldapusergroup.save()
            # permissions
            # permissions a los que pertenece
            instances___permission = instance.permissions.all()
            # permissions seleccionados en el formulario
            permissions_selected = self.cleaned_data.get('permissions')
            # permissions que tenian que no se seleccionaron ahora
            instances___permission_to_delete = [x for x in instances___permission if x not in permissions_selected]
            # permissions que se seleccionaron ahora que no tenia
            instances___permission_to_add = [x for x in permissions_selected if x not in instances___permission]
            # to delete permissions
            for instance___permission_to_delete in instances___permission_to_delete:
                instance___ldapuserpermission = models.LDAPUserPermission.objects.get(ldapuser=instance, permission=instance___permission_to_delete)
                instance___ldapuserpermission.delete()
            # to add permissions
            for instance___permission_to_add in instances___permission_to_add:
                instance___ldapuserpermission = models.LDAPUserPermission(ldapuser=instance, permission=instance___permission_to_add)
                instance___ldapuserpermission.save()
            # save to data base
            instance.save()
            #
            # LDAP
            ldap.___void___action___ldapuser_instance_update___(instance=instance)
        return instance


class LDAPUserDelete(forms.ModelForm):
    class Meta:
        model = models.LDAPUser
        fields = ['id', ]

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super().__init__(*args, **kwargs)

    def ___delete___(self):
        # avatar
        if self.instance.avatar is not None and self.instance.avatar != '':
            if os.path.exists(self.instance.___string___folder_path___()):
                shutil.rmtree(self.instance.___string___folder_path___())
        # instance delete
        self.instance.delete()
        #
        # LDAP
        ldap.___void___action___ldapuser_instance_delete___(instance=self.instance)
