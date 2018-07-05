# -*- coding: utf-8 -*-
# django modules import
from django import http
from django.contrib import messages
from django.http import HttpResponse
# from django.views.decorators.csrf import csrf_exempt

# python libraries import
from tempfile import TemporaryFile

# user modules import
from ....security import (
    decorators as decorators___application___security,
    utils as utils___application___security
)
from ... import utils as utils___hpc
from ... import ssh, linux, slurm
from . import forms


@decorators___application___security.___required___request_is_ajax___()
@decorators___application___security.___required___application___security___user___is_ldapuser___(___application___security___from___module___=utils___application___security.___APPLICATION___SECURITY___FROM___MODULE___HPC___)
def ___view___index___(request):
    dict___data = dict()
    path = linux.generate_data_dict(request, 'path')
    dict___data['___HTML___APPLICATION___HPC___CONTENT___CENTER___'] = utils___hpc.___html___template___(
        request=request,
        context={
            'home': path,
            'path': path,
        },
        template_name='application/hpc/___includes___/content/center/hpc_explorer/index.html'
    )
    return http.JsonResponse(dict___data)


@decorators___application___security.___required___request_is_ajax___()
@decorators___application___security.___required___application___security___user___is_ldapuser_or_ldapuserimported___(___application___security___from___module___=utils___application___security.___APPLICATION___SECURITY___FROM___MODULE___HPC___)
def ___view___list___(request):
    dict___data = dict()
    path = request.GET.get('path', None)
    data = linux.generate_data_dict(request, option='list', parameters=[path])
    if data:
        dict___data['list'] = utils___hpc.___html___template___(
            request=request,
            context={
                'data': data
            },
            template_name='application/hpc/___includes___/content/center/hpc_explorer/___includes___/list.html'
        )
        return http.JsonResponse(dict___data)
    else:
        return utils___hpc.___httpresponse___error___(request)


@decorators___application___security.___required___request_is_ajax___()
@decorators___application___security.___required___application___security___user___is_ldapuser_or_ldapuserimported___(___application___security___from___module___=utils___application___security.___APPLICATION___SECURITY___FROM___MODULE___HPC___)
def ___view___modal___(request):
    dict___data = dict()
    dict___data['___BOOLEAN___ERROR___'] = False
    if request.method == 'POST':
        option = request.POST.get('option', None)
        parameters = list()
        parameters.append(request.POST.get('path', None))
        if option == 'rename':
            parameters.append(request.POST.get('name', None))
        parameters.append(request.POST.get('generic', None))
        data = linux.generate_data_dict(request, option=option, parameters=parameters)
        if data:
            dict___data['list'] = utils___hpc.___html___template___(
                request=request,
                context={
                    'data': data
                },
                template_name='application/hpc/___includes___/content/center/hpc_explorer/___includes___/list.html'
            )
            return http.JsonResponse(dict___data)
        else:
            return utils___hpc.___jsonresponse___error___(request)
    else:
        option = request.GET.get('option', None)
        if option:
            dict___data['___HTML___APPLICATION___HPC___MODAL___'] = utils___hpc.___html___template___(
                request=request,
                context={
                    'form': forms.GenericForm(option=option)
                },
                template_name='application/hpc/___includes___/modal/hpc/' + option + '.html'
            )
            dict___data['___HTML___APPLICATION___HPC___MODAL___MESSAGE___'] = utils___hpc.___html___template_message___(request=request)
            return http.JsonResponse(dict___data)
        else:
            return utils___hpc.___jsonresponse___error___(request)


@decorators___application___security.___required___request_is_ajax___()
@decorators___application___security.___required___application___security___user___is_ldapuser_or_ldapuserimported___(___application___security___from___module___=utils___application___security.___APPLICATION___SECURITY___FROM___MODULE___HPC___)
def ___view___upload___(request):
    dict___data = dict()
    dict___data['___BOOLEAN___ERROR___'] = False
    if request.method == 'POST':
        path = request.POST.get('path')
        files = request.FILES.getlist('files')
        form = forms.UploadMultipleFilesForm(request.POST, request.FILES)
        instance = request.___APPLICATION___SECURITY___USER___
        if form.is_valid():
            for file in files:
                ssh.ssh_sftp_putfo(instance.group_identifier(), instance.private_key.path, file, path + '/' + file.name)
            data = linux.generate_data_dict(request, option='list', parameters=[path])
            if data:
                dict___data['list'] = utils___hpc.___html___template___(
                    request=request,
                    context={
                        'data': data
                    },
                    template_name='application/hpc/___includes___/content/center/hpc_explorer/___includes___/list.html'
                )
                return http.JsonResponse(dict___data)
        return utils___hpc.___httpresponse___error___(request)
    else:
        dict___data['___HTML___APPLICATION___HPC___MODAL___'] = utils___hpc.___html___template___(
            request=request,
            context={
                'form': forms.UploadMultipleFilesForm()
            },
            template_name='application/hpc/___includes___/modal/hpc/upload.html'
        )
        dict___data['___HTML___APPLICATION___HPC___MODAL___MESSAGE___'] = utils___hpc.___html___template_message___(request=request)
        return http.JsonResponse(dict___data)


@decorators___application___security.___required___application___security___user___is_ldapuser_or_ldapuserimported___(___application___security___from___module___=utils___application___security.___APPLICATION___SECURITY___FROM___MODULE___HPC___)
def ___view___download___(request):
    path = request.GET.get('path', None)
    name = request.GET.get('name', None)
    instance = request.___APPLICATION___SECURITY___USER___

    with TemporaryFile() as f:
        ssh.ssh_sftp_getfo(instance.group_identifier(), instance.private_key.path, path + '/' + name, f)
        f.seek(0)
        response = HttpResponse(f.read())
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Description'] = 'File Transfer'
    response['Content-Encoding'] = 'binary'
    response['Content-Disposition'] = 'attachment; filename=%s' % name
    response['Expires'] = 0
    response['Cache-Control'] = 'must-revalidate'
    response['Pragma'] = 'public'
    return response


