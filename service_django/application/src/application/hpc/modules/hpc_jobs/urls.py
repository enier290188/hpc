# -*- coding: utf-8 -*-
from . import views
from django.conf.urls import url

urlpatterns = [
    url(regex=r'^$', view=views.___view___index___, name='index'),
    url(regex=r'^list/$', view=views.___view___list___, name='list'),
    url(regex=r'^detail/$', view=views.___view___detail___, name='detail'),
    url(regex=r'^action/$', view=views.___view___action___, name='action'),
]
