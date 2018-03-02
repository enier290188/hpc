# -*- coding: utf-8 -*-
from . import forms
from src.application.security import models

# The model to administrate
___MODEL___ = models.Group
# The model path to administrate
___MODEL_PATH___ = 'group'
# The forms of the model to administrate
___FORM___CREATE___ = forms.GroupCreate
___FORM___DETAIL___ = forms.GroupDetail
___FORM___UPDATE___ = forms.GroupUpdate
___FORM___DELETE___ = forms.GroupDelete
#
# Pagination
___INT___PAGINATOR_AMOUNT_PER_PAGE___ = 1000000


def ___void___list___tree___(request, dict___data, instance):
    # get parents of instance
    list_int___group_parent = []
    temporal_int___group_parent = instance.parent
    if temporal_int___group_parent != 0:
        while temporal_int___group_parent != 0:
            list_int___group_parent.append(temporal_int___group_parent)
            temporal_instance___group_parent = models.Group.objects.___instance___by_pk___(pk=temporal_int___group_parent)
            temporal_int___group_parent = temporal_instance___group_parent.parent
        #
        instances___localusergroup = models.LOCALUserGroup.objects.filter(group=instance.pk)
        for instance___localusergroup in instances___localusergroup:
            # parents que tiene ahora que no tiene incluidos
            list_int___group_parent_selected = [x.pk for x in instance___localusergroup.localuser.groups.all()]
            list_int___group_parent_to_add = [x for x in list_int___group_parent if x not in list_int___group_parent_selected]
            for int___group_parent_to_add in list_int___group_parent_to_add:
                temporal_instance___group_parent_to_add = models.Group.objects.___instance___by_pk___(pk=int___group_parent_to_add)
                temporal_instance___localusergroup_to_save = models.LOCALUserGroup(localuser=instance___localusergroup.localuser, group=temporal_instance___group_parent_to_add)
                temporal_instance___localusergroup_to_save.save()
        #
        instances___ldapusergroup = models.LDAPUserGroup.objects.filter(group=instance.pk)
        for instance___ldapusergroup in instances___ldapusergroup:
            # parents que tiene ahora que no tiene incluidos
            list_int___group_parent_selected = [x.pk for x in instance___ldapusergroup.ldapuser.groups.all()]
            list_int___group_parent_to_add = [x for x in list_int___group_parent if x not in list_int___group_parent_selected]
            for int___group_parent_to_add in list_int___group_parent_to_add:
                temporal_instance___group_parent_to_add = models.Group.objects.___instance___by_pk___(pk=int___group_parent_to_add)
                temporal_instance___ldapusergroup_to_save = models.LDAPUserGroup(ldapuser=instance___ldapusergroup.ldapuser, group=temporal_instance___group_parent_to_add)
                temporal_instance___ldapusergroup_to_save.save()
