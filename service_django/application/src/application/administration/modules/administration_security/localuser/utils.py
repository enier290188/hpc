# -*- coding: utf-8 -*-
from . import forms
from src.application.security import models

# The model to administrate
___MODEL___ = models.LOCALUser
# The model path to administrate
___MODEL_PATH___ = 'localuser'
# The forms of the model to administrate
___FORM___CREATE___ = forms.LOCALUserCreate
___FORM___DETAIL___ = forms.LOCALUserDetail
___FORM___UPDATE___ = forms.LOCALUserUpdate
___FORM___DELETE___ = forms.LOCALUserDelete
#
# Pagination
___INT___PAGINATOR_AMOUNT_PER_PAGE___ = 10
