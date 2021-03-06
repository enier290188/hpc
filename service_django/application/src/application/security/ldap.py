# -*- coding: utf-8 -*-
from . import models
from django.conf import settings
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _
import ldap3
import os
import shutil


def ___connection___ldap___():
    # The server and the connection are created with the default parameters
    # define the server
    # define an unsecure LDAP server, requesting info on DSE and schema
    server = ldap3.Server(
        host=settings.LDAP_SERVER_HOST,
        port=settings.LDAP_SERVER_PORT,
        use_ssl=False,
        get_info=ldap3.ALL
    )
    # define the connection
    connection = ldap3.Connection(
        server=server,
        user=settings.LDAP_SERVER_USER,
        password=settings.LDAP_SERVER_PASSWORD,
        auto_bind='NONE',
        version=3,
        authentication='SIMPLE',
        client_strategy='SYNC',
        auto_referrals=True,
        check_names=True,
        read_only=False,
        lazy=False,
        raise_exceptions=False
    )
    return connection


##########################################################################################
def ___boolean___ldap___ldapuser_group_instances_search___(connection):
    # perform the operation search
    boolean___is_find = connection.search(
        search_base=settings.LDAP_SERVER_GROUPS_SEARCH_BASE,
        search_filter='(&(objectClass=posixGroup)(objectClass=hpcCubaGroup))',
        search_scope=ldap3.SUBTREE,
        attributes=['cn', 'gidNumber', ]
    )
    return boolean___is_find


def ___boolean___ldap___ldapuser_instances_search___(connection, string___gidnumber):
    # perform the operation search
    boolean___is_find = connection.search(
        search_base=settings.LDAP_SERVER_GROUPS_SEARCH_BASE,
        search_filter='(&(objectClass=posixGroup)(objectClass=hpcCubaGroup)(gidNumber=%s))' % (string___gidnumber,),
        search_scope=ldap3.SUBTREE,
        attributes=['cn', 'gidNumber', ]
    )
    if boolean___is_find:
        boolean___is_find = connection.search(
            search_base='ou=%s,%s' % (str(connection.entries[0].cn), settings.LDAP_SERVER_USERS_SEARCH_BASE,),
            search_filter='(&(objectClass=inetOrgPerson)(objectClass=posixAccount)(objectClass=top)(objectClass=hpcCubaUser)(gidNumber=%s))' % (string___gidnumber,),
            search_scope=ldap3.SUBTREE,
            attributes=['uid', 'uidNumber', 'gidNumber', 'givenName', 'sn', 'mail', 'userPassword', 'description', 'homeDirectory', 'institute', 'researchField', 'researchGroup', 'userProfile', 'tutorInstitution', 'tutorMail', 'tutorName', ]
        )
    return boolean___is_find


def ___boolean___ldap___ldapuser_instance_search___(connection, instance):
    # perform the operation search
    boolean___is_find = connection.search(
        search_base='ou=%s,%s' % (settings.LDAP_SERVER_GROUPS_GROUP_CN, settings.LDAP_SERVER_USERS_SEARCH_BASE,),
        search_filter='(&(objectClass=inetOrgPerson)(objectClass=posixAccount)(objectClass=top)(objectClass=hpcCubaUser)(uidNumber=%s)(gidNumber=%s))' % (100000 + instance.pk, settings.LDAP_SERVER_GROUPS_GROUP_GIDNUMBER,),
        search_scope=ldap3.SUBTREE,
        attributes=['uid', 'uidNumber', 'gidNumber', ]
    )
    return boolean___is_find


