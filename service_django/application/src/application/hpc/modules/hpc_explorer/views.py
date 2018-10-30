# -*- coding: utf-8 -*-
# django modules import
from django import http
from django.contrib import messages
from django.http import HttpResponse
from django.utils.translation import ugettext_lazy as _

# python libraries import
from tempfile import TemporaryFile
from datetime import datetime

# user modules import
from ....security import (
    decorators as decorators___application___security,
    utils as utils___application___security
)
from ... import utils as utils___hpc
from ... import ssh, linux, crlf
from . import forms


@decorators___application___security.___required___request_is_ajax___()
@decorators___application___security.___required___application___security___user___is_ldapuser_or_ldapuserimported___(___application___security___from___module___=utils___application___security.___APPLICATION___SECURITY___FROM___MODULE___HPC___)
def ___view___index___(request):
    dict___data = dict()
    path = linux.generate_data_dict(request, 'path')
    if path:
        dict___data['___HTML___APPLICATION___HPC___CONTENT___CENTER___'] = utils___hpc.___html___template___(
            request=request,
            context={
                'home': path,
                'path': path,
            },
            template_name='application/hpc/___includes___/content/center/hpc_explorer/index.html'
        )
        return http.JsonResponse(dict___data)
    else:
        return utils___hpc.___httpresponse___error___(request)


@decorators___application___security.___required___request_is_ajax___()
@decorators___application___security.___required___application___security___user___is_ldapuser_or_ldapuserimported___(___application___security___from___module___=utils___application___security.___APPLICATION___SECURITY___FROM___MODULE___HPC___)
def ___view___list___(request):
    dict___data = dict()
    path = request.GET.get('path', None)
    data = linux.generate_data_dict(request, option='list', dict___data=dict___data, parameters=[path])
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
def ___view___edit___(request):
    instance = request.___APPLICATION___SECURITY___USER___
    dict___data = dict()
    dict___data['___BOOLEAN___ERROR___'] = False
    if request.method == 'POST':
        full_path = request.POST.get('path') + '/' + request.POST.get('file_name')
        form = forms.FileEditForm(request.POST)
        if form.is_valid():
            file_content = crlf.normalize_line_endings(form.cleaned_data.get('file_content'))
            if isinstance(linux.edit_file(instance, full_path, file_content), tuple):
                dict___data['___BOOLEAN___ERROR___'] = True
        return http.JsonResponse(dict___data)
    else:
        full_path = request.GET.get('path') + '/' + request.GET.get('file_name')
        error, response = ssh.ssh_exec(instance.group_identifier(), instance.private_key.path, 'file -bi "%s"' % full_path)
        if error:
            messages.add_message(request, messages.ERROR, response)
        else:
            encoding = response.decode('utf-8')
            if encoding.find("text/") == -1:
                messages.add_message(request, messages.ERROR, _('HPC___SSH___MESSAGES_OpenFileNotEncodingText') % encoding)
            else:
                error, response = linux.open_file(instance, full_path)
                if error:
                    messages.add_message(request, messages.ERROR, response)
                else:
                    dict___data['___HTML___APPLICATION___HPC___MODAL___'] = utils___hpc.___html___template___(
                        request=request,
                        context={'form': forms.FileEditForm(content=response)},
                        template_name='application/hpc/___includes___/modal/hpc/edit.html'
                    )
                    return http.JsonResponse(dict___data)
        dict___data['___BOOLEAN___ERROR___'] = True
        return utils___hpc.___jsonresponse___error___(request)


