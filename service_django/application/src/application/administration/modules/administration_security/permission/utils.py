# -*- coding: utf-8 -*-
from . import forms
from src.application.security import models

# The model to administrate
___MODEL___ = models.Permission
# The model path to administrate
___MODEL_PATH___ = 'permission'
# The forms of the model to administrate
___FORM___DETAIL___ = forms.PermissionDetail
___FORM___UPDATE___ = forms.PermissionUpdate
#
# Pagination
___INT___PAGINATOR_AMOUNT_PER_PAGE___ = 1000000
