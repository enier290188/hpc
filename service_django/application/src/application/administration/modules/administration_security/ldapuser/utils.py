# -*- coding: utf-8 -*-
from . import forms
from src.application.security import ldap, models
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _

# The model to administrate
___MODEL___ = models.LDAPUser
# The model path to administrate
___MODEL_PATH___ = 'ldapuser'
# The forms of the model to administrate
___FORM___CREATE___ = forms.LDAPUserCreate
___FORM___DETAIL___ = forms.LDAPUserDetail
___FORM___UPDATE___ = forms.LDAPUserUpdate
___FORM___DELETE___ = forms.LDAPUserDelete
#
# Pagination
___INT___PAGINATOR_AMOUNT_PER_PAGE___ = 10


def ___boolean___create___initial___(request, dict___data):
    # LDAP
    ldap.___messages___action___is_there_connection___(request=request)
    return True


def ___boolean___detail___initial___(request, dict___data):
    # LDAP
    ldap.___messages___action___is_there_connection___(request=request)
    return True


def ___boolean___update___initial___(request, dict___data):
    # LDAP
    ldap.___messages___action___is_there_connection___(request=request)
    return True


def ___boolean___delete___initial___(request, dict___data):
    # LDAP
    ldap.___messages___action___is_there_connection___(request=request)
    return True