@decorators___application___security.___required___request_is_ajax___()
@decorators___application___security.___required___application___security___user___is_ldapuser_or_ldapuserimported___(___application___security___from___module___=utils___application___security.___APPLICATION___SECURITY___FROM___MODULE___HPC___)
def ___view___edit___(request):
    dict___data = dict()
    dict___data['___BOOLEAN___ERROR___'] = False
    if request.method == 'POST':
        path = request.POST.get('path')
        file_name = request.POST.get('file_name')
        form = forms.FileEditForm(request.POST)
        if form.is_valid():
            file_content = form.cleaned_data.get('file_content')
            if linux.edit_file(request, path + '/' + file_name, file_content) is True:
                dict___data['___BOOLEAN___ERROR___'] = True
        return http.JsonResponse(dict___data)
    else:
        path = request.GET.get('path')
        file_name = request.GET.get('file_name')
        file_content = linux.open_file(request, path + '/' + file_name)
        if file_content is True:
            dict___data['___BOOLEAN___ERROR___'] = True
            messages.add_message(request, messages.ERROR, 'Open file is not posible')
            return utils___hpc.___jsonresponse___error___(request)
        else:
            dict___data['___HTML___APPLICATION___HPC___MODAL___'] = utils___hpc.___html___template___(
                request=request,
                context={
                    'form': forms.FileEditForm(content=file_content)
                },
                template_name='application/hpc/___includes___/modal/hpc/edit.html'
            )
            dict___data['___HTML___APPLICATION___HPC___MODAL___MESSAGE___'] = utils___hpc.___html___template_message___(request=request)
            return http.JsonResponse(dict___data)


@decorators___application___security.___required___request_is_ajax___()
@decorators___application___security.___required___application___security___user___is_ldapuser_or_ldapuserimported___(___application___security___from___module___=utils___application___security.___APPLICATION___SECURITY___FROM___MODULE___HPC___)
def ___view___delete___(request):
    dict___data = dict()
    dict___data['___BOOLEAN___ERROR___'] = False
    values = request.POST.getlist('values[]', None)
    data = linux.generate_data_dict(request, option='delete', parameters=values)
    if data:
        dict___data['list'] = utils___hpc.___html___template___(
            request=request,
            context={
                'data': data
            },
            template_name='application/hpc/___includes___/content/center/hpc_explorer/___includes___/list.html'
        )
        return http.JsonResponse(dict___data)


@decorators___application___security.___required___request_is_ajax___()
@decorators___application___security.___required___application___security___user___is_ldapuser_or_ldapuserimported___(___application___security___from___module___=utils___application___security.___APPLICATION___SECURITY___FROM___MODULE___HPC___)
def ___view___execute___(request):
    dict___data = dict()
    dict___data['___BOOLEAN___ERROR___'] = False
    if request.method == 'POST':
        values = request.POST.getlist('values[]')
        slurm.generate_data_dict(request, 'execute', values)
        if len(messages.get_messages(request=request)) <= 0:
            messages.add_message(request, request.SUCCESS, 'Todo ok')
        else:
            dict___data['___BOOLEAN___ERROR___'] = True
        dict___data['___HTML___APPLICATION___HPC___MODAL___'] = utils___hpc.___html___template_modal___message___(request=request)
        dict___data['___HTML___APPLICATION___HPC___MODAL___MESSAGE___'] = utils___hpc.___html___template_message___(request=request)
        return http.JsonResponse(dict___data)
    else:
        dict___data['___HTML___APPLICATION___HPC___MODAL___'] = utils___hpc.___html___template___(
            request=request,
            context=dict(),
            template_name='application/hpc/___includes___/modal/hpc/execute.html'
        )
        return http.JsonResponse(dict___data)


'''
@decorators___application___security.___required___request_is_ajax___()
@decorators___application___security.___required___application___security___user___is_ldapuser_or_ldapuserimported___(___application___security___from___module___=utils___application___security.___APPLICATION___SECURITY___FROM___MODULE___HPC___)
def ___view___create_folder___(request):
    dict___data = dict()
    dict___data['___BOOLEAN___ERROR___'] = False
    if request.method == 'POST':
        parameters = list()
        parameters.append(request.POST.get('path', None))
        parameters.append(request.POST.get('generic', None))
        data = linux.generate_data_dict(request, option='folder', parameters=parameters)
        dict___data['___BOOLEAN___ERROR___'] = True
        dict___data['___HTML___APPLICATION___HPC___MODAL___'] = utils___hpc.___html___template_modal___message___(request=request)
        dict___data['___HTML___APPLICATION___HPC___MODAL___MESSAGE___'] = utils___hpc.___html___template_message___(request=request)
        dict___data['list'] = utils___hpc.___html___template___(
            request=request,
            context={
                'data': data
            },
            template_name='application/hpc/___includes___/content/center/hpc_explorer/___includes___/list.html'
        )
        return http.JsonResponse(dict___data)
    else:
        dict___data['___HTML___APPLICATION___HPC___MODAL___'] = utils___hpc.___html___template___(
            request=request,
            context={
                'form': forms.GenericForm(option='folder')
            },
            template_name='application/hpc/___includes___/modal/hpc/folder.html'
        )
        dict___data['___HTML___APPLICATION___HPC___MODAL___MESSAGE___'] = utils___hpc.___html___template_message___(request=request)
        return http.JsonResponse(dict___data)

'''