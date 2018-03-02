# -*- coding: utf-8 -*-
from . import forms
from src.application.security import models

# The model to administrate
___MODEL___ = models.LOCALUserRequest
# The model path to administrate
___MODEL_PATH___ = 'localuserrequest'
# The forms of the model to administrate
___FORM___DETAIL___ = forms.LOCALUserRequestDetail
___FORM___APPROVE___ = forms.LOCALUserRequestApprove
___FORM___DISAPPROVE___ = forms.LOCALUserRequestDisapprove
#
# Pagination
___INT___PAGINATOR_AMOUNT_PER_PAGE___ = 10
