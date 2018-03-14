# -*- coding: utf-8 -*-
from django.conf.urls import include, url

urlpatterns = [
    url(r'^hpc_jobs/', include('src.application.hpc.modules.hpc_jobs.urls', namespace='hpc_jobs')),
]
