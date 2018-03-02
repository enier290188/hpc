# -*- coding: utf-8 -*-
from . import forms
from src.application.help import models

# The model to administrate
___MODEL___ = models.Document
# The model path to administrate
___MODEL_PATH___ = 'document'
# The forms of the model to administrate
___FORM___CREATE___ = forms.DocumentCreate
___FORM___DETAIL___ = forms.DocumentDetail
___FORM___UPDATE___ = forms.DocumentUpdate
___FORM___DELETE___ = forms.DocumentDelete
#
# Pagination
___INT___PAGINATOR_AMOUNT_PER_PAGE___ = 1000000
