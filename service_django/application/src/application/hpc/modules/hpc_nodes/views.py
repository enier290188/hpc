# -*- coding: utf-8 -*-
# django modules import
from django import http
from django.conf import settings
from django.utils import timezone
from django.http import HttpResponse

# user modules import
from ....security import (
    decorators as decorators___application___security,
    utils as utils___application___security
)
from ... import utils as utils___hpc
from ... import ssh
from ... import slurm


@decorators___application___security.___required___request_is_ajax___()
@decorators___application___security.___required___application___security___user___is_ldapuser___(___application___security___from___module___=utils___application___security.___APPLICATION___SECURITY___FROM___MODULE___HPC___)
def ___view___index___(request):
    dict___data = dict()
    import random
    info = slurm.generate_data_dict(request, option='nodes')
    info.update({'random': random.random()})
    if info:
        dict___data['___HTML___APPLICATION___HPC___CONTENT___CENTER___'] = utils___hpc.___html___template___(
            request=request,
            context=info,
            template_name='application/hpc/___includes___/content/center/hpc_nodes/index.html'
        )
        return http.JsonResponse(dict___data)
    else:
        return utils___hpc.___jsonresponse___error___(request)


@decorators___application___security.___required___request_is_ajax___()
@decorators___application___security.___required___application___security___user___is_ldapuser___(___application___security___from___module___=utils___application___security.___APPLICATION___SECURITY___FROM___MODULE___HPC___)
def ___view___chartnodes___(request):
    serializers = slurm.generate_data_json(request, option='nodes')
    return HttpResponse(serializers)
