# -*- coding: utf-8 -*-
from django.conf.urls import include, url

urlpatterns = [
    url(r'^bigdata_module01/', include('src.application.bigdata.modules.bigdata_module01.urls', namespace='bigdata_module01')),
    url(r'^bigdata_module02/', include('src.application.bigdata.modules.bigdata_module02.urls', namespace='bigdata_module02')),
    url(r'^bigdata_module03/', include('src.application.bigdata.modules.bigdata_module03.urls', namespace='bigdata_module03')),
]
