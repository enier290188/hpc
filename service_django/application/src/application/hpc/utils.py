# -*- coding: utf-8 -*-
from django import http
from django.contrib import messages
from django.template import loader
from django.utils.translation import ugettext_lazy as _
from django.core import urlresolvers
import json

___APPLICATION___HPC___JOBS___URL_REVERSE___ = 'application___hpc:modules:hpc_jobs:index'


def ___html___template___(request, context, template_name):
    return loader.render_to_string(
        template_name=template_name,
        context=context,
        request=request
    )


def ___html___template_message___(request):
    return loader.render_to_string(
        template_name='application/hpc/___includes___/modal/___includes___/message/message.html',
        context={
            'ctx___messages': messages.get_messages(request=request),
        },
        request=request
    )


def ___html___template_modal___message___(request):
    return loader.render_to_string(
        template_name='application/hpc/___includes___/modal/message/message.html',
        context={
            'ctx___messages': messages.get_messages(request=request),
        },
        request=request
    )


def ___httpresponse___error___(request):
    if len(messages.get_messages(request=request)) <= 0:
        messages.add_message(request, messages.ERROR, _('APPLICATION___HPC___SSH___MESSAGES_ServerNotAvailable'))
    dict___data = dict()
    dict___data['___BOOLEAN___ERROR___'] = True
    dict___data['___HTML___APPLICATION___HPC___MODAL___'] = ___html___template_modal___message___(request=request)
    dict___data['___HTML___APPLICATION___HPC___MODAL___MESSAGE___'] = ___html___template_message___(request=request)
    return http.HttpResponse(json.dumps(dict___data), content_type='application/json')


def ___jsonresponse___error___(request):
    if len(messages.get_messages(request=request)) <= 0:
        messages.add_message(request, messages.ERROR, _('APPLICATION___HPC___SSH___MESSAGES_ServerNotAvailable'))
    dict___data = dict()
    dict___data['___BOOLEAN___ERROR___'] = True
    dict___data['___HTML___APPLICATION___HPC___MODAL___'] = ___html___template_modal___message___(request=request)
    dict___data['___HTML___APPLICATION___HPC___MODAL___MESSAGE___'] = ___html___template_message___(request=request)
    return http.JsonResponse(dict___data)


def ___jsonresponse___success___modal(request):
    if len(messages.get_messages(request=request)) <= 0:
        messages.add_message(request, messages.SUCCESS, "El archivo se ha guardado satisfactoriamente")
    dict___data = dict()
    dict___data['___BOOLEAN___ERROR___'] = False
    dict___data['___HTML___APPLICATION___HPC___MODAL___'] = ___html___template_modal___message___(request=request)
    dict___data['___HTML___APPLICATION___HPC___MODAL___MESSAGE___'] = ___html___template_message___(request=request)
    return http.JsonResponse(dict___data)
