# -*- coding: utf-8 -*-
from ... import utils as utils___hpc
from . import slurm
from src.application.security import (
    decorators as decorators___application___security,
    utils as utils___application___security
)
from django import http
from django.contrib import messages
import json


@decorators___application___security.___required___request_is_ajax___()
@decorators___application___security.___required___application___security___user___is_ldapuser_or_ldapuserimported___(___application___security___from___module___=utils___application___security.___APPLICATION___SECURITY___FROM___MODULE___HPC___)
def ___view___index___(request):
    dict___data = dict()
    instance = request.___APPLICATION___SECURITY___USER___
    has_error, data_content = slurm.exec_cmd(instance, parameters='keys')
    if has_error:
        messages.add_message(request, messages.ERROR, data_content)
        return utils___hpc.___jsonresponse___error___(request)
    else:
        dict___data['___HTML___APPLICATION___HPC___CONTENT___CENTER___'] = utils___hpc.___html___template___(
            request=request,
            context={
                'DATA': data_content
            },
            template_name='application/hpc/___includes___/content/center/hpc_jobs/index.html'
        )
        return http.JsonResponse(dict___data)


@decorators___application___security.___required___request_is_ajax___()
@decorators___application___security.___required___application___security___user___is_ldapuser_or_ldapuserimported___(___application___security___from___module___=utils___application___security.___APPLICATION___SECURITY___FROM___MODULE___HPC___)
def ___view___api___(request):
    if request.method == "POST":
        parameters = request.POST.getlist('parameters[]', None)
    else:
        parameters = request.GET.getlist('parameters[]', None)
    instance = request.___APPLICATION___SECURITY___USER___
    has_error, data_content = slurm.exec_cmd(instance, parameters=parameters)
    if has_error:
        messages.add_message(request, messages.ERROR, data_content)
        return utils___hpc.___jsonresponse___error___(request)
    else:
        return http.HttpResponse(json.dumps(data_content), content_type='application/json')
