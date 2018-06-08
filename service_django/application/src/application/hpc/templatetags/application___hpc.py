# -*- coding: utf-8 -*-
from django import template

register = template.Library()


@register.filter()
def ___data_background___(state):
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
        return 'red'
    if state == 'RUNNING':
        return 'blue'
    if state == 'SUSPENDED':
        return 'darker'
    if state == 'CANCELLED':
        return 'orange'
    if state == 'COMPLETING':
        return 'purple'
    if state == 'COMPLETED':
        return 'green'
    if state == 'FAILED':
        return 'red'
    if state == 'TIMEOUT':
        return 'red'
    if state == 'NODE_FAIL':
        return 'red'
    return ''


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
