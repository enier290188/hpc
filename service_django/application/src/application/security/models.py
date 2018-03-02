# -*- coding: utf-8 -*-
from django.conf import settings
from django.db import models
from django.utils import timezone
from passlib.handlers import django as passlib___django
from passlib.hash import ldap_salted_sha1 as passlib___ldap_salted_sha1

___LOCALUSER_FOLDER_PATH___ = 'application/security/localuser'
___LDAPUSER_FOLDER_PATH___ = 'application/security/ldapuser'
___LDAPUSERIMPORTED_FOLDER_PATH___ = 'application/security/ldapuserimported'


class LOCALUserManager(models.Manager):
    def ___instances___(self, request):
        if isinstance(request.___APPLICATION___SECURITY___USER___, LOCALUser):
            instances = self.all().filter(is_superuser=False).exclude(pk=request.___APPLICATION___SECURITY___USER___.pk)
        else:
            instances = self.all().filter(is_superuser=False)
        instances = instances.order_by('first_name', 'identifier')
        return instances

    def ___instance___(self, request, pk):
        try:
            instance = self.get(pk=pk)
            if instance.is_superuser or (isinstance(request.___APPLICATION___SECURITY___USER___, LOCALUser) and request.___APPLICATION___SECURITY___USER___.pk == instance.pk):
                return None
        except LOCALUser.DoesNotExist:
            return None
        return instance

    def ___instance___by_pk___(self, pk):
        try:
            instance = self.get(pk=pk)
        except LOCALUser.DoesNotExist:
            return None
        return instance

    def ___instance___by_identifier___(self, identifier):
        try:
            instance = self.get(identifier=identifier)
        except LOCALUser.DoesNotExist:
            return None
        return instance

    def ___instance___by_email___(self, email):
        try:
            instance = self.get(email=email)
        except LOCALUser.DoesNotExist:
            return None
        return instance


class LOCALUser(models.Model):
    def ___AVATAR_UPLOAD_TO___(instance, filename):
        return '%s/%s/%s.jpg' % (___LOCALUSER_FOLDER_PATH___, instance.identifier, instance.identifier,)

    id = models.AutoField(
        primary_key=True,
    )
    is_active = models.BooleanField(
        default=True,
        null=False,
        blank=False,
    )
    created = models.DateTimeField(
        auto_now_add=True,
        auto_now=False,
        editable=True,
    )
    modified = models.DateTimeField(
        auto_now_add=False,
        auto_now=True,
        editable=True,
    )
    avatar = models.ImageField(
        null=True,
        blank=True,
        upload_to=___AVATAR_UPLOAD_TO___,
    )
    first_name = models.CharField(
        default='',
        max_length=100,
        null=True,
        blank=True,
    )
    last_name = models.CharField(
        default='',
        max_length=100,
        null=True,
        blank=True,
    )
    identifier = models.CharField(
        unique=True,
        max_length=100,
        null=False,
        blank=False,
    )
    email = models.CharField(
        unique=True,
        max_length=150,
        null=False,
        blank=False,
    )
    password = models.CharField(
        max_length=1024,
        null=False,
        blank=False,
    )
    detail = models.TextField(
        default='',
        max_length=1024,
        null=True,
        blank=True,
    )
    groups = models.ManyToManyField(
        'Group',
        related_name='localuser_groups_set',
        through='LOCALUserGroup',
        through_fields=('localuser', 'group')
    )
    permissions = models.ManyToManyField(
        'Permission',
        related_name='localuser_permissions_set',
        through='LOCALUserPermission',
        through_fields=('localuser', 'permission')
    )
    locale = models.CharField(
        default='',
        max_length=10,
        null=True,
        blank=True,
    )
    is_superuser = models.BooleanField(
        default=False,
        null=False,
        blank=False,
    )
    objects = LOCALUserManager()

    class Meta:
        db_table = 'application___security___localuser'
        ordering = ['id', ]

    def __str__(self):
        if self.first_name and self.last_name:
            return '%s %s' % (self.first_name, self.last_name,)
        if self.first_name:
            return '%s' % (self.first_name,)
        return self.identifier

    def save(self, *args, **kwargs):
        if self.password == '':
            self.___void___encrypt_password___(password='')
        return super(LOCALUser, self).save(*args, **kwargs)

    def ___string___folder_path___(self):
        return '%s/%s/%s' % (settings.MEDIA_ROOT, ___LOCALUSER_FOLDER_PATH___, self.identifier,)

    def ___void___encrypt_password___(self, password):
        self.password = passlib___django.django_pbkdf2_sha256.encrypt(password)

    def ___boolean___verify_password___(self, password):
        return passlib___django.django_pbkdf2_sha256.verify(password, self.password)

    def ___boolean___has_permission___(self, set_identifier___to_verify=set()):
        if self.is_superuser:
            return True
        if set_identifier___to_verify and self.groups and self.permissions:
            set_identifier = set()
            # groups
            instances___group = self.groups.filter(is_active=True)
            for instance___group in instances___group:
                instances___permission = instance___group.permissions.filter(is_active=True)
                for instance___permission in instances___permission:
                    set_identifier.add(instance___permission.identifier)
            # permissions
            instances___permission = self.permissions.all().filter(is_active=True)
            for instance___permission in instances___permission:
                set_identifier.add(instance___permission.identifier)
            #
            for identifier in set_identifier___to_verify:
                if identifier not in set_identifier:
                    return False
            return True
        else:
            return False