def ___boolean___ldap___ldapuser_instance_create___(connection, instance):
    # perform the operation create
    attributes = {
        'uid': instance.identifier,
        'uidNumber': '%s' % (100000 + instance.pk),
        'gidNumber': settings.LDAP_SERVER_GROUPS_GROUP_GIDNUMBER,
        'cn': instance.__str__(),
        'givenName': (instance.first_name if instance.first_name != '' else '-'),
        'sn': (instance.last_name if instance.last_name != '' else '-'),
        'mail': instance.email,
        'userPassword': instance.password,
        'description': instance.detail,
        'homeDirectory': '%s%s/%s' % (settings.LDAP_SERVER_USERS_HOMEDIRECTORY, settings.LDAP_SERVER_GROUPS_GROUP_CN, instance.identifier,),
        'loginShell': '/bin/bash',
        #
        'institute': instance.institute,
        'researchField': instance.researchField,
        'researchGroup': instance.researchGroup,
        'serviceType': 'serviceType',
        'userProfile': instance.userProfile,
    }
    if instance.tutorInstitution:
        attributes.update({'tutorInstitution': instance.tutorInstitution})
    if instance.tutorMail:
        attributes.update({'tutorMail': instance.tutorMail})
    if instance.tutorName:
        attributes.update({'tutorName': instance.tutorName})
    boolean___is_add = connection.add(
        dn='uid=%s,ou=%s,%s' % (instance.identifier, settings.LDAP_SERVER_GROUPS_GROUP_CN, settings.LDAP_SERVER_USERS_SEARCH_BASE,),
        object_class=['inetOrgPerson', 'posixAccount', 'top', 'hpcCubaUser'],
        attributes=attributes
    )
    # HPC
    if boolean___is_add:
        boolean___is_add = ___boolean___ldap___ldapuserhpc_instance_create___(
            connection=connection,
            string___group_cn=settings.LDAP_SERVER_GROUPS_GROUP_CN.lower(),
            int___group_gidnumber=int(settings.LDAP_SERVER_GROUPS_GROUP_GIDNUMBER),
            instance=instance
        )
    return boolean___is_add


def ___boolean___ldap___ldapuser_instance_update___(connection, instance):
    boolean___is_update = True
    # perform the operation search
    boolean___is_find = ___boolean___ldap___ldapuser_instance_search___(
        connection=connection,
        instance=instance
    )
    if boolean___is_find:
        if instance.identifier != str(connection.entries[0].uid):
            # perform the operation update dn
            boolean___is_update = connection.modify_dn(
                dn='uid=%s,ou=%s,%s' % (str(connection.entries[0].uid), settings.LDAP_SERVER_GROUPS_GROUP_CN, settings.LDAP_SERVER_USERS_SEARCH_BASE,),
                relative_dn='uid=%s' % (instance.identifier,)
            )
        if boolean___is_update:
            # perform the operation update
            changes = {
                'uidNumber': [(ldap3.MODIFY_REPLACE, [100000 + instance.pk])],
                'gidNumber': [(ldap3.MODIFY_REPLACE, [settings.LDAP_SERVER_GROUPS_GROUP_GIDNUMBER])],
                'cn': [(ldap3.MODIFY_REPLACE, [instance.__str__()])],
                'givenName': [(ldap3.MODIFY_REPLACE, [(instance.first_name if instance.first_name != '' else '-')])],
                'sn': [(ldap3.MODIFY_REPLACE, [(instance.last_name if instance.last_name != '' else '-')])],
                'mail': [(ldap3.MODIFY_REPLACE, [instance.email])],
                'userPassword': [(ldap3.MODIFY_REPLACE, [instance.password])],
                'description': [(ldap3.MODIFY_REPLACE, [instance.detail])],
                'homeDirectory': [(ldap3.MODIFY_REPLACE, ['%s%s/%s' % (settings.LDAP_SERVER_USERS_HOMEDIRECTORY, settings.LDAP_SERVER_GROUPS_GROUP_CN, instance.identifier,)])],
                'loginShell': [(ldap3.MODIFY_REPLACE, ['/bin/bash'])],
                #
                'institute': [(ldap3.MODIFY_REPLACE, [instance.institute])],
                'researchField': [(ldap3.MODIFY_REPLACE, [instance.researchField])],
                'researchGroup': [(ldap3.MODIFY_REPLACE, [instance.researchGroup])],
                'serviceType': [(ldap3.MODIFY_REPLACE, ['serviceType'])],
                'userProfile': [(ldap3.MODIFY_REPLACE, [instance.userProfile])],
            }
            if instance.tutorInstitution:
                changes.update({'tutorInstitution': [(ldap3.MODIFY_REPLACE, [instance.tutorInstitution])]})
            if instance.tutorMail:
                changes.update({'tutorMail': [(ldap3.MODIFY_REPLACE, [instance.tutorMail])]})
            if instance.tutorName:
                changes.update({'tutorName': [(ldap3.MODIFY_REPLACE, [instance.tutorName])]})
            boolean___is_update = connection.modify(
                dn='uid=%s,ou=%s,%s' % (instance.identifier, settings.LDAP_SERVER_GROUPS_GROUP_CN, settings.LDAP_SERVER_USERS_SEARCH_BASE,),
                changes=changes
            )
            # HPC
            if boolean___is_update:
                boolean___is_update = ___boolean___ldap___ldapuserhpc_instance_update___(
                    connection=connection,
                    string___group_cn=settings.LDAP_SERVER_GROUPS_GROUP_CN.lower(),
                    int___group_gidnumber=int(settings.LDAP_SERVER_GROUPS_GROUP_GIDNUMBER),
                    instance=instance
                )
    return boolean___is_update


