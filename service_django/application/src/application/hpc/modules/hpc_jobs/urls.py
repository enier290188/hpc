# -*- coding: utf-8 -*-
from . import views
from django.conf.urls import url

urlpatterns = [
    url(regex=r'^$', view=views.___view___index___, name='index'),
    url(regex=r'^api/$', view=views.___view___api___, name='api'),
]