class LOCALUserForgotCredentialsManager(models.Manager):
    def ___instances___(self, request):
        instances = self.all()
        return instances

    def ___instance___(self, request, pk):
        try:
            instance = self.get(pk=pk)
        except LOCALUserForgotCredentials.DoesNotExist:
            return None
        return instance

    def ___instance___by_pk___(self, pk):
        try:
            instance = self.get(pk=pk)
        except LOCALUserForgotCredentials.DoesNotExist:
            return None
        return instance


class LOCALUserForgotCredentials(models.Model):
    id = models.AutoField(
        primary_key=True,
    )
    created = models.DateTimeField(
        auto_now_add=True,
        auto_now=False,
        editable=True,
    )
    modified = models.DateTimeField(
        auto_now_add=False,
        auto_now=True,
        editable=True,
    )
    email = models.CharField(
        unique=True,
        max_length=150,
        null=False,
        blank=False,
    )
    code = models.CharField(
        unique=True,
        max_length=100,
        null=False,
        blank=False,
    )
    password = models.CharField(
        default='',
        max_length=1024,
        null=True,
        blank=True,
    )
    objects = LOCALUserForgotCredentialsManager()
    #
    ___INT___MAXIMUM_TIME_OF_EXISTENCE___ = 15

    class Meta:
        db_table = 'application___security___localuserforgotcredentials'
        ordering = ['id', ]

    def __str__(self):
        return '%s-%s' % (self.email, self.code,)

    def ___void___encrypt_password___(self, password):
        self.password = passlib___django.django_pbkdf2_sha256.encrypt(password)

    def ___int___time_of_existence___(self):  # in minutes
        time___created = timezone.datetime.time(self.created)
        time___now = timezone.now()
        hour___created = time___created.hour
        hour___now = time___now.hour
        minute___created = time___created.minute
        minute___now = time___now.minute
        #
        if hour___created == hour___now:
            minutes = minute___now - minute___created
        else:
            minutes = 60 - minute___created + minute___now
        return minutes


class LOCALUserRequestManager(models.Manager):
    def ___instances___(self, request):
        instances = self.all()
        return instances

    def ___instance___(self, request, pk):
        try:
            instance = self.get(pk=pk)
        except LOCALUserRequest.DoesNotExist:
            return None
        return instance

    def ___instance___by_pk___(self, pk):
        try:
            instance = self.get(pk=pk)
        except LOCALUserRequest.DoesNotExist:
            return None
        return instance


