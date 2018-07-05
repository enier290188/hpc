# -*- coding: utf-8 -*-
from . import views
from django.conf.urls import url

urlpatterns = [
    url(regex=r'^$', view=views.___view___index___, name='index'),
    url(regex=r'^list/$', view=views.___view___list___, name='list'),

    # url(regex=r'^create-folder/$', view=views.___view___create_folder___, name='create-folder'),
    # url(regex=r'^create-file/$', view=views.___view___create_file___, name='create-file'),
    # url(regex=r'^rename/$', view=views.___view___rename___, name='rename'),
    # url(regex=r'^go-to/$', view=views.___view___go_to___, name='go-to'),

    url(regex=r'^modal/$', view=views.___view___modal___, name='modal'),
    url(regex=r'^upload/$', view=views.___view___upload___, name='upload'),
    url(regex=r'^download/$', view=views.___view___download___, name='download'),
    url(regex=r'^edit/$', view=views.___view___edit___, name='edit'),
    url(regex=r'^delete/$', view=views.___view___delete___, name='delete'),
    url(regex=r'^execute/$', view=views.___view___execute___, name='execute'),
]
