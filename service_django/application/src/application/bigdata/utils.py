# -*- coding: utf-8 -*-
from django.contrib import messages
from django.template import loader


def ___html___template___(request, context, template_name):
    return loader.render_to_string(
        template_name=template_name,
        context=context,
        request=request
    )


def ___html___template_message___(request):
    return loader.render_to_string(
        template_name='application/bigdata/___includes___/modal/___includes___/message/message.html',
        context={
            'ctx___messages': messages.get_messages(request=request),
        },
        request=request
    )


def ___html___template_modal___message___(request):
    return loader.render_to_string(
        template_name='application/bigdata/___includes___/modal/message/message.html',
        context={
            'ctx___messages': messages.get_messages(request=request),
        },
        request=request
    )