class LOCALUserRequest(models.Model):
    id = models.AutoField(
        primary_key=True,
    )
    created = models.DateTimeField(
        auto_now_add=True,
        auto_now=False,
        editable=True,
    )
    modified = models.DateTimeField(
        auto_now_add=False,
        auto_now=True,
        editable=True,
    )
    first_name = models.CharField(
        default='',
        max_length=100,
        null=True,
        blank=True,
    )
    last_name = models.CharField(
        default='',
        max_length=100,
        null=True,
        blank=True,
    )
    identifier = models.CharField(
        unique=True,
        max_length=100,
        null=False,
        blank=False,
    )
    email = models.CharField(
        unique=True,
        max_length=150,
        null=False,
        blank=False,
    )
    password = models.CharField(
        max_length=1024,
        null=False,
        blank=False,
    )
    detail = models.TextField(
        default='',
        max_length=1024,
        null=True,
        blank=True,
    )
    objects = LOCALUserRequestManager()

    class Meta:
        db_table = 'application___security___localuserrequest'
        ordering = ['id', ]

    def __str__(self):
        if self.first_name and self.last_name:
            return '%s %s' % (self.first_name, self.last_name,)
        if self.first_name:
            return '%s' % (self.first_name,)
        return self.identifier

    def save(self, *args, **kwargs):
        if self.password == '':
            self.___void___encrypt_password___(password='')
        return super(LOCALUserRequest, self).save(*args, **kwargs)

    def ___void___encrypt_password___(self, password):
        self.password = passlib___django.django_pbkdf2_sha256.encrypt(password)


class LOCALUserGroupManager(models.Manager):
    pass


class LOCALUserGroup(models.Model):
    localuser = models.ForeignKey(
        'LOCALUser',
    )
    group = models.ForeignKey(
        'Group',
    )
    is_active = models.BooleanField(
        default=True,
        null=False,
        blank=False,
    )
    created = models.DateTimeField(
        auto_now_add=True,
        auto_now=False,
        editable=True,
    )
    modified = models.DateTimeField(
        auto_now_add=False,
        auto_now=True,
        editable=True,
    )
    objects = LOCALUserGroupManager()

    class Meta:
        db_table = 'application___security___localusergroup'
        ordering = ['localuser', 'group']

    def __str__(self):
        return '<%s> <%s>' % (self.localuser, self.group,)


class LOCALUserPermissionManager(models.Manager):
    pass


class LOCALUserPermission(models.Model):
    localuser = models.ForeignKey(
        'LOCALUser',
    )
    permission = models.ForeignKey(
        'Permission',
    )
    is_active = models.BooleanField(
        default=True,
        null=False,
        blank=False,
    )
    created = models.DateTimeField(
        auto_now_add=True,
        auto_now=False,
        editable=True,
    )
    modified = models.DateTimeField(
        auto_now_add=False,
        auto_now=True,
        editable=True,
    )
    objects = LOCALUserPermissionManager()

    class Meta:
        db_table = 'application___security___localuserpermission'
        ordering = ['localuser', 'permission']

    def __str__(self):
        return '<%s> <%s>' % (self.localuser, self.permission,)


class LDAPUserManager(models.Manager):
    def ___instances___(self, request):
        if isinstance(request.___APPLICATION___SECURITY___USER___, LDAPUser):
            instances = self.all().filter(is_superuser=False).exclude(pk=request.___APPLICATION___SECURITY___USER___.pk)
        else:
            instances = self.all().filter(is_superuser=False)
        instances = instances.order_by('first_name', 'identifier')
        return instances

    def ___instance___(self, request, pk):
        try:
            instance = self.get(pk=pk)
            if instance.is_superuser or (isinstance(request.___APPLICATION___SECURITY___USER___, LDAPUser) and request.___APPLICATION___SECURITY___USER___.pk == instance.pk):
                return None
        except LDAPUser.DoesNotExist:
            return None
        return instance

    def ___instance___by_pk___(self, pk):
        try:
            instance = self.get(pk=pk)
        except LDAPUser.DoesNotExist:
            return None
        return instance

    def ___instance___by_identifier___(self, identifier):
        try:
            instance = self.get(identifier=identifier)
        except LDAPUser.DoesNotExist:
            return None
        return instance

    def ___instance___by_email___(self, email):
        try:
            instance = self.get(email=email)
        except LDAPUser.DoesNotExist:
            return None
        return instance


