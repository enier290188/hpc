# -*- coding: utf-8 -*-
from ... import utils as utils___website
from src.application.security import (
    decorators as decorators___application___security,
)
from django import http


@decorators___application___security.___required___request_is_ajax___()
def ___view___index___(request):
    dict___data = dict()
    dict___data['___HTML___APPLICATION___WEBSITE___CONTENT___CENTER___'] = utils___website.___html___template___(
        request=request,
        context=dict(),
        template_name='application/website/___includes___/content/center/website_home/index.html',
    )
    return http.JsonResponse(dict___data)
