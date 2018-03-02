# -*- coding: utf-8 -*-
from django.conf.urls import include, url

urlpatterns = [
    url(r'^administration_security/', include('src.application.administration.modules.administration_security.urls', namespace='administration_security')),
    url(r'^administration_help/', include('src.application.administration.modules.administration_help.urls', namespace='administration_help')),
]
