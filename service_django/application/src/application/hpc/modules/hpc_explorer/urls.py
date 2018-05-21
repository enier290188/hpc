# -*- coding: utf-8 -*-
from . import views
from django.conf.urls import url

urlpatterns = [
    url(regex=r'^$', view=views.___view___index___, name='index'),
    url(regex=r'^list/$', view=views.___view___list___, name='list'),
    url(regex=r'^modal/$', view=views.___view___modal___, name='modal'),
    url(regex=r'^upload/$', view=views.___view___upload___, name='upload'),
    url(regex=r'^download/$', view=views.___view___download___, name='download'),
    url(regex=r'^edit/$', view=views.___view___edit___, name='edit'),
    url(regex=r'^delete/$', view=views.___view___delete___, name='delete'),
    url(regex=r'^execute/$', view=views.___view___execute___, name='execute'),
]