@decorators___application___security.___required___request_is_ajax___()
@decorators___application___security.___required___application___security___user___is_ldapuser_or_ldapuserimported___(___application___security___from___module___=utils___application___security.___APPLICATION___SECURITY___FROM___MODULE___HPC___)
def ___view___rename___(request):
    dict___data = dict()
    dict___data['___BOOLEAN___ERROR___'] = False
    if request.method == 'POST':
        path = request.POST.get('path', None)
        name = request.POST.get('name', None)
        new_name = request.POST.get('generic', None)
        data = linux.generate_data_dict(request, option='rename', dict___data=dict___data, parameters=[path, name, new_name])
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
        dict___data['___HTML___APPLICATION___HPC___MODAL___'] = utils___hpc.___html___template___(
            request=request,
            context={
                'form': forms.GenericForm(option='rename')
            },
            template_name='application/hpc/___includes___/modal/hpc/rename.html'
        )
        return http.JsonResponse(dict___data)


@decorators___application___security.___required___application___security___user___is_ldapuser_or_ldapuserimported___(___application___security___from___module___=utils___application___security.___APPLICATION___SECURITY___FROM___MODULE___HPC___)
def ___view___download___(request):
    instance = request.___APPLICATION___SECURITY___USER___
    path = request.GET.get('path', None)
    name = request.GET.get('name', None)
    ftype = request.GET.get('type', None)
    full_path = path + '/' + name
    relative_path = "/".join(full_path.split('/')[4:])
    if ftype == 'directory':
        compress_file = '/tmp/%s%s.tar.gz' % (name, str(datetime.now()))
        ssh.ssh_exec(instance.group_identifier(), instance.private_key.path, 'tar -zcvf "%s" "%s"' % (compress_file, relative_path))
        relative_path = compress_file
    with TemporaryFile() as f:
        result = ssh.ssh_sftp_getfo(instance.group_identifier(), instance.private_key.path, relative_path, f)
        if isinstance(result, tuple):
            return HttpResponse()
        f.seek(0)
        response = HttpResponse(f.read())
    if ftype == 'directory':
        ssh.ssh_exec(instance.group_identifier(), instance.private_key.path, 'rm "%s"' % relative_path)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Description'] = 'File Transfer'
    response['Content-Encoding'] = 'binary'
    response['Content-Disposition'] = 'attachment; filename="{}"'.format(relative_path.split('/')[-1])
    response['Expires'] = 0
    response['Cache-Control'] = 'must-revalidate'
    response['Pragma'] = 'public'
    return response


@decorators___application___security.___required___request_is_ajax___()
@decorators___application___security.___required___application___security___user___is_ldapuser_or_ldapuserimported___(___application___security___from___module___=utils___application___security.___APPLICATION___SECURITY___FROM___MODULE___HPC___)
def ___view___paste___(request):
    dict___data = dict()
    dict___data['___BOOLEAN___ERROR___'] = False
    if request.method == 'POST':
        from_path = request.POST.get('from', None)
        to_path = request.POST.get('to', None)
        files_to_copy = request.POST.getlist('filesToCopy[]', None)
        parameters = [to_path, from_path]
        for file in files_to_copy:
            parameters.append(file)
        data = linux.generate_data_dict(request, option='paste', dict___data=dict___data, parameters=parameters)
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
def ___view___execute___(request):
    instance = request.___APPLICATION___SECURITY___USER___
    dict___data = dict()
    dict___data['___BOOLEAN___ERROR___'] = False
    if request.method == 'POST':
        values = request.POST.getlist('values[]')
        error, message = ssh.ssh_exec(username=instance.group_identifier(), private_key_path=instance.private_key.path, command='sbatch "' + values[0] + '/' + values[1] + '"')
        if error:
            messages.add_message(request, messages.ERROR, message)
            dict___data['___BOOLEAN___ERROR___'] = True
        else:
            messages.add_message(request, messages.SUCCESS, _('HPC___EXPLORER___MESSAGES___ExecuteOk'))
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


@decorators___application___security.___required___request_is_ajax___()
@decorators___application___security.___required___application___security___user___is_ldapuser_or_ldapuserimported___(___application___security___from___module___=utils___application___security.___APPLICATION___SECURITY___FROM___MODULE___HPC___)
def ___view___delete___(request):
    dict___data = dict()
    dict___data['___BOOLEAN___ERROR___'] = False
    if request.method == 'POST':
        values = request.POST.getlist('values[]', None)
        data = linux.generate_data_dict(request, option='delete', dict___data=dict___data, parameters=values)
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
    else:
        dict___data['___HTML___APPLICATION___HPC___MODAL___'] = utils___hpc.___html___template___(
            request=request,
            context=dict(),
            template_name='application/hpc/___includes___/modal/hpc/delete.html'
        )
        return http.JsonResponse(dict___data)