def ___boolean___ldap___ldapuser_instance_delete___(connection, instance):
    # perform the operation delete
    boolean___is_delete = connection.delete(
        dn='uid=%s,ou=%s,%s' % (instance.identifier, settings.LDAP_SERVER_GROUPS_GROUP_CN, settings.LDAP_SERVER_USERS_SEARCH_BASE,)
    )
    # HPC
    if boolean___is_delete:
        boolean___is_delete = ___boolean___ldap___ldapuserhpc_instance_delete___(
            connection=connection,
            string___group_cn=settings.LDAP_SERVER_GROUPS_GROUP_CN.lower(),
            instance=instance
        )
    return boolean___is_delete


##########################################################################################
def ___boolean___ldap___ldapuserhpc_group_search___(connection, string___group_cn):
    # perform the operation search
    boolean___is_find = connection.search(
        search_base=settings.LDAP_SERVER_GROUPS_SEARCH_BASE,
        search_filter='(&(objectClass=posixGroup)(objectClass=hpcCubaGroup)(cn=%s))' % (string___group_cn,),
        search_scope=ldap3.SUBTREE,
        attributes=['cn', 'gidNumber', ]
    )
    return boolean___is_find


def ___boolean___ldap___ldapuserhpc_instances_search___(connection):
    # perform the operation search
    boolean___is_find = connection.search(
        search_base='%s' % (settings.LDAP_SERVER_USERS_HPC_SEARCH_BASE,),
        search_filter='(&(objectClass=inetOrgPerson)(objectClass=posixAccount)(objectClass=top)(objectClass=hpcCubaUser))',
        search_scope=ldap3.SUBTREE,
        attributes=['uid', 'uidNumber', 'gidNumber', 'givenName', 'sn', 'mail', 'userPassword', 'description', 'homeDirectory', 'institute', 'researchField', 'researchGroup', 'userProfile', 'tutorInstitution', 'tutorMail', 'tutorName', ]
    )
    return boolean___is_find


def ___boolean___ldap___ldapuserhpc_instance_search___(connection, string___group_cn, int___group_gidnumber, instance):
    # perform the operation search
    boolean___is_find = connection.search(
        search_base='%s' % (settings.LDAP_SERVER_USERS_HPC_SEARCH_BASE,),
        search_filter='(&(objectClass=inetOrgPerson)(objectClass=posixAccount)(objectClass=top)(objectClass=hpcCubaUser)(uid=%s_*)(uidNumber=%s)(gidNumber=%s))' % (string___group_cn, ((int___group_gidnumber * 100000) + instance.pk), int___group_gidnumber,),
        search_scope=ldap3.SUBTREE,
        attributes=['uid', 'uidNumber', 'gidNumber', ]
    )
    return boolean___is_find


