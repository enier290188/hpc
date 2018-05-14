# -*- coding: utf-8 -*-
# django modules import
from django import http

# user modules import
from ....security import (
    decorators as decorators___application___security,
    utils as utils___application___security
)
from ... import utils as utils___hpc
from ... import slurm


@decorators___application___security.___required___request_is_ajax___()
@decorators___application___security.___required___application___security___user___is_ldapuser_or_ldapuserimported___(___application___security___from___module___=utils___application___security.___APPLICATION___SECURITY___FROM___MODULE___HPC___)
def ___view___index___(request):
    dict___data = dict()
    data = slurm.generate_data_dict(request, option='keys')
    if data:
        dict___data['___HTML___APPLICATION___HPC___CONTENT___CENTER___'] = utils___hpc.___html___template___(
            request=request,
            context={
                'DATA': data
            },
            template_name='application/hpc/___includes___/content/center/hpc_jobs/index.html'
        )
        return http.JsonResponse(dict___data)
    else:
        return utils___hpc.___jsonresponse___error___(request)


@decorators___application___security.___required___request_is_ajax___()
@decorators___application___security.___required___application___security___user___is_ldapuser_or_ldapuserimported___(___application___security___from___module___=utils___application___security.___APPLICATION___SECURITY___FROM___MODULE___HPC___)
def ___view___list___(request):
    option = request.GET.get('option', None)
    parameters = request.GET.getlist('parameters[]', None)
    data = slurm.generate_data_json(request, option, parameters=parameters)
    if data:
        return http.HttpResponse(data, content_type='application/json')
    else:
        return utils___hpc.___httpresponse___error___(request)


@decorators___application___security.___required___request_is_ajax___()
@decorators___application___security.___required___application___security___user___is_ldapuser_or_ldapuserimported___(___application___security___from___module___=utils___application___security.___APPLICATION___SECURITY___FROM___MODULE___HPC___)
def ___view___detail___(request):
    dict___data = dict()
    parameters = request.GET.getlist('parameters[]', None)
    data = slurm.generate_data_dict(request, option='detail job', parameters=parameters)
    if data:
        dict___data['detail'] = utils___hpc.___html___template___(
            request=request,
            context={
                'data': data
            },
            template_name='application/hpc/___includes___/content/center/hpc_jobs/___includes___/detail.html'
        )
        return http.JsonResponse(dict___data)
    else:
        return utils___hpc.___httpresponse___error___(request)


@decorators___application___security.___required___request_is_ajax___()
@decorators___application___security.___required___application___security___user___is_ldapuser_or_ldapuserimported___(___application___security___from___module___=utils___application___security.___APPLICATION___SECURITY___FROM___MODULE___HPC___)
def ___view___stop___(request):
    parameters = request.GET.getlist('parameters[]', None)
    slurm.generate_data_dict(request, option='job stop', parameters=parameters)
    return ___view___detail___(request)


@decorators___application___security.___required___request_is_ajax___()
@decorators___application___security.___required___application___security___user___is_ldapuser_or_ldapuserimported___(___application___security___from___module___=utils___application___security.___APPLICATION___SECURITY___FROM___MODULE___HPC___)
def ___view___continue___(request):
    parameters = request.GET.getlist('parameters[]', None)
    slurm.generate_data_dict(request, option='job cont', parameters=parameters)
    return ___view___detail___(request)


@decorators___application___security.___required___request_is_ajax___()
@decorators___application___security.___required___application___security___user___is_ldapuser_or_ldapuserimported___(___application___security___from___module___=utils___application___security.___APPLICATION___SECURITY___FROM___MODULE___HPC___)
def ___view___requeue___(request):
    parameters = request.GET.getlist('parameters[]', None)
    slurm.generate_data_dict(request, option='job requeue', parameters=parameters)
    return ___view___list___(request)


@decorators___application___security.___required___request_is_ajax___()
@decorators___application___security.___required___application___security___user___is_ldapuser_or_ldapuserimported___(___application___security___from___module___=utils___application___security.___APPLICATION___SECURITY___FROM___MODULE___HPC___)
def ___view___kill___(request):
    parameters = request.GET.getlist('parameters[]', None)
    slurm.generate_data_dict(request, option='job kill', parameters=parameters)
    return ___view___list___(request)
