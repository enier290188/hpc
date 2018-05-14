# -*- coding: utf-8 -*-
from . import views
from .modules.hpc_explorer import views as v
from django.conf.urls import include, url

urlpatterns = [
    url(regex=r'^$', view=views.___view___index___, name='index'),
    url(regex=r'^index___load/$', view=views.___view___index___load___, name='index___load'),
    url(regex=r'^index___title/$', view=views.___view___index___title___, name='index___title'),
    url(regex=r'^index___header/$', view=views.___view___index___header___, name='index___header'),
    url(regex=r'^index___leftside/$', view=views.___view___index___leftside___, name='index___leftside'),
    url(regex=r'^index___content___center/$', view=views.___view___index___content___center___, name='index___content___center'),
    url(regex=r'^index___content___footer/$', view=views.___view___index___content___footer___, name='index___content___footer'),
    url(regex=r'^download/$', view=v.___view___download___, name='download'),
    #
    url(regex=r'^login/$', view=views.___view___login___, name='login'),
    url(regex=r'^login___forgot_credentials_1/$', view=views.___view___login___forgot_credentials_1___, name='login___forgot_credentials_1'),
    url(regex=r'^login___forgot_credentials_2/(?P<pk>\d+)/$', view=views.___view___login___forgot_credentials_2___, name='login___forgot_credentials_2'),
    url(regex=r'^login___forgot_credentials_3/(?P<pk>\d+)/$', view=views.___view___login___forgot_credentials_3___, name='login___forgot_credentials_3'),
    url(regex=r'^login___request/$', view=views.___view___login___request___, name='login___request'),
    url(regex=r'^logout/$', view=views.___view___logout___, name='logout'),
    url(regex=r'^profile/$', view=views.___view___profile___, name='profile'),
    url(regex=r'^locale/$', view=views.___view___locale___, name='locale'),
    #
    url(r'^modules/', include('src.application.hpc.modules.urls', namespace='modules')),
]