def ___boolean___ldap___ldapuserhpc_instance_create___(connection, string___group_cn, int___group_gidnumber, instance):
    # perform the operation create
    attributes = {
        'uid': '%s_%s' % (string___group_cn, instance.identifier,),
        'uidNumber': '%s' % ((int___group_gidnumber * 100000) + instance.pk),
        'gidNumber': '%s' % (int___group_gidnumber,),
        'cn': instance.__str__(),
        'givenName': (instance.first_name if instance.first_name != '' else '-'),
        'sn': (instance.last_name if instance.last_name != '' else '-'),
        'mail': instance.email,
        'userPassword': instance.password,
        'description': instance.detail,
        'homeDirectory': '%s%s_%s' % (settings.LDAP_SERVER_USERS_HOMEDIRECTORY, string___group_cn, instance.identifier,),
        'loginShell': '/bin/bash',
        #
        'institute': instance.institute,
        'researchField': instance.researchField,
        'researchGroup': instance.researchGroup,
        'serviceType': 'serviceType',
        'userProfile': instance.userProfile,
    }
    if instance.tutorInstitution:
        attributes.update({'tutorInstitution': instance.tutorInstitution})
    if instance.tutorMail:
        attributes.update({'tutorMail': instance.tutorMail})
    if instance.tutorName:
        attributes.update({'tutorName': instance.tutorName})
    boolean___is_add = connection.add(
        dn='uid=%s,%s' % ('%s_%s' % (string___group_cn, instance.identifier,), settings.LDAP_SERVER_USERS_HPC_SEARCH_BASE,),
        object_class=['inetOrgPerson', 'posixAccount', 'top', 'hpcCubaUser'],
        attributes=attributes
    )
    return boolean___is_add


def ___boolean___ldap___ldapuserhpc_instance_update___(connection, string___group_cn, int___group_gidnumber, instance):
    boolean___is_update = True
    # perform the operation search
    boolean___is_find = ___boolean___ldap___ldapuserhpc_instance_search___(
        connection=connection,
        string___group_cn=string___group_cn,
        int___group_gidnumber=int___group_gidnumber,
        instance=instance
    )
    if boolean___is_find:
        if '%s_%s' % (string___group_cn, instance.identifier,) != str(connection.entries[0].uid):
            # perform the operation update dn
            boolean___is_update = connection.modify_dn(
                dn='uid=%s,%s' % (str(connection.entries[0].uid), settings.LDAP_SERVER_USERS_HPC_SEARCH_BASE,),
                relative_dn='uid=%s_%s' % (string___group_cn, instance.identifier,)
            )
        if boolean___is_update:
            # perform the operation update
            changes = {
                'uidNumber': [(ldap3.MODIFY_REPLACE, [(int___group_gidnumber * 100000) + instance.pk])],
                'gidNumber': [(ldap3.MODIFY_REPLACE, [int___group_gidnumber])],
                'cn': [(ldap3.MODIFY_REPLACE, [instance.__str__()])],
                'givenName': [(ldap3.MODIFY_REPLACE, [(instance.first_name if instance.first_name != '' else '-')])],
                'sn': [(ldap3.MODIFY_REPLACE, [(instance.last_name if instance.last_name != '' else '-')])],
                'mail': [(ldap3.MODIFY_REPLACE, [instance.email])],
                'userPassword': [(ldap3.MODIFY_REPLACE, [instance.password])],
                'description': [(ldap3.MODIFY_REPLACE, [instance.detail])],
                'homeDirectory': [(ldap3.MODIFY_REPLACE, ['%s%s_%s' % (settings.LDAP_SERVER_USERS_HOMEDIRECTORY, string___group_cn, instance.identifier,)])],
                'loginShell': [(ldap3.MODIFY_REPLACE, ['/bin/bash'])],
                #
                'institute': [(ldap3.MODIFY_REPLACE, [instance.institute])],
                'researchField': [(ldap3.MODIFY_REPLACE, [instance.researchField])],
                'researchGroup': [(ldap3.MODIFY_REPLACE, [instance.researchGroup])],
                'serviceType': [(ldap3.MODIFY_REPLACE, ['serviceType'])],
                'userProfile': [(ldap3.MODIFY_REPLACE, [instance.userProfile])],
            }
            if instance.tutorInstitution:
                changes.update({'tutorInstitution': [(ldap3.MODIFY_REPLACE, [instance.tutorInstitution])]})
            if instance.tutorMail:
                changes.update({'tutorMail': [(ldap3.MODIFY_REPLACE, [instance.tutorMail])]})
            if instance.tutorName:
                changes.update({'tutorName': [(ldap3.MODIFY_REPLACE, [instance.tutorName])]})
            boolean___is_update = connection.modify(
                dn='uid=%s,%s' % ('%s_%s' % (string___group_cn, instance.identifier,), settings.LDAP_SERVER_USERS_HPC_SEARCH_BASE,),
                changes=changes
            )
    return boolean___is_update


