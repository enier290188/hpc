from . import models, utils
from django.utils import translation


class ApplicationSecurityMiddleware(object):
    def process_request(self, request):
        instance = None
        if request.session.get('___APPLICATION___SECURITY___USER___MODEL___') and (request.session.get('___APPLICATION___SECURITY___USER___PK___')):
            if request.session.get('___APPLICATION___SECURITY___USER___MODEL___') == utils.___APPLICATION___SECURITY___USER___MODEL___LOCALUSER___:
                instance = models.LOCALUser.objects.___instance___by_pk___(pk=request.session.get('___APPLICATION___SECURITY___USER___PK___'))
            if request.session.get('___APPLICATION___SECURITY___USER___MODEL___') == utils.___APPLICATION___SECURITY___USER___MODEL___LDAPUSER___:
                instance = models.LDAPUser.objects.___instance___by_pk___(pk=request.session.get('___APPLICATION___SECURITY___USER___PK___'))
            if request.session.get('___APPLICATION___SECURITY___USER___MODEL___') == utils.___APPLICATION___SECURITY___USER___MODEL___LDAPUSERIMPORTED___:
                instance = models.LDAPUserImported.objects.___instance___by_pk___(pk=request.session.get('___APPLICATION___SECURITY___USER___PK___'))
            if instance is not None:
                translation.activate(instance.locale)
                request.session[translation.LANGUAGE_SESSION_KEY] = instance.locale
        request.___APPLICATION___SECURITY___USER___ = instance
        #
        list_string___url = (
            '/website/',
            '/website/modules/website_home/',
            '/website/modules/website_help/',
            '/hpc/',
            '/hpc/modules/hpc_jobs/',
            '/hpc/modules/hpc_script/',
            '/hpc/modules/hpc_nodes/',
            '/hpc/modules/hpc_explorer/',
            '/bigdata/',
            '/bigdata/modules/bigdata_module01/',
            '/bigdata/modules/bigdata_module02/',
            '/bigdata/modules/bigdata_module03/',
            '/administration/',
            '/administration/modules/administration_security/localuser/',
            '/administration/modules/administration_security/localuserrequest/',
            '/administration/modules/administration_security/ldapuser/',
            '/administration/modules/administration_security/ldapuserrequest/',
            '/administration/modules/administration_security/ldapuserimported/',
            '/administration/modules/administration_security/group/',
            '/administration/modules/administration_security/permission/',
            '/administration/modules/administration_help/document/',
        )
        if request.path in list_string___url:
            if request.path == '/website/':
                request.session['___APPLICATION___SECURITY___USER___URL_CURRENT___'] = '/website/modules/website_home/'
            elif request.path == '/hpc/':
                request.session['___APPLICATION___SECURITY___USER___URL_CURRENT___'] = '/hpc/modules/hpc_jobs/'
            elif request.path == '/bigdata/':
                request.session['___APPLICATION___SECURITY___USER___URL_CURRENT___'] = '/bigdata/modules/bigdata_module01/'
            else:
                request.session['___APPLICATION___SECURITY___USER___URL_CURRENT___'] = request.path

    def process_response(self, request, response):
        return response
