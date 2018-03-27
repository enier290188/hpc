# -*- coding: utf-8 -*-
from . import ldap, models, utils
from django import http, shortcuts
from django.contrib import messages
from django.core import urlresolvers
from django.utils.translation import ugettext_lazy as _


def ___jsonresponse___not_permission___(request, ___application___security___from___module___):
    if request.is_ajax():
        dict___data = dict()
        dict___data['___BOOLEAN___ERROR___'] = True
        messages.add_message(request, messages.ERROR, _('APPLICATION___SECURITY___MESSAGE Action not performed, you do not have permission.'))
        dict_string___application___security___from___module = utils.___dict_string___application___security___from___module___(request=request, ___application___security___from___module___=___application___security___from___module___)
        string___modal = dict_string___application___security___from___module['string___modal']
        string___modal___message = dict_string___application___security___from___module['string___modal___message']
        string___modal___modal = dict_string___application___security___from___module['string___modal___modal']
        string___modal___modal___message = dict_string___application___security___from___module['string___modal___modal___message']
        dict___data[string___modal] = utils.___html___template_modal___message___(request=request, ___application___security___from___module___=___application___security___from___module___)
        dict___data[string___modal___message] = utils.___html___template_message___(request=request, ___application___security___from___module___=___application___security___from___module___)
        dict___data[string___modal___modal] = utils.___html___template_modal___message___(request=request, ___application___security___from___module___=___application___security___from___module___)
        dict___data[string___modal___modal___message] = utils.___html___template_message___(request=request, ___application___security___from___module___=___application___security___from___module___)
        dict___data['___APPLICATION___SECURITY___USER___WITHOUT_PERMISSION___'] = True
        dict___data['___APPLICATION___SECURITY___USER___URL_REDIRECT___'] = urlresolvers.reverse(utils.___APPLICATION___SECURITY___USER___URL_REVERSE___)
        return http.JsonResponse(dict___data)
    else:
        return shortcuts.redirect(urlresolvers.reverse(utils.___APPLICATION___SECURITY___USER___URL_REVERSE___))


def ___required___request_is_ajax___(function=None):
    def _decorator(view_func):
        def _view(request, *args, **kwargs):
            if request.is_ajax():
                return view_func(request, *args, **kwargs)
            return shortcuts.redirect(urlresolvers.reverse(utils.___APPLICATION___SECURITY___USER___URL_REVERSE___))

        return _view

    if function is None:
        return _decorator
    else:
        return _decorator(function)


def ___required___application___security___user___(function=None, ___application___security___from___module___=''):
    def _decorator(view_func):
        def _view(request, *args, **kwargs):
            if request.___APPLICATION___SECURITY___USER___ is not None:
                return view_func(request, *args, **kwargs)
            return ___jsonresponse___not_permission___(request=request, ___application___security___from___module___=___application___security___from___module___)

        return _view

    if function is None:
        return _decorator
    else:
        return _decorator(function)


def ___required___application___security___user___has_permission___(function=None, ___application___security___from___module___='', set_identifier___to_verify=set()):
    def _decorator(view_func):
        @___required___application___security___user___(___application___security___from___module___=___application___security___from___module___)
        def _view(request, *args, **kwargs):
            if request.___APPLICATION___SECURITY___USER___.is_superuser is True or request.___APPLICATION___SECURITY___USER___.___boolean___has_permission___(set_identifier___to_verify=set_identifier___to_verify):
                return view_func(request, *args, **kwargs)
            return ___jsonresponse___not_permission___(request=request, ___application___security___from___module___=___application___security___from___module___)

        return _view

    if function is None:
        return _decorator
    else:
        return _decorator(function)