def ___boolean___ldap___ldapuserhpc_instance_delete___(connection, string___group_cn, instance):
    # perform the operation delete
    boolean___is_delete = connection.delete(
        dn='uid=%s,%s' % ('%s_%s' % (string___group_cn, instance.identifier,), settings.LDAP_SERVER_USERS_HPC_SEARCH_BASE,)
    )
    return boolean___is_delete


##########################################################################################
def ___void___ldap___ldapuser_instances_synchronize___(connection):
    # synchronize ldapuser instances
    instances = models.LDAPUser.objects.all()
    for instance in instances:
        # perform the operation search
        boolean___is_find = ___boolean___ldap___ldapuser_instance_search___(
            connection=connection,
            instance=instance
        )
        if boolean___is_find:
            # perform the operation update
            ___boolean___ldap___ldapuser_instance_update___(
                connection=connection,
                instance=instance
            )
        else:
            # perform the operation create
            ___boolean___ldap___ldapuser_instance_create___(
                connection=connection,
                instance=instance
            )
    # perform the operation search
    boolean___is_find = ___boolean___ldap___ldapuser_instances_search___(
        connection=connection,
        string___gidnumber=settings.LDAP_SERVER_GROUPS_GROUP_GIDNUMBER
    )
    if boolean___is_find:
        list_entry___to_delete = list()
        for entry in connection.entries:
            string___uid = str(entry.uid)
            string___uidnumber = str(entry.uidNumber)
            string___homedirectory = str(entry.homeDirectory)
            boolean___delete = True
            for instance in instances:
                uid = instance.identifier
                uidnumber = '%s' % (100000 + instance.pk)
                homedirectory = '%s%s/%s' % (settings.LDAP_SERVER_USERS_HOMEDIRECTORY, settings.LDAP_SERVER_GROUPS_GROUP_CN, instance.identifier,)
                if uid == string___uid and uidnumber == string___uidnumber and homedirectory == string___homedirectory:
                    boolean___delete = False
                    break
            if boolean___delete is True:
                list_entry___to_delete.append(entry)
        for entry in list_entry___to_delete:
            # perform the operation update
            connection.delete(
                dn='uid=%s,ou=%s,%s' % (str(entry.uid), settings.LDAP_SERVER_GROUPS_GROUP_CN, settings.LDAP_SERVER_USERS_SEARCH_BASE,)
            )
            connection.delete(
                dn='uid=%s,%s' % ('%s_%s' % (settings.LDAP_SERVER_GROUPS_GROUP_CN.lower(), str(entry.uid),), settings.LDAP_SERVER_USERS_HPC_SEARCH_BASE,)
            )


