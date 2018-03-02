# -*- coding: utf-8 -*-
from . import forms
from src.application.security import ldap, models
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _

# The model to administrate
___MODEL___ = models.LDAPUserRequest
# The model path to administrate
___MODEL_PATH___ = 'ldapuserrequest'
# The forms of the model to administrate
___FORM___DETAIL___ = forms.LDAPUserRequestDetail
___FORM___APPROVE___ = forms.LDAPUserRequestApprove
___FORM___DISAPPROVE___ = forms.LDAPUserRequestDisapprove
#
# Pagination
___INT___PAGINATOR_AMOUNT_PER_PAGE___ = 10


def ___boolean___approve___initial___(request, dict___data):
    # LDAP
    ldap.___messages___action___is_there_connection___(request=request)
    return True
