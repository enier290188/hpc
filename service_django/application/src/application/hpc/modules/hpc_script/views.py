# -*- coding: utf-8 -*-
# django modules import
from django import http
from django.conf import settings
from django.contrib import messages
from django.utils import timezone

# python libraries import
import os

# user modules import
from ....security import (
    decorators as decorators___application___security,
    utils as utils___application___security
)
from ... import utils as utils___hpc
from ... import ssh
from ... import linux
from . import forms
from . import script


@decorators___application___security.___required___request_is_ajax___()
@decorators___application___security.___required___application___security___user___is_ldapuser___(___application___security___from___module___=utils___application___security.___APPLICATION___SECURITY___FROM___MODULE___HPC___)
def ___view___index___(request):
    dict___data = dict()
    if request.method == "POST":
        form = forms.ScriptForm(request.POST, request=request)
        if form.is_valid():
            script_name = form.cleaned_data.get('script_name') + '.sl'
            file = os.path.join(settings.MEDIA_ROOT, script_name + str(timezone.now()))
            with open(file, 'wb') as f:
                for line in script.build(form).splitlines():
                    f.write(bytes(line, 'utf-8') + b'\n')
            instance = request.___APPLICATION___SECURITY___USER___
            username = '42110027' # instance.username
            password = '12345*abc' # instance.password
            result = ssh.ssh_sftp_put(username, password, file, script_name)
            os.unlink(file)
            if result['HAS_ERROR']:
                messages.add_message(request, messages.ERROR, result['MESSAGE'])
                return utils___hpc.___jsonresponse___error___(request)
            if request.POST.get('submit') == 'run':
                result = ssh.ssh_exec(username, password, 'sbatch "' + script_name + '"')
                if result['HAS_ERROR']:
                    messages.add_message(request, messages.ERROR, result['MESSAGE'])
                    return utils___hpc.___jsonresponse___error___(request)
                else:
                    messages.add_message(request, messages.SUCCESS, 'El script se ha guardado en la carpeta de usuario y y se ha enviado a la cola de ejecucion.')
            else:
                messages.add_message(request, messages.SUCCESS, 'El script se ha guardado satisfactoriamente en la carpeta del usuario.')
            return utils___hpc.___jsonresponse___success___(request)
        else:
            dict___data['___HTML___APPLICATION___HPC___CONTENT___CENTER___'] = utils___hpc.___html___template___(
                request=request,
                context={
                    'form': form
                },
                template_name='application/hpc/___includes___/content/center/hpc_script/index.html'
            )
            return http.JsonResponse(dict___data)
    else:
        dict___data['___HTML___APPLICATION___HPC___CONTENT___CENTER___'] = utils___hpc.___html___template___(
            request=request,
            context={
                'form': forms.ScriptForm(request=request),
                'method': 'GET',
            },
            template_name='application/hpc/___includes___/content/center/hpc_script/index.html'
        )
        return http.JsonResponse(dict___data)


@decorators___application___security.___required___request_is_ajax___()
@decorators___application___security.___required___application___security___user___is_ldapuser___(___application___security___from___module___=utils___application___security.___APPLICATION___SECURITY___FROM___MODULE___HPC___)
def ___view___vars___(request):
    dict___data = dict()
    dict___data['___BOOLEAN___ERROR___'] = False
    data = linux.generate_data_dict(request, option='envVars')
    if data:
        messages.add_message(request, messages.SUCCESS, 'Esto es la ostia')
        dict___data['___HTML___APPLICATION___HPC___MODAL___'] = utils___hpc.___html___template___(
            request=request,
            context={
                'variables': data
            },
            template_name='application/hpc/___includes___/modal/hpc/variables.html'
        )
        dict___data['___HTML___APPLICATION___HPC___MODAL___MESSAGE___'] = utils___hpc.___html___template_message___(request=request)
        return http.JsonResponse(dict___data)
    else:
        return utils___hpc.___jsonresponse___error___(request)