@decorators___application___security.___required___request_is_ajax___()
@decorators___application___security.___required___application___security___user___is_ldapuser_or_ldapuserimported___(___application___security___from___module___=utils___application___security.___APPLICATION___SECURITY___FROM___MODULE___HPC___)
def ___view___go_to___(request):
    dict___data = dict()
    dict___data['___BOOLEAN___ERROR___'] = False
    dict___data['___HTML___APPLICATION___HPC___MODAL___'] = utils___hpc.___html___template___(
        request=request,
        context=dict(),
        template_name='application/hpc/___includes___/modal/hpc/goto.html'
    )
    return http.JsonResponse(dict___data)


@decorators___application___security.___required___request_is_ajax___()
@decorators___application___security.___required___application___security___user___is_ldapuser_or_ldapuserimported___(___application___security___from___module___=utils___application___security.___APPLICATION___SECURITY___FROM___MODULE___HPC___)
def ___view___create_folder___(request):
    dict___data = dict()
    dict___data['___BOOLEAN___ERROR___'] = False
    if request.method == 'POST':
        path = request.POST.get('path', None)
        name = request.POST.get('generic', None)
        data = linux.generate_data_dict(request, option='folder', dict___data=dict___data, parameters=[path, name])
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
        dict___data['___HTML___APPLICATION___HPC___MODAL___'] = utils___hpc.___html___template___(
            request=request,
            context={
                'form': forms.GenericForm(option='folder')
            },
            template_name='application/hpc/___includes___/modal/hpc/folder.html'
        )
        return http.JsonResponse(dict___data)


@decorators___application___security.___required___request_is_ajax___()
@decorators___application___security.___required___application___security___user___is_ldapuser_or_ldapuserimported___(___application___security___from___module___=utils___application___security.___APPLICATION___SECURITY___FROM___MODULE___HPC___)
def ___view___create_file___(request):
    dict___data = dict()
    dict___data['___BOOLEAN___ERROR___'] = False
    if request.method == 'POST':
        path = request.POST.get('path', None)
        name = request.POST.get('generic', None)
        data = linux.generate_data_dict(request, option='file', dict___data=dict___data, parameters=[path, name])
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
        dict___data['___HTML___APPLICATION___HPC___MODAL___'] = utils___hpc.___html___template___(
            request=request,
            context={
                'form': forms.GenericForm(option='file')
            },
            template_name='application/hpc/___includes___/modal/hpc/file.html'
        )
        return http.JsonResponse(dict___data)


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
                result = ssh.ssh_sftp_putfo(instance.group_identifier(), instance.private_key.path, file, path + '/' + file.name)
                if isinstance(result, tuple):
                    messages.add_message(request, messages.ERROR, result[1])
                    dict___data['___BOOLEAN___ERROR___'] = True
                    dict___data['___HTML___APPLICATION___HPC___MODAL___'] = utils___hpc.___html___template_modal___message___(request=request)
                    dict___data['___HTML___APPLICATION___HPC___MODAL___MESSAGE___'] = utils___hpc.___html___template_message___(request=request)
            data = linux.generate_data_dict(request, option='list', dict___data=dict___data, parameters=[path])
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


@decorators___application___security.___required___request_is_ajax___()
@decorators___application___security.___required___application___security___user___is_ldapuser_or_ldapuserimported___(___application___security___from___module___=utils___application___security.___APPLICATION___SECURITY___FROM___MODULE___HPC___)
def ___view___error___(request):
    message = request.GET.get('message')
    messages.add_message(request, messages.ERROR, message)
    return utils___hpc.___httpresponse___error___(request)
