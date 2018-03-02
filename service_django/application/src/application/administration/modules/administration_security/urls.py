# -*- coding: utf-8 -*-
from django.conf.urls import include, url

urlpatterns = [
    url(r'^localuser/', include('src.application.administration.modules.administration_security.localuser.urls', namespace='localuser')),
    url(r'^localuserrequest/', include('src.application.administration.modules.administration_security.localuserrequest.urls', namespace='localuserrequest')),
    url(r'^ldapuser/', include('src.application.administration.modules.administration_security.ldapuser.urls', namespace='ldapuser')),
    url(r'^ldapuserrequest/', include('src.application.administration.modules.administration_security.ldapuserrequest.urls', namespace='ldapuserrequest')),
    url(r'^ldapuserimported/', include('src.application.administration.modules.administration_security.ldapuserimported.urls', namespace='ldapuserimported')),
    url(r'^group/', include('src.application.administration.modules.administration_security.group.urls', namespace='group')),
    url(r'^permission/', include('src.application.administration.modules.administration_security.permission.urls', namespace='permission')),
]