class LDAPUser(models.Model):
    def ___AVATAR_UPLOAD_TO___(instance, filename):
        return '%s/%s/%s.jpg' % (___LDAPUSER_FOLDER_PATH___, instance.identifier, instance.identifier,)

    id = models.AutoField(
        primary_key=True,
    )
    is_active = models.BooleanField(
        default=True,
        null=False,
        blank=False,
    )
    created = models.DateTimeField(
        auto_now_add=True,
        auto_now=False,
        editable=True,
    )
    modified = models.DateTimeField(
        auto_now_add=False,
        auto_now=True,
        editable=True,
    )
    avatar = models.ImageField(
        null=True,
        blank=True,
        upload_to=___AVATAR_UPLOAD_TO___,
    )
    first_name = models.CharField(
        default='',
        max_length=100,
        null=True,
        blank=True,
    )
    last_name = models.CharField(
        default='',
        max_length=100,
        null=True,
        blank=True,
    )
    identifier = models.CharField(
        unique=True,
        max_length=100,
        null=False,
        blank=False,
    )
    email = models.CharField(
        unique=True,
        max_length=150,
        null=False,
        blank=False,
    )
    password = models.CharField(
        max_length=1024,
        null=False,
        blank=False,
    )
    detail = models.TextField(
        default='',
        max_length=1024,
        null=True,
        blank=True,
    )
    groups = models.ManyToManyField(
        'Group',
        related_name='ldapuser_groups_set',
        through='LDAPUserGroup',
        through_fields=('ldapuser', 'group')
    )
    permissions = models.ManyToManyField(
        'Permission',
        related_name='ldapuser_permissions_set',
        through='LDAPUserPermission',
        through_fields=('ldapuser', 'permission')
    )
    locale = models.CharField(
        default='',
        max_length=10,
        null=True,
        blank=True,
    )
    is_superuser = models.BooleanField(
        default=False,
        null=False,
        blank=False,
    )
    objects = LDAPUserManager()

    class Meta:
        db_table = 'application___security___ldapuser'
        ordering = ['id', ]

    def __str__(self):
        if self.first_name and self.last_name:
            return '%s %s' % (self.first_name, self.last_name,)
        if self.first_name:
            return '%s' % (self.first_name,)
        return self.identifier

    def save(self, *args, **kwargs):
        if self.password == '':
            self.___void___encrypt_password___(password='')
        return super(LDAPUser, self).save(*args, **kwargs)

    def ___string___folder_path___(self):
        return '%s/%s/%s' % (settings.MEDIA_ROOT, ___LDAPUSER_FOLDER_PATH___, self.identifier,)

    def ___void___encrypt_password___(self, password):
        self.password = passlib___ldap_salted_sha1.encrypt(password)

    def ___boolean___verify_password___(self, password):
        return passlib___ldap_salted_sha1.verify(password, self.password)

    def ___boolean___has_permission___(self, set_identifier___to_verify=set()):
        if self.is_superuser:
            return True
        if set_identifier___to_verify and self.groups and self.permissions:
            set_identifier = set()
            # groups
            instances___group = self.groups.filter(is_active=True)
            for instance___group in instances___group:
                instances___permission = instance___group.permissions.filter(is_active=True)
                for instance___permission in instances___permission:
                    set_identifier.add(instance___permission.identifier)
            # permissions
            instances___permission = self.permissions.all().filter(is_active=True)
            for instance___permission in instances___permission:
                set_identifier.add(instance___permission.identifier)
            #
            for identifier in set_identifier___to_verify:
                if identifier not in set_identifier:
                    return False
            return True
        else:
            return False


class LDAPUserImportedManager(models.Manager):
    def ___instances___(self, request):
        instances = self.all().order_by('ldap_group', 'identifier')
        return instances

    def ___instance___(self, request, pk):
        try:
            instance = self.get(pk=pk)
        except LDAPUserImported.DoesNotExist:
            return None
        return instance

    def ___instance___by_pk___(self, pk):
        try:
            instance = self.get(pk=pk)
        except LDAPUserImported.DoesNotExist:
            return None
        return instance

    def ___instance___by_identifier___(self, identifier):
        try:
            instance = self.get(identifier=identifier)
        except LDAPUserImported.DoesNotExist:
            return None
        return instance

    def ___instance___by_ldap_group_and_identifier___(self, ldap_group, identifier):
        try:
            instance = self.get(ldap_group=ldap_group, identifier=identifier)
        except LDAPUserImported.DoesNotExist:
            return None
        return instance