def ___required___application___security___user___is_localuser___(function=None, ___application___security___from___module___=''):
    def _decorator(view_func):
        @___required___application___security___user___()
        def _view(request, *args, **kwargs):
            if isinstance(request.___APPLICATION___SECURITY___USER___, models.LOCALUser):
                return view_func(request, *args, **kwargs)
            return ___jsonresponse___not_permission___(request=request, ___application___security___from___module___=___application___security___from___module___)

        return _view

    if function is None:
        return _decorator
    else:
        return _decorator(function)


def ___required___application___security___user___is_ldapuser_or_ldapuserimported___(function=None, ___application___security___from___module___=''):
    def _decorator(view_func):
        @___required___application___security___user___()
        def _view(request, *args, **kwargs):
            if isinstance(request.___APPLICATION___SECURITY___USER___, models.LDAPUser) or isinstance(request.___APPLICATION___SECURITY___USER___, models.LDAPUserImported):
                return view_func(request, *args, **kwargs)
            return ___jsonresponse___not_permission___(request=request, ___application___security___from___module___=___application___security___from___module___)

        return _view

    if function is None:
        return _decorator
    else:
        return _decorator(function)


def ___required___application___security___user___is_ldapuser___(function=None, ___application___security___from___module___=''):
    def _decorator(view_func):
        @___required___application___security___user___()
        def _view(request, *args, **kwargs):
            if isinstance(request.___APPLICATION___SECURITY___USER___, models.LDAPUser):
                return view_func(request, *args, **kwargs)
            return ___jsonresponse___not_permission___(request=request, ___application___security___from___module___=___application___security___from___module___)

        return _view

    if function is None:
        return _decorator
    else:
        return _decorator(function)


def ___required___application___security___user___is_ldapuserimported___(function=None, ___application___security___from___module___=''):
    def _decorator(view_func):
        @___required___application___security___user___()
        def _view(request, *args, **kwargs):
            if isinstance(request.___APPLICATION___SECURITY___USER___, models.LDAPUserImported):
                return view_func(request, *args, **kwargs)
            return ___jsonresponse___not_permission___(request=request, ___application___security___from___module___=___application___security___from___module___)

        return _view

    if function is None:
        return _decorator
    else:
        return _decorator(function)


def ___required___ldap_connection___(function=None, ___application___security___from___module___=''):
    def _decorator(view_func):
        def _view(request, *args, **kwargs):
            boolean___is_there_connection = False
            connection = ldap.___connection___ldap___()
            try:
                # start the connection
                if connection.bind():
                    boolean___is_there_connection = True
            except (Exception,):
                pass
            finally:
                # close the connection
                connection.unbind()
            if boolean___is_there_connection is False:
                dict___data = dict()
                dict___data['___BOOLEAN___ERROR___'] = True
                messages.add_message(request, messages.ERROR, _('APPLICATION___SECURITY___MESSAGE Action not performed, connection to the LDAP could not be established.'))
                dict_string___application___security___from___module = utils.___dict_string___application___security___from___module___(request=request, ___application___security___from___module___=___application___security___from___module___)
                string___modal = dict_string___application___security___from___module['string___modal']
                string___modal___message = dict_string___application___security___from___module['string___modal___message']
                string___modal___modal = dict_string___application___security___from___module['string___modal___modal']
                string___modal___modal___message = dict_string___application___security___from___module['string___modal___modal___message']
                dict___data[string___modal] = utils.___html___template_modal___message___(request=request, ___application___security___from___module___=___application___security___from___module___)
                dict___data[string___modal___message] = utils.___html___template_message___(request=request, ___application___security___from___module___=___application___security___from___module___)
                dict___data[string___modal___modal] = utils.___html___template_modal___message___(request=request, ___application___security___from___module___=___application___security___from___module___)
                dict___data[string___modal___modal___message] = utils.___html___template_message___(request=request, ___application___security___from___module___=___application___security___from___module___)
                return http.JsonResponse(dict___data)
            else:
                return view_func(request, *args, **kwargs)

        return _view

    if function is None:
        return _decorator
    else:
        return _decorator(function)
