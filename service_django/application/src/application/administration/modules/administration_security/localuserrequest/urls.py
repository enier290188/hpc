# -*- coding: utf-8 -*-
from . import views
from django.conf.urls import url

urlpatterns = [
    url(regex=r'^$', view=views.___view___index___, name='index'),
    url(regex=r'^list/$', view=views.___view___list___, name='list'),
    url(regex=r'^detail/(?P<pk>\d+)/$', view=views.___view___detail___, name='detail'),
    url(regex=r'^approve/(?P<pk>\d+)/$', view=views.___view___approve___, name='approve'),
    url(regex=r'^disapprove/(?P<pk>\d+)/$', view=views.___view___disapprove___, name='disapprove'),
]