def ___void___ldap___ldapuserimported_instances_synchronize___(connection):
    # get groups
    boolean___is_find = ___boolean___ldap___ldapuser_group_instances_search___(connection=connection)
    if boolean___is_find:
        # get imported user groups.
        list_entry___group = list()
        for entry in connection.entries:
            string___cn = str(entry.cn)
            string___gidnumber = str(entry.gidNumber)
            if string___gidnumber == settings.LDAP_SERVER_GROUPS_GROUP_GIDNUMBER:
                continue
            dict_instance___entry = {
                'cn': string___cn,
                'gidNumber': string___gidnumber,
            }
            list_entry___group.append(dict_instance___entry)
        # delete instances
        instances = models.LDAPUserImported.objects.all()
        list_instance___to_delete = list()
        for instance in instances:
            boolean___delete = True
            for entry___group in list_entry___group:
                # perform the operation search
                boolean___is_find = ___boolean___ldap___ldapuser_instances_search___(
                    connection=connection,
                    string___gidnumber=entry___group['gidNumber']
                )
                if boolean___is_find:
                    for entry___user in connection.entries:
                        string___uid = str(entry___user.uid)
                        if instance.identifier == string___uid and instance.ldap_group == entry___group['cn']:
                            boolean___delete = False
                            break
                    if boolean___delete is False:
                        break
            if boolean___delete is True:
                list_instance___to_delete.append(instance)
        for instance in list_instance___to_delete:
            # avatar
            if instance.avatar is not None and instance.avatar != '':
                if os.path.exists(instance.___string___folder_path___()):
                    shutil.rmtree(instance.___string___folder_path___())
            instance.delete()
        # synchronize
        for entry___group in list_entry___group:
            # perform the operation search
            boolean___is_find = ___boolean___ldap___ldapuser_instances_search___(
                connection=connection,
                string___gidnumber=entry___group['gidNumber']
            )
            if boolean___is_find:
                for entry in connection.entries:
                    string___uid = str(entry.uid)
                    string___givenname = (str(entry.givenName) if str(entry.givenName) != '[]' else '')
                    string___sn = (str(entry.sn) if str(entry.sn) != '[]' else '')
                    string___mail = str(entry.mail)
                    string___userpassword = str(entry.userPassword)[2:-1]
                    string___description = str(entry.description)
                    string___institute = str(entry.institute)
                    string___researchField = str(entry.researchField)
                    string___researchGroup = str(entry.researchGroup)
                    string___userProfile = str(entry.userProfile)
                    string___tutorInstitution = str(entry.tutorInstitution)
                    string___tutorMail = str(entry.tutorMail)
                    string___tutorName = str(entry.tutorName)
                    instance = models.LDAPUserImported.objects.___instance___by_ldap_group_and_identifier___(ldap_group=entry___group['cn'], identifier=string___uid)
                    if instance is not None:
                        instance.first_name = string___givenname
                        instance.last_name = string___sn
                        instance.email = string___mail
                        instance.password = string___userpassword
                        instance.detail = string___description
                        instance.institute = string___institute
                        instance.researchField = string___researchField
                        instance.researchGroup = string___researchGroup
                        instance.userProfile = string___userProfile
                        instance.tutorInstitution = string___tutorInstitution
                        instance.tutorMail = string___tutorMail
                        instance.tutorName = string___tutorName
                        instance.save()
                    else:
                        instance = models.LDAPUserImported(
                            is_active=True,
                            ldap_group=entry___group['cn'],
                            identifier=string___uid,
                            email=string___mail,
                            first_name=string___givenname,
                            last_name=string___sn,
                            password=string___userpassword,
                            detail=string___description,
                            institute=string___institute,
                            researchField=string___researchField,
                            researchGroup=string___researchGroup,
                            userProfile=string___userProfile,
                            tutorInstitution=string___tutorInstitution,
                            tutorMail=string___tutorMail,
                            tutorName = string___tutorName
                        )
                        instance.save()