class LDAPUserImported(models.Model):
    def ___AVATAR_UPLOAD_TO___(instance, filename):
        return '%s/%s/%s/%s.jpg' % (___LDAPUSERIMPORTED_FOLDER_PATH___, instance.ldap_group, instance.identifier, instance.identifier,)

    id = models.AutoField(
        primary_key=True,
    )
    is_active = models.BooleanField(
        default=True,
        null=False,
        blank=False,
    )
    created = models.DateTimeField(
        auto_now_add=True,
        auto_now=False,
        editable=True,
    )
    modified = models.DateTimeField(
        auto_now_add=False,
        auto_now=True,
        editable=True,
    )
    avatar = models.ImageField(
        null=True,
        blank=True,
        upload_to=___AVATAR_UPLOAD_TO___,
    )
    first_name = models.CharField(
        default='',
        max_length=100,
        null=True,
        blank=True,
    )
    last_name = models.CharField(
        default='',
        max_length=100,
        null=True,
        blank=True,
    )
    ldap_group = models.CharField(
        max_length=100,
        null=True,
        blank=False,
    )
    identifier = models.CharField(
        max_length=100,
        null=False,
        blank=False,
    )
    email = models.CharField(
        max_length=150,
        null=False,
        blank=False,
    )
    password = models.CharField(
        max_length=1024,
        null=False,
        blank=False,
    )
    detail = models.TextField(
        default='',
        max_length=1024,
        null=True,
        blank=True,
    )
    locale = models.CharField(
        default='',
        max_length=10,
        null=True,
        blank=True,
    )
    objects = LDAPUserImportedManager()

    class Meta:
        unique_together = ('ldap_group', 'identifier', )
        db_table = 'application___security___ldapuserimported'
        ordering = ['id', ]

    def __str__(self):
        if self.first_name and self.last_name:
            return '%s %s' % (self.first_name, self.last_name,)
        if self.first_name:
            return '%s' % (self.first_name,)
        return self.identifier

    def save(self, *args, **kwargs):
        if self.password == '':
            self.___void___encrypt_password___(password='')
        return super(LDAPUserImported, self).save(*args, **kwargs)

    def ___string___folder_path___(self):
        return '%s/%s/%s/%s' % (settings.MEDIA_ROOT, ___LDAPUSERIMPORTED_FOLDER_PATH___, self.ldap_group, self.identifier,)

    def ___void___encrypt_password___(self, password):
        self.password = passlib___ldap_salted_sha1.encrypt(password)

    def ___boolean___verify_password___(self, password):
        return passlib___ldap_salted_sha1.verify(password, self.password)


class LDAPUserForgotCredentialsManager(models.Manager):
    def ___instances___(self, request):
        instances = self.all()
        return instances

    def ___instance___(self, request, pk):
        try:
            instance = self.get(pk=pk)
        except LDAPUserForgotCredentials.DoesNotExist:
            return None
        return instance

    def ___instance___by_pk___(self, pk):
        try:
            instance = self.get(pk=pk)
        except LDAPUserForgotCredentials.DoesNotExist:
            return None
        return instance


