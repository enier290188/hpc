# -*- coding: utf-8 -*-
from django.conf.urls import include, url

urlpatterns = [
    url(r'^hpc_module01/', include('src.application.hpc.modules.hpc_module01.urls', namespace='hpc_module01')),
    url(r'^hpc_module02/', include('src.application.hpc.modules.hpc_module02.urls', namespace='hpc_module02')),
    url(r'^hpc_module03/', include('src.application.hpc.modules.hpc_module03.urls', namespace='hpc_module03')),
]