def ___void___ldap___ldapuserhpc_instances_synchronize___(connection):
    # synchronize ldapuser instances
    instances = models.LDAPUser.objects.all()
    for instance in instances:
        # perform the operation search
        boolean___is_find = ___boolean___ldap___ldapuserhpc_instance_search___(
            connection=connection,
            string___group_cn=settings.LDAP_SERVER_GROUPS_GROUP_CN.lower(),
            int___group_gidnumber=int(settings.LDAP_SERVER_GROUPS_GROUP_GIDNUMBER),
            instance=instance
        )
        if boolean___is_find:
            # perform the operation update
            ___boolean___ldap___ldapuserhpc_instance_update___(
                connection=connection,
                string___group_cn=settings.LDAP_SERVER_GROUPS_GROUP_CN.lower(),
                int___group_gidnumber=int(settings.LDAP_SERVER_GROUPS_GROUP_GIDNUMBER),
                instance=instance
            )
        else:
            # perform the operation create
            ___boolean___ldap___ldapuserhpc_instance_create___(
                connection=connection,
                string___group_cn=settings.LDAP_SERVER_GROUPS_GROUP_CN.lower(),
                int___group_gidnumber=int(settings.LDAP_SERVER_GROUPS_GROUP_GIDNUMBER),
                instance=instance
            )
    instances = models.LDAPUserImported.objects.all()
    for instance in instances:
        # perform the operation search
        boolean___is_find = ___boolean___ldap___ldapuserhpc_group_search___(
            connection=connection,
            string___group_cn=instance.ldap_group
        )
        if boolean___is_find:
            string___group_cn = str(connection.entries[0].cn)
            int___group_gidnumber = int(str(connection.entries[0].gidNumber))
            #
            boolean___is_find = ___boolean___ldap___ldapuserhpc_instance_search___(
                connection=connection,
                string___group_cn=string___group_cn.lower(),
                int___group_gidnumber=int___group_gidnumber,
                instance=instance
            )
            if boolean___is_find:
                # perform the operation update
                ___boolean___ldap___ldapuserhpc_instance_update___(
                    connection=connection,
                    string___group_cn=string___group_cn.lower(),
                    int___group_gidnumber=int___group_gidnumber,
                    instance=instance
                )
            else:
                # perform the operation create
                ___boolean___ldap___ldapuserhpc_instance_create___(
                    connection=connection,
                    string___group_cn=string___group_cn.lower(),
                    int___group_gidnumber=int___group_gidnumber,
                    instance=instance
                )
    # perform the operation search
    boolean___is_find = ___boolean___ldap___ldapuserhpc_instances_search___(
        connection=connection,
    )
    if boolean___is_find:
        list_entry___to_delete = list()
        for entry in connection.entries:
            string___uid = str(entry.uid)
            string___uidnumber = str(entry.uidNumber)
            string___homedirectory = str(entry.homeDirectory)
            boolean___delete = True
            instances = models.LDAPUser.objects.all()
            for instance in instances:
                uid = '%s_%s' % (settings.LDAP_SERVER_GROUPS_GROUP_CN.lower(), instance.identifier,)
                uidnumber = '%s' % ((int(settings.LDAP_SERVER_GROUPS_GROUP_GIDNUMBER) * 100000) + instance.pk)
                homedirectory = '%s%s_%s' % (settings.LDAP_SERVER_USERS_HOMEDIRECTORY, settings.LDAP_SERVER_GROUPS_GROUP_CN.lower(), instance.identifier,)
                if uid == string___uid and uidnumber == string___uidnumber and homedirectory == string___homedirectory:
                    boolean___delete = False
                    break
            if boolean___delete is True:
                instances = models.LDAPUserImported.objects.all()
                for instance in instances:
                    boolean___is_find = ___boolean___ldap___ldapuserhpc_group_search___(
                        connection=connection,
                        string___group_cn=instance.ldap_group
                    )
                    if boolean___is_find is True:
                        uid = '%s_%s' % (str(connection.entries[0].cn).lower(), instance.identifier,)
                        uidnumber = '%s' % ((int(str(connection.entries[0].gidNumber)) * 100000) + instance.pk)
                        homedirectory = '%s%s_%s' % (settings.LDAP_SERVER_USERS_HOMEDIRECTORY, str(connection.entries[0].cn).lower(), instance.identifier,)
                        if uid == string___uid and uidnumber == string___uidnumber and homedirectory == string___homedirectory:
                            boolean___delete = False
                            break
            if boolean___delete is True:
                list_entry___to_delete.append(entry)
        for entry in list_entry___to_delete:
            # perform the operation update
            connection.delete(
                dn='uid=%s,%s' % (str(entry.uid), settings.LDAP_SERVER_USERS_HPC_SEARCH_BASE,)
            )


##########################################################################################
def ___messages___action___is_there_connection___(request):
    boolean___is_there_connection = False
    connection = ___connection___ldap___()
    try:
        # start the connection
        if connection.bind():
            boolean___is_there_connection = True
    except (Exception,):
        pass
    finally:
        # close the connection
        connection.unbind()
    if boolean___is_there_connection is False:
        messages.add_message(request, messages.WARNING, _('APPLICATION___SECURITY___MESSAGE Connection to the LDAP could not be established. When the connection will be place, the action will be perform in the LDAP.'))


def ___void___action___ldapuser_instance_create___(instance):
    connection = ___connection___ldap___()
    try:
        # start the connection
        if connection.bind():
            # perform the operation search
            boolean___is_find = ___boolean___ldap___ldapuser_instance_search___(
                connection=connection,
                instance=instance
            )
            if boolean___is_find:
                # perform the operation delete
                ___boolean___ldap___ldapuser_instance_delete___(
                    connection=connection,
                    instance=instance
                )
            # perform the operation create
            ___boolean___ldap___ldapuser_instance_create___(
                connection=connection,
                instance=instance
            )
    except (Exception,):
        pass
    finally:
        # close the connection
        connection.unbind()


