# -*- coding: utf-8 -*-
from . import forms
from src.application.security import models

# The model to administrate
___MODEL___ = models.LDAPUserImported
# The model path to administrate
___MODEL_PATH___ = 'ldapuserimported'
# The forms of the model to administrate
___FORM___DETAIL___ = forms.LDAPUserImportedDetail
___FORM___UPDATE___ = forms.LDAPUserImportedUpdate
___FORM___DELETE___ = forms.LDAPUserImportedDelete
#
# Pagination
___INT___PAGINATOR_AMOUNT_PER_PAGE___ = 10
