# -*- coding: utf-8 -*-
from django import shortcuts
from django.core import urlresolvers


def ___view___index___(request):
    return shortcuts.redirect(urlresolvers.reverse('application___website:index'))
