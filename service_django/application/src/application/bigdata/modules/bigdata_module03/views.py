# -*- coding: utf-8 -*-
from ... import utils as utils___bigdata
from src.application.security import (
    decorators as decorators___application___security,
    utils as utils___application___security
)
from django import http


@decorators___application___security.___required___request_is_ajax___()
@decorators___application___security.___required___application___security___user___is_ldapuser_or_ldapuserimported___(___application___security___from___module___=utils___application___security.___APPLICATION___SECURITY___FROM___MODULE___BIGDATA___)
def ___view___index___(request):
    dict___data = dict()
    dict___data['___HTML___APPLICATION___BIGDATA___CONTENT___CENTER___'] = utils___bigdata.___html___template___(
        request=request,
        context=dict(),
        template_name='application/bigdata/___includes___/content/center/bigdata_module03/index.html'
    )
    return http.JsonResponse(dict___data)

