# -*- coding: utf-8 -*-
from ... import utils as utils___hpc
from src.application.security import (
    decorators as decorators___application___security,
    utils as utils___application___security
)
from django import http


@decorators___application___security.___required___request_is_ajax___()
@decorators___application___security.___required___application___security___user___is_ldapuser___(___application___security___from___module___=utils___application___security.___APPLICATION___SECURITY___FROM___MODULE___HPC___)
def ___view___index___(request):
    dict___data = dict()
    dict___data['___HTML___APPLICATION___HPC___CONTENT___CENTER___'] = utils___hpc.___html___template___(
        request=request,
        context=dict(),
        template_name='application/hpc/___includes___/content/center/hpc_module02/index.html'
    )
    return http.JsonResponse(dict___data)

