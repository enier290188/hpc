# -*- coding: utf-8 -*-
from django.conf.urls import include, url

urlpatterns = [
    url(r'^hpc_jobs/', include('src.application.hpc.modules.hpc_jobs.urls', namespace='hpc_jobs')),
    url(r'^hpc_script/', include('src.application.hpc.modules.hpc_script.urls', namespace='hpc_script')),
    url(r'^hpc_nodes/', include('src.application.hpc.modules.hpc_nodes.urls', namespace='hpc_nodes')),
    url(r'^hpc_explorer/', include('src.application.hpc.modules.hpc_explorer.urls', namespace='hpc_explorer')),
]