def ___void___action___ldapuser_instance_update___(instance):
    connection = ___connection___ldap___()
    try:
        # start the connection
        if connection.bind():
            # perform the operation search
            boolean___is_find = ___boolean___ldap___ldapuser_instance_search___(
                connection=connection,
                instance=instance
            )
            if boolean___is_find:
                # perform the operation update
                ___boolean___ldap___ldapuser_instance_update___(
                    connection=connection,
                    instance=instance
                )
            else:
                # perform the operation create
                ___boolean___ldap___ldapuser_instance_create___(
                    connection=connection,
                    instance=instance
                )
    except (Exception,):
        pass
    finally:
        # close the connection
        connection.unbind()


def ___void___action___ldapuser_instance_delete___(instance):
    connection = ___connection___ldap___()
    try:
        # start the connection
        if connection.bind():
            # perform the operation delete
            ___boolean___ldap___ldapuser_instance_delete___(
                connection=connection,
                instance=instance
            )
    except (Exception,):
        pass
    finally:
        # close the connection
        connection.unbind()


def ___void___action___user_instances_synchronize___():
    connection = ___connection___ldap___()
    try:
        # start the connection
        if connection.bind():
            ___void___ldap___ldapuser_instances_synchronize___(connection=connection)
            ___void___ldap___ldapuserimported_instances_synchronize___(connection=connection)
            ___void___ldap___ldapuserhpc_instances_synchronize___(connection=connection)
    except (Exception,):
        pass
    finally:
        # close the connection
        connection.unbind()


def synchronize():
    from src.application.security.models import LDAPUser
    import logging
    logging.basicConfig(filename='/service_django/error.log', level=logging.DEBUG)
    from ldap3.utils.log import set_library_log_detail_level, set_library_log_hide_sensitive_data, EXTENDED

    set_library_log_detail_level(EXTENDED)
    set_library_log_hide_sensitive_data(False)
    server = ldap3.Server(
        host=settings.LDAP_SERVER_HOST,
        port=settings.LDAP_SERVER_PORT,
        use_ssl=False,
        get_info=ldap3.ALL
    )
    # define the connection
    connection = ldap3.Connection(
        server=server,
        user=settings.LDAP_SERVER_USER,
        password=settings.LDAP_SERVER_PASSWORD,
        auto_bind='NONE',
        version=3,
        authentication='SIMPLE',
        client_strategy='SYNC',
        auto_referrals=True,
        check_names=True,
        read_only=False,
        lazy=False,
        raise_exceptions=False
    )
    instance = LDAPUser.objects.get(pk=11)
    if connection.bind():
        attributes = {
            'uid': instance.identifier,
            'uidNumber': '%s' % (100000 + instance.pk),
            'gidNumber': settings.LDAP_SERVER_GROUPS_GROUP_GIDNUMBER,
            'cn': instance.__str__(),
            'givenName': (instance.first_name if instance.first_name != '' else '-'),
            'sn': (instance.last_name if instance.last_name != '' else '-'),
            'mail': instance.email,
            'userPassword': instance.password,
            'description': instance.detail,
            'homeDirectory': '%s%s/%s' % (settings.LDAP_SERVER_USERS_HOMEDIRECTORY, settings.LDAP_SERVER_GROUPS_GROUP_CN, instance.identifier,),
            'loginShell': '/bin/bash',
            #
            'institute': instance.institute,
            'researchField': instance.researchField,
            'researchGroup': instance.researchGroup,
            'serviceType': 'serviceType',
            'userProfile': instance.userProfile,
        }
        if instance.tutorInstitution:
            attributes.update({'tutorInstitution': instance.tutorInstitution})
        if instance.tutorMail:
            attributes.update({'tutorMail': instance.tutorMail})
        if instance.tutorName:
            attributes.update({'tutorName': instance.tutorName})
        boolean___is_add = connection.add(
            dn='uid=%s,ou=%s,%s' % (instance.identifier, settings.LDAP_SERVER_GROUPS_GROUP_CN, settings.LDAP_SERVER_USERS_SEARCH_BASE,),
            object_class=['inetOrgPerson', 'posixAccount', 'top', 'hpcCubaUser'],
            attributes=attributes
        )
        print(attributes)
        print(boolean___is_add)
    else:
        print("not bind")
    connection.unbind()
