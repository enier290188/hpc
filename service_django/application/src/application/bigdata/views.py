# -*- coding: utf-8 -*-
from . import utils
from src.application.security import (
    decorators as decorators___application___security,
    utils as utils___application___security
)
from django import http, shortcuts


@decorators___application___security.___required___application___security___user___is_ldapuser_or_ldapuserimported___(___application___security___from___module___=utils___application___security.___APPLICATION___SECURITY___FROM___MODULE___BIGDATA___)
def ___view___index___(request):
    dict___context = dict()
    return shortcuts.render(
        request=request,
        context=dict___context,
        template_name='application/bigdata/application___bigdata.html'
    )


@decorators___application___security.___required___request_is_ajax___()
@decorators___application___security.___required___application___security___user___is_ldapuser_or_ldapuserimported___(___application___security___from___module___=utils___application___security.___APPLICATION___SECURITY___FROM___MODULE___BIGDATA___)
def ___view___index___load___(request):
    dict___data = dict()
    dict___data['___BOOLEAN___ERROR___'] = False
    dict___data['___HTML___APPLICATION___BIGDATA___LOAD___'] = utils.___html___template___(
        request=request,
        context=dict(),
        template_name='application/bigdata/___includes___/load/load.html'
    )
    return http.JsonResponse(dict___data)


@decorators___application___security.___required___request_is_ajax___()
@decorators___application___security.___required___application___security___user___is_ldapuser_or_ldapuserimported___(___application___security___from___module___=utils___application___security.___APPLICATION___SECURITY___FROM___MODULE___BIGDATA___)
def ___view___index___title___(request):
    dict___data = dict()
    dict___data['___BOOLEAN___ERROR___'] = False
    dict___data['___HTML___APPLICATION___BIGDATA___TITLE___'] = utils.___html___template___(
        request=request,
        context=dict(),
        template_name='application/bigdata/___includes___/title/title.html'
    )
    return http.JsonResponse(dict___data)


@decorators___application___security.___required___request_is_ajax___()
@decorators___application___security.___required___application___security___user___is_ldapuser_or_ldapuserimported___(___application___security___from___module___=utils___application___security.___APPLICATION___SECURITY___FROM___MODULE___BIGDATA___)
def ___view___index___header___(request):
    dict___data = dict()
    dict___data['___BOOLEAN___ERROR___'] = False
    dict___data['___HTML___APPLICATION___BIGDATA___HEADER___'] = utils.___html___template___(
        request=request,
        context=dict(),
        template_name='application/bigdata/___includes___/header/header.html'
    )
    return http.JsonResponse(dict___data)


@decorators___application___security.___required___request_is_ajax___()
@decorators___application___security.___required___application___security___user___is_ldapuser_or_ldapuserimported___(___application___security___from___module___=utils___application___security.___APPLICATION___SECURITY___FROM___MODULE___BIGDATA___)
def ___view___index___leftside___(request):
    dict___data = dict()
    dict___data['___BOOLEAN___ERROR___'] = False
    dict___data['___HTML___APPLICATION___BIGDATA___LEFTSIDE___'] = utils.___html___template___(
        request=request,
        context=dict(),
        template_name='application/bigdata/___includes___/leftside/leftside.html'
    )
    return http.JsonResponse(dict___data)


@decorators___application___security.___required___request_is_ajax___()
@decorators___application___security.___required___application___security___user___is_ldapuser_or_ldapuserimported___(___application___security___from___module___=utils___application___security.___APPLICATION___SECURITY___FROM___MODULE___BIGDATA___)
def ___view___index___content___center___(request):
    dict___data = dict()
    dict___data['___BOOLEAN___ERROR___'] = False
    dict___data['___HTML___APPLICATION___BIGDATA___CONTENT___CENTER___'] = utils.___html___template___(
        request=request,
        context=dict(),
        template_name='application/bigdata/___includes___/content/center/index.html'
    )
    return http.JsonResponse(dict___data)


@decorators___application___security.___required___request_is_ajax___()
@decorators___application___security.___required___application___security___user___is_ldapuser_or_ldapuserimported___(___application___security___from___module___=utils___application___security.___APPLICATION___SECURITY___FROM___MODULE___BIGDATA___)
def ___view___index___content___footer___(request):
    dict___data = dict()
    dict___data['___BOOLEAN___ERROR___'] = False
    dict___data['___HTML___APPLICATION___BIGDATA___CONTENT___FOOTER___'] = utils.___html___template___(
        request=request,
        context=dict(),
        template_name='application/bigdata/___includes___/content/footer/footer.html'
    )
    return http.JsonResponse(dict___data)


@decorators___application___security.___required___request_is_ajax___()
def ___view___login___(request):
    return utils___application___security.___jsonresponse___login___(
        request=request,
        ___application___security___from___module___=utils___application___security.___APPLICATION___SECURITY___FROM___MODULE___BIGDATA___
    )


@decorators___application___security.___required___request_is_ajax___()
def ___view___login___forgot_credentials_1___(request):
    return utils___application___security.___jsonresponse___login___forgot_credentials_1___(
        request=request,
        ___application___security___from___module___=utils___application___security.___APPLICATION___SECURITY___FROM___MODULE___BIGDATA___
    )


@decorators___application___security.___required___request_is_ajax___()
def ___view___login___forgot_credentials_2___(request, pk):
    return utils___application___security.___jsonresponse___login___forgot_credentials_2___(
        request=request,
        ___application___security___from___module___=utils___application___security.___APPLICATION___SECURITY___FROM___MODULE___BIGDATA___,
        pk=pk
    )


@decorators___application___security.___required___request_is_ajax___()
def ___view___login___forgot_credentials_3___(request, pk):
    return utils___application___security.___jsonresponse___login___forgot_credentials_3___(
        request=request,
        ___application___security___from___module___=utils___application___security.___APPLICATION___SECURITY___FROM___MODULE___BIGDATA___,
        pk=pk
    )


@decorators___application___security.___required___request_is_ajax___()
def ___view___login___request___(request):
    return utils___application___security.___jsonresponse___login___request___(
        request=request,
        ___application___security___from___module___=utils___application___security.___APPLICATION___SECURITY___FROM___MODULE___BIGDATA___
    )


@decorators___application___security.___required___request_is_ajax___()
@decorators___application___security.___required___application___security___user___is_ldapuser_or_ldapuserimported___(___application___security___from___module___=utils___application___security.___APPLICATION___SECURITY___FROM___MODULE___BIGDATA___)
def ___view___logout___(request):
    return utils___application___security.___jsonresponse___logout___(
        request=request,
        ___application___security___from___module___=utils___application___security.___APPLICATION___SECURITY___FROM___MODULE___BIGDATA___
    )


@decorators___application___security.___required___request_is_ajax___()
@decorators___application___security.___required___application___security___user___is_ldapuser_or_ldapuserimported___(___application___security___from___module___=utils___application___security.___APPLICATION___SECURITY___FROM___MODULE___BIGDATA___)
def ___view___profile___(request):
    return utils___application___security.___jsonresponse___profile___(
        request=request,
        ___application___security___from___module___=utils___application___security.___APPLICATION___SECURITY___FROM___MODULE___BIGDATA___
    )


@decorators___application___security.___required___request_is_ajax___()
def ___view___locale___(request):
    return utils___application___security.___jsonresponse___locale___(
        request=request,
        ___application___security___from___module___=utils___application___security.___APPLICATION___SECURITY___FROM___MODULE___BIGDATA___
    )
