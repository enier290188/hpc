# -*- coding: utf-8 -*-
from django import template

register = template.Library()


@register.filter()
def ___get_label___(state):
    """
    JOB STATE CODES
       Jobs typically pass through several states in the course of their exe-
       cution.   The typical states are PENDING, RUNNING, SUSPENDED, COMPLET-
       ING, and COMPLETED.  An explanation of each state follows.

       CA  CANCELLED       Job was explicitly cancelled by the user or system
                           administrator.   The  job may or may not have been
                           initiated.

       CD  COMPLETED       Job has terminated all processes on all nodes.

       CG  COMPLETING      Job is in the process  of  completing.  Some  pro-
                           cesses on some nodes may still be active.

       F   FAILED          Job  terminated  with  non-zero exit code or other
                           failure condition.

       NF  NODE_FAIL       Job terminated due to failure of one or more allo-
                           cated nodes.

       PD  PENDING         Job is awaiting resource allocation.

       R   RUNNING         Job currently has an allocation.

       S   SUSPENDED       Job has an allocation, but execution has been sus-
                           pended.

       TO  TIMEOUT         Job terminated upon reaching its time limit.
   """
    if state == 'PENDING':
        return 'danger'
    if state == 'RUNNING':
        return 'info'
    if state == 'SUSPENDED':
        return 'warning'
    if state == 'CANCELLED':
        return 'primary'
    if state == 'COMPLETING':
        return 'primary'
    if state == 'COMPLETED':
        return 'success'
    if state == 'FAILED':
        return 'danger'
    if state == 'TIMEOUT':
        return 'danger'
    if state == 'NODE_FAIL':
        return 'danger'
    return 'default'


@register.filter()
def ___disable_if_cant_requeue___(state):
    if state == 'RUNNING' or state == 'SUSPENDED' or state == 'COMPLETED' or state == 'FAILED':
        return
    else:
        return 'disabled'


@register.filter()
def ___disable_if_cant_cancelled___(state):
    if state == 'CANCELLED':
        return 'disabled'
    else:
        return
