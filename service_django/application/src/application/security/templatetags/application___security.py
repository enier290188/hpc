# -*- coding: utf-8 -*-
from src.application.security import models
from django import template
from django.conf import settings
from django.contrib.staticfiles.templatetags import staticfiles
from django.utils import timezone

register = template.Library()


@register.filter()
def ___get_string___title___(request):
    return '-%s' % (settings.LDAP_SERVER_GROUPS_GROUP_CN,)


@register.filter()
def ___get_boolean___not___(boolean):
    return not boolean


@register.filter()
def ___required___application___security___user___(request):
    if request.___APPLICATION___SECURITY___USER___ is not None:
        return True
    return False


@register.filter()
def ___required___application___security___user___has_permission___(request, string___identifiers_to_verify):
    if ___required___application___security___user___(request=request):
        set_identifier___to_verify = set(' '.join(string___identifiers_to_verify.split()).split())  # delete space
        if request.___APPLICATION___SECURITY___USER___.is_superuser is True or request.___APPLICATION___SECURITY___USER___.___boolean___has_permission___(set_identifier___to_verify=set_identifier___to_verify):
            return True
    return False


@register.filter()
def ___required___application___security___user___is_localuser___(request):
    if ___required___application___security___user___(request=request):
        if isinstance(request.___APPLICATION___SECURITY___USER___, models.LOCALUser):
            return True
    return False


@register.filter()
def ___required___application___security___user___is_ldapuser___(request):
    if ___required___application___security___user___(request=request):
        if isinstance(request.___APPLICATION___SECURITY___USER___, models.LDAPUser) or isinstance(request.___APPLICATION___SECURITY___USER___, models.LDAPUserImported):
            return True
    return False


@register.filter()
def ___get_instance___application___security___user___(request):
    return request.___APPLICATION___SECURITY___USER___


@register.filter()
def ___get_string___application___security___user___url_current___(request):
    return request.session['___APPLICATION___SECURITY___USER___URL_CURRENT___']


@register.filter()
def ___get_string___application___security___user___avatar_url___(request):
    string___avatar_url = staticfiles.static('application/security/img/avatar/avatar.png')
    if request.___APPLICATION___SECURITY___USER___ is not None and request.___APPLICATION___SECURITY___USER___.avatar:
        string___avatar_url = request.___APPLICATION___SECURITY___USER___.avatar.url
    return '%s?%s' % (string___avatar_url, timezone.datetime.now().strftime("%Y%m%d%H%M%S"))


@register.filter()
def ___get_string___user___avatar_url___(instance):
    string___avatar_url = staticfiles.static('application/security/img/avatar/avatar.png')
    if instance is not None and instance.avatar:
        string___avatar_url = instance.avatar.url
    return '%s?%s' % (string___avatar_url, timezone.datetime.now().strftime("%Y%m%d%H%M%S"))


@register.filter()
def ___get_string___user___th___width___(request, string___identifiers_to_verify):
    if request.___APPLICATION___SECURITY___USER___ is not None:
        list_identifier___to_verify = list(' '.join(string___identifiers_to_verify.split()).split())  # delete space
        if list_identifier___to_verify[0] != 'none':
            boolean___has_permission_0 = request.___APPLICATION___SECURITY___USER___.___boolean___has_permission___(set_identifier___to_verify={list_identifier___to_verify[0], })
        else:
            boolean___has_permission_0 = False
        if list_identifier___to_verify[1] != 'none':
            boolean___has_permission_1 = request.___APPLICATION___SECURITY___USER___.___boolean___has_permission___(set_identifier___to_verify={list_identifier___to_verify[1], })
        else:
            boolean___has_permission_1 = False
        if list_identifier___to_verify[2] != 'none':
            boolean___has_permission_2 = request.___APPLICATION___SECURITY___USER___.___boolean___has_permission___(set_identifier___to_verify={list_identifier___to_verify[2], })
        else:
            boolean___has_permission_2 = False
        if list_identifier___to_verify[3] != 'none':
            boolean___has_permission_3 = request.___APPLICATION___SECURITY___USER___.___boolean___has_permission___(set_identifier___to_verify={list_identifier___to_verify[3], })
        else:
            boolean___has_permission_3 = False
        #
        if boolean___has_permission_1 and boolean___has_permission_2 and boolean___has_permission_3:
            return 'th___width_3'
        if (boolean___has_permission_1 and boolean___has_permission_2) or (boolean___has_permission_1 and boolean___has_permission_3) or (boolean___has_permission_2 and boolean___has_permission_3):
            return 'th___width_2'
        if boolean___has_permission_1 or boolean___has_permission_2 or boolean___has_permission_3:
            return 'th___width_1'
        if boolean___has_permission_0:
            return 'th___width_1'
    return 'th___width_0'


@register.filter()
def ___get_boolean___show_the_administration_link___(request):
    if ___required___application___security___user___(request=request):
        if request.___APPLICATION___SECURITY___USER___.is_superuser is True:
            return True
        if request.___APPLICATION___SECURITY___USER___.___boolean___has_permission___(set_identifier___to_verify={'application_security_localuser_list', }):
            return True
        if request.___APPLICATION___SECURITY___USER___.___boolean___has_permission___(set_identifier___to_verify={'application_security_localuserrequest_list', }):
            return True
        if request.___APPLICATION___SECURITY___USER___.___boolean___has_permission___(set_identifier___to_verify={'application_security_ldapuser_list', }):
            return True
        if request.___APPLICATION___SECURITY___USER___.___boolean___has_permission___(set_identifier___to_verify={'application_security_ldapuserrequest_list', }):
            return True
        if request.___APPLICATION___SECURITY___USER___.___boolean___has_permission___(set_identifier___to_verify={'application_security_ldapuserimported_list', }):
            return True
        if request.___APPLICATION___SECURITY___USER___.___boolean___has_permission___(set_identifier___to_verify={'application_security_group_list', }):
            return True
        if request.___APPLICATION___SECURITY___USER___.___boolean___has_permission___(set_identifier___to_verify={'application_security_permission_list', }):
            return True
        if request.___APPLICATION___SECURITY___USER___.___boolean___has_permission___(set_identifier___to_verify={'application_help_document_list', }):
            return True
    return False
