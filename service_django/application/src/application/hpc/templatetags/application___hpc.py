# -*- coding: utf-8 -*-
from django import template

register = template.Library()


@register.filter()
def ___get_label___(state):
    if state == 'PENDING':
        return "danger"
    if state == 'RUNNING':
        return "info"
    if state == 'SUSPENDED':
        return "warning"
    if state == 'CANCELLED':
        return "warning"
    if state == 'COMPLETING':
        return "primary"
    if state == 'COMPLETED':
        return "success"
    if state == 'COMPLETE':
        return "success"
    if state == 'CONFIGURING':
        return "info"
    if state == 'FAILED':
        return "danger"
    if state == 'TIMEOUT':
        return "danger"
    if state == 'PREEMPTED':
        return "warning"
    if state == 'NODE_FAIL':
        return "danger"
    if state == 'REVOKED':
        return "danger"
    if state == 'SPECIAL_EXIT':
        return "default"
    return "default"


@register.filter()
def ___disable_if_cant_requeue___(state):
    if state == 'RUNNING' or state == 'SUSPENDED' or state == 'COMPLETED' or state == 'FAILED':
        return
    else:
        return "disabled"