class LDAPUserForgotCredentials(models.Model):
    id = models.AutoField(
        primary_key=True,
    )
    created = models.DateTimeField(
        auto_now_add=True,
        auto_now=False,
        editable=True,
    )
    modified = models.DateTimeField(
        auto_now_add=False,
        auto_now=True,
        editable=True,
    )
    email = models.CharField(
        unique=True,
        max_length=150,
        null=False,
        blank=False,
    )
    code = models.CharField(
        unique=True,
        max_length=100,
        null=False,
        blank=False,
    )
    password = models.CharField(
        default='',
        max_length=1024,
        null=True,
        blank=True,
    )
    objects = LDAPUserForgotCredentialsManager()
    #
    ___INT___MAXIMUM_TIME_OF_EXISTENCE___ = 15

    class Meta:
        db_table = 'application___security___ldapuserforgotcredentials'
        ordering = ['id', ]

    def __str__(self):
        return '%s-%s' % (self.email, self.code,)

    def ___void___encrypt_password___(self, password):
        self.password = passlib___ldap_salted_sha1.encrypt(password)

    def ___int___time_of_existence___(self):  # in minutes
        time___created = timezone.datetime.time(self.created)
        time___now = timezone.now()
        hour___created = time___created.hour
        hour___now = time___now.hour
        minute___created = time___created.minute
        minute___now = time___now.minute
        #
        if hour___created == hour___now:
            minutes = minute___now - minute___created
        else:
            minutes = 60 - minute___created + minute___now
        return minutes


class LDAPUserRequestManager(models.Manager):
    def ___instances___(self, request):
        instances = self.all()
        return instances

    def ___instance___(self, request, pk):
        try:
            instance = self.get(pk=pk)
        except LDAPUserRequest.DoesNotExist:
            return None
        return instance

    def ___instance___by_pk___(self, pk):
        try:
            instance = self.get(pk=pk)
        except LDAPUserRequest.DoesNotExist:
            return None
        return instance


class LDAPUserRequest(models.Model):
    id = models.AutoField(
        primary_key=True,
    )
    created = models.DateTimeField(
        auto_now_add=True,
        auto_now=False,
        editable=True,
    )
    modified = models.DateTimeField(
        auto_now_add=False,
        auto_now=True,
        editable=True,
    )
    first_name = models.CharField(
        default='',
        max_length=100,
        null=True,
        blank=True,
    )
    last_name = models.CharField(
        default='',
        max_length=100,
        null=True,
        blank=True,
    )
    identifier = models.CharField(
        unique=True,
        max_length=100,
        null=False,
        blank=False,
    )
    email = models.CharField(
        unique=True,
        max_length=150,
        null=False,
        blank=False,
    )
    password = models.CharField(
        max_length=1024,
        null=False,
        blank=False,
    )
    detail = models.TextField(
        default='',
        max_length=1024,
        null=True,
        blank=True,
    )
    objects = LDAPUserRequestManager()

    class Meta:
        db_table = 'application___security___ldapuserrequest'
        ordering = ['id', ]

    def __str__(self):
        if self.first_name and self.last_name:
            return '%s %s' % (self.first_name, self.last_name,)
        if self.first_name:
            return '%s' % (self.first_name,)
        return self.identifier

    def save(self, *args, **kwargs):
        if self.password == '':
            self.___void___encrypt_password___(password='')
        return super(LDAPUserRequest, self).save(*args, **kwargs)

    def ___void___encrypt_password___(self, password):
        self.password = passlib___ldap_salted_sha1.encrypt(password)


class LDAPUserGroupManager(models.Manager):
    pass


class LDAPUserGroup(models.Model):
    ldapuser = models.ForeignKey(
        'LDAPUser',
    )
    group = models.ForeignKey(
        'Group',
    )
    is_active = models.BooleanField(
        default=True,
        null=False,
        blank=False,
    )
    created = models.DateTimeField(
        auto_now_add=True,
        auto_now=False,
        editable=True,
    )
    modified = models.DateTimeField(
        auto_now_add=False,
        auto_now=True,
        editable=True,
    )
    objects = LDAPUserGroupManager()

    class Meta:
        db_table = 'application___security___ldapusergroup'
        ordering = ['ldapuser', 'group']

    def __str__(self):
        return '<%s> <%s>' % (self.ldapuser, self.group,)


class LDAPUserPermissionManager(models.Manager):
    pass


class LDAPUserPermission(models.Model):
    ldapuser = models.ForeignKey(
        'LDAPUser',
    )
    permission = models.ForeignKey(
        'Permission',
    )
    is_active = models.BooleanField(
        default=True,
        null=False,
        blank=False,
    )
    created = models.DateTimeField(
        auto_now_add=True,
        auto_now=False,
        editable=True,
    )
    modified = models.DateTimeField(
        auto_now_add=False,
        auto_now=True,
        editable=True,
    )
    objects = LDAPUserPermissionManager()

    class Meta:
        db_table = 'application___security___ldapuserpermission'
        ordering = ['ldapuser', 'permission']

    def __str__(self):
        return '<%s> <%s>' % (self.ldapuser, self.permission,)


