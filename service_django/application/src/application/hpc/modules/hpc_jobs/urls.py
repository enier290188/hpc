# -*- coding: utf-8 -*-
from . import views
from django.conf.urls import url

urlpatterns = [
    url(regex=r'^$', view=views.___view___index___, name='index'),
    url(regex=r'^list/$', view=views.___view___list___, name='list'),
    url(regex=r'^detail/$', view=views.___view___detail___, name='detail'),
    url(regex=r'^stop/$', view=views.___view___stop___, name='stop'),
    url(regex=r'^continue/$', view=views.___view___continue___, name='continue'),
    url(regex=r'^requeue/$', view=views.___view___requeue___, name='requeue'),
    url(regex=r'^kill/$', view=views.___view___kill___, name='kill'),
]
