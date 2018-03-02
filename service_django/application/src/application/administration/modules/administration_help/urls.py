# -*- coding: utf-8 -*-
from django.conf.urls import include, url

urlpatterns = [
    url(r'^document/', include('src.application.administration.modules.administration_help.document.urls', namespace='document')),
]