class GroupManager(models.Manager):
    def ___instances___(self, request):
        instances = self.all()
        instances___position_not_equal_0 = instances.exclude(position__lte=0)
        instances___position_equal_0 = instances.exclude(position__gt=0)
        int___position = 1
        if instances___position_not_equal_0.count() > 0:
            for instance in instances___position_not_equal_0:
                instance.position = int___position
                instance.save()
                int___position += 1
        if instances___position_equal_0.count() > 0:
            for instance in instances___position_equal_0:
                instance.position = int___position
                instance.save()
                int___position += 1
        instances = self.all()
        return instances

    def ___instance___(self, request, pk):
        try:
            instance = self.get(pk=pk)
        except Group.DoesNotExist:
            return None
        return instance

    def ___instance___by_pk___(self, pk):
        try:
            instance = self.get(pk=pk)
        except Group.DoesNotExist:
            return None
        return instance


class Group(models.Model):
    id = models.AutoField(
        primary_key=True,
    )
    is_active = models.BooleanField(
        default=True,
        null=False,
        blank=False,
    )
    created = models.DateTimeField(
        auto_now_add=True,
        auto_now=False,
        editable=True,
    )
    modified = models.DateTimeField(
        auto_now_add=False,
        auto_now=True,
        editable=True,
    )
    name = models.CharField(
        unique=True,
        max_length=100,
        null=False,
        blank=False,
    )
    permissions = models.ManyToManyField(
        'Permission',
        related_name='group_permissions_set',
        through='GroupPermission',
        through_fields=('group', 'permission')
    )
    parent = models.PositiveIntegerField(
        default=0,
        null=True,
        blank=True,
    )
    position = models.PositiveIntegerField(
        default=0,
        null=True,
        blank=True,
    )
    objects = GroupManager()

    class Meta:
        db_table = 'application___security___group'
        ordering = ['position', 'id', ]

    def __str__(self):
        return self.name


class PermissionManager(models.Manager):
    def ___instances___(self, request):
        instances = self.all()
        return instances

    def ___instance___(self, request, pk):
        try:
            instance = self.get(pk=pk)
        except Permission.DoesNotExist:
            return None
        return instance

    def ___instance___by_pk___(self, pk):
        try:
            instance = self.get(pk=pk)
        except Permission.DoesNotExist:
            return None
        return instance


class Permission(models.Model):
    id = models.AutoField(
        primary_key=True,
    )
    is_active = models.BooleanField(
        default=True,
        null=False,
        blank=False,
    )
    created = models.DateTimeField(
        auto_now_add=True,
        auto_now=False,
        editable=True,
    )
    modified = models.DateTimeField(
        auto_now_add=False,
        auto_now=True,
        editable=True,
    )
    name = models.CharField(
        unique=True,
        max_length=100,
        null=False,
        blank=False,
    )
    identifier = models.CharField(
        unique=True,
        max_length=100,
        null=False,
        blank=False,
    )
    objects = PermissionManager()

    class Meta:
        db_table = 'application___security___permission'
        ordering = ['id', ]

    def __str__(self):
        return self.name


class GroupPermissionManager(models.Manager):
    pass


class GroupPermission(models.Model):
    group = models.ForeignKey(
        'Group',
    )
    permission = models.ForeignKey(
        'Permission',
    )
    is_active = models.BooleanField(
        default=True,
        null=False,
        blank=False,
    )
    created = models.DateTimeField(
        auto_now_add=True,
        auto_now=False,
        editable=True,
    )
    modified = models.DateTimeField(
        auto_now_add=False,
        auto_now=True,
        editable=True,
    )
    objects = GroupPermissionManager()

    class Meta:
        db_table = 'application___security___grouppermission'
        ordering = ['group', 'permission']

    def __str__(self):
        return '<%s> <%s>' % (self.group, self.permission,)
