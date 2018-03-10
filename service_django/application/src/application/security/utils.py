# -*- coding: utf-8 -*-
from . import forms, ldap, models, tasks
from django import http
from django.conf import settings
from django.contrib import messages
from django.core import urlresolvers
from django.template import loader
from django.utils import translation
from django.utils.translation import ugettext_lazy as _
import copy

# Security from module
___APPLICATION___SECURITY___FROM___MODULE___WEBSITE___ = 'website'
___APPLICATION___SECURITY___FROM___MODULE___HPC___ = 'hpc'
___APPLICATION___SECURITY___FROM___MODULE___BIGDATA___ = 'bigdata'
___APPLICATION___SECURITY___FROM___MODULE___ADMINISTRATION___ = 'administration'
# Sessions ___APPLICATION___SECURITY___USER___MODEL___
___APPLICATION___SECURITY___USER___MODEL___LOCALUSER___ = 'localuser'
___APPLICATION___SECURITY___USER___MODEL___LOCALUSER___TEXT___ = 'LOCAL'
___APPLICATION___SECURITY___USER___MODEL___LDAPUSER___ = 'ldapuser'
___APPLICATION___SECURITY___USER___MODEL___LDAPUSER___TEXT___ = 'LDAP'
___APPLICATION___SECURITY___USER___MODEL___LDAPUSERIMPORTED___ = 'ldapuserimported'
___APPLICATION___SECURITY___USER___MODEL___LDAPUSERIMPORTED___TEXT___ = 'LDAPIMPORTED'
# It is the URL where the user should go, either because of an error or when sawing his session.
___APPLICATION___SECURITY___USER___URL_REVERSE___ = 'application'


def ___html___template___(request, context, template_name):
    return loader.render_to_string(
        template_name=template_name,
        context=context,
        request=request
    )


def ___html___template_message___(request, ___application___security___from___module___):
    return loader.render_to_string(
        template_name='application/%s/___includes___/modal/___includes___/message/message.html' % (___application___security___from___module___,),
        context={
            'ctx___messages': messages.get_messages(request=request),
        },
        request=request
    )


def ___html___template_modal___login___(request, ___application___security___from___module___, tab___localuserlogin, tab___ldapuserlogin, form___localuserlogin, form___ldapuserlogin):
    return loader.render_to_string(
        template_name='application/%s/___includes___/modal/security/login.html' % (___application___security___from___module___,),
        context={
            'ctx___tab___localuserlogin': tab___localuserlogin,
            'ctx___tab___ldapuserlogin': tab___ldapuserlogin,
            'ctx___form___localuserlogin': form___localuserlogin,
            'ctx___form___ldapuserlogin': form___ldapuserlogin,
        },
        request=request
    )


def ___html___template_modal___login___forgot_credentials_1___(request, ___application___security___from___module___, tab___localuserlogin___forgot_credentials, tab___ldapuserlogin___forgot_credentials, form):
    return loader.render_to_string(
        template_name='application/%s/___includes___/modal/security/login___forgot_credentials_1.html' % (___application___security___from___module___,),
        context={
            'ctx___tab___localuserlogin___forgot_credentials': tab___localuserlogin___forgot_credentials,
            'ctx___tab___ldapuserlogin___forgot_credentials': tab___ldapuserlogin___forgot_credentials,
            'ctx___form': form,
        },
        request=request
    )


def ___html___template_modal___login___forgot_credentials_2___(request, ___application___security___from___module___, tab___localuserlogin___forgot_credentials, tab___ldapuserlogin___forgot_credentials, form):
    return loader.render_to_string(
        template_name='application/%s/___includes___/modal/security/login___forgot_credentials_2.html' % (___application___security___from___module___,),
        context={
            'ctx___tab___localuserlogin___forgot_credentials': tab___localuserlogin___forgot_credentials,
            'ctx___tab___ldapuserlogin___forgot_credentials': tab___ldapuserlogin___forgot_credentials,
            'ctx___form': form,
        },
        request=request
    )


def ___html___template_modal___login___forgot_credentials_3___(request, ___application___security___from___module___, tab___localuserlogin___forgot_credentials, tab___ldapuserlogin___forgot_credentials, form):
    return loader.render_to_string(
        template_name='application/%s/___includes___/modal/security/login___forgot_credentials_3.html' % (___application___security___from___module___,),
        context={
            'ctx___tab___localuserlogin___forgot_credentials': tab___localuserlogin___forgot_credentials,
            'ctx___tab___ldapuserlogin___forgot_credentials': tab___ldapuserlogin___forgot_credentials,
            'ctx___form': form,
        },
        request=request
    )


def ___html___template_modal___login___request___(request, ___application___security___from___module___, tab___localuserlogin___request, tab___ldapuserlogin___request, form):
    return loader.render_to_string(
        template_name='application/%s/___includes___/modal/security/login___request.html' % (___application___security___from___module___,),
        context={
            'ctx___tab___localuserlogin___request': tab___localuserlogin___request,
            'ctx___tab___ldapuserlogin___request': tab___ldapuserlogin___request,
            'ctx___form': form,
        },
        request=request
    )


def ___html___template_modal___logout___(request, ___application___security___from___module___):
    return loader.render_to_string(
        template_name='application/%s/___includes___/modal/security/logout.html' % (___application___security___from___module___,),
        context={
        },
        request=request
    )


def ___html___template_modal___profile___(request, ___application___security___from___module___, form):
    return loader.render_to_string(
        template_name='application/%s/___includes___/modal/security/profile.html' % (___application___security___from___module___,),
        context={
            'ctx___form': form,
        },
        request=request
    )


def ___html___template_modal___message___(request, ___application___security___from___module___):
    return loader.render_to_string(
        template_name='application/%s/___includes___/modal/message/message.html' % (___application___security___from___module___,),
        context={
            'ctx___messages': messages.get_messages(request=request),
        },
        request=request
    )


def ___dict_string___application___security___from___module___(request, ___application___security___from___module___):
    string___modal = ''
    string___modal___message = ''
    string___modal___modal = ''
    string___modal___modal___message = ''
    if ___application___security___from___module___ == ___APPLICATION___SECURITY___FROM___MODULE___WEBSITE___:
        string___modal = '___HTML___APPLICATION___WEBSITE___MODAL___'
        string___modal___message = '___HTML___APPLICATION___WEBSITE___MODAL___MESSAGE___'
        string___modal___modal = '___HTML___APPLICATION___WEBSITE___MODAL___MODAL___'
        string___modal___modal___message = '___HTML___APPLICATION___WEBSITE___MODAL___MODAL___MESSAGE___'
    if ___application___security___from___module___ == ___APPLICATION___SECURITY___FROM___MODULE___HPC___:
        string___modal = '___HTML___APPLICATION___HPC___MODAL___'
        string___modal___message = '___HTML___APPLICATION___HPC___MODAL___MESSAGE___'
        string___modal___modal = '___HTML___APPLICATION___HPC___MODAL___MODAL___'
        string___modal___modal___message = '___HTML___APPLICATION___HPC___MODAL___MODAL___MESSAGE___'
    if ___application___security___from___module___ == ___APPLICATION___SECURITY___FROM___MODULE___BIGDATA___:
        string___modal = '___HTML___APPLICATION___BIGDATA___MODAL___'
        string___modal___message = '___HTML___APPLICATION___BIGDATA___MODAL___MESSAGE___'
        string___modal___modal = '___HTML___APPLICATION___BIGDATA___MODAL___MODAL___'
        string___modal___modal___message = '___HTML___APPLICATION___BIGDATA___MODAL___MODAL___MESSAGE___'
    if ___application___security___from___module___ == ___APPLICATION___SECURITY___FROM___MODULE___ADMINISTRATION___:
        string___modal = '___HTML___APPLICATION___ADMINISTRATION___MODAL___'
        string___modal___message = '___HTML___APPLICATION___ADMINISTRATION___MODAL___MESSAGE___'
        string___modal___modal = '___HTML___APPLICATION___ADMINISTRATION___MODAL___MODAL___'
        string___modal___modal___message = '___HTML___APPLICATION___ADMINISTRATION___MODAL___MODAL___MESSAGE___'
    dict___response = {
        'string___modal': string___modal,
        'string___modal___message': string___modal___message,
        'string___modal___modal': string___modal___modal,
        'string___modal___modal___message': string___modal___modal___message,
    }
    return dict___response


def ___jsonresponse___error___(request, ___application___security___from___module___):
    dict___data = dict()
    dict___data['___BOOLEAN___ERROR___'] = True
    #
    dict_string___application___security___from___module = ___dict_string___application___security___from___module___(request=request, ___application___security___from___module___=___application___security___from___module___)
    string___modal = dict_string___application___security___from___module['string___modal']
    string___modal___message = dict_string___application___security___from___module['string___modal___message']
    string___modal___modal = dict_string___application___security___from___module['string___modal___modal']
    string___modal___modal___message = dict_string___application___security___from___module['string___modal___modal___message']
    dict___data[string___modal] = ___html___template_modal___message___(request=request, ___application___security___from___module___=___application___security___from___module___)
    dict___data[string___modal___message] = ___html___template_message___(request=request, ___application___security___from___module___=___application___security___from___module___)
    dict___data[string___modal___modal] = ___html___template_modal___message___(request=request, ___application___security___from___module___=___application___security___from___module___)
    dict___data[string___modal___modal___message] = ___html___template_message___(request=request, ___application___security___from___module___=___application___security___from___module___)
    return http.JsonResponse(dict___data)


def ___jsonresponse___login___(request, ___application___security___from___module___):
    dict___data = dict()
    dict___data['___BOOLEAN___ERROR___'] = False
    if request.___APPLICATION___SECURITY___USER___ is not None:
        messages.add_message(request, messages.ERROR, _('APPLICATION___SECURITY___MESSAGE ERROR.'))
        return ___jsonresponse___error___(request=request, ___application___security___from___module___=___application___security___from___module___)
    if request.GET.get('tab___localuserlogin'):
        tab___localuserlogin = True
        tab___ldapuserlogin = False
    elif request.GET.get('tab___ldapuserlogin'):
        tab___localuserlogin = False
        tab___ldapuserlogin = True
    else:
        # default
        tab___localuserlogin = False
        tab___ldapuserlogin = True
    # 0: initial
    # 1: login is ok
    # 2: login is not ok
    # 3: login is ok, but user.is_active=False
    dict___data['___INT___IS_VALID_FORM___'] = 0
    instance = None
    form___localuserlogin = forms.LOCALUserLogin(data=None, request=request)
    form___ldapuserlogin = forms.LDAPUserLogin(data=None, request=request)
    if request.method == 'POST':
        dict___data['___BOOLEAN___IS_METHOD_POST___'] = True
        if tab___localuserlogin is True:
            form___localuserlogin = forms.LOCALUserLogin(data=request.POST or None, request=request)
            form = form___localuserlogin
        elif tab___ldapuserlogin is True:
            form___ldapuserlogin = forms.LDAPUserLogin(data=request.POST or None, request=request)
            form = form___ldapuserlogin
        else:
            messages.add_message(request, messages.ERROR, _('APPLICATION___SECURITY___MESSAGE ERROR.'))
            return ___jsonresponse___error___(request=request, ___application___security___from___module___=___application___security___from___module___)
        if form.is_valid():
            if tab___localuserlogin is True:
                identifier = form.cleaned_data.get('local_identifier')
                password = form.cleaned_data.get('local_password')
                model = models.LOCALUser
                ___application___security___user___model___ = ___APPLICATION___SECURITY___USER___MODEL___LOCALUSER___
                instance = model.objects.___instance___by_identifier___(identifier=identifier)
            elif tab___ldapuserlogin is True:
                identifier = form.cleaned_data.get('ldap_identifier')
                password = form.cleaned_data.get('ldap_password')
                ldap_group = form.cleaned_data.get('ldap_group')
                if ldap_group == settings.LDAP_SERVER_GROUPS_GROUP_CN:
                    model = models.LDAPUser
                    ___application___security___user___model___ = ___APPLICATION___SECURITY___USER___MODEL___LDAPUSER___
                    instance = model.objects.___instance___by_identifier___(identifier=identifier)
                else:
                    model = models.LDAPUserImported
                    ___application___security___user___model___ = ___APPLICATION___SECURITY___USER___MODEL___LDAPUSERIMPORTED___
                    instance = model.objects.___instance___by_ldap_group_and_identifier___(ldap_group=ldap_group, identifier=identifier)
            else:
                messages.add_message(request, messages.ERROR, _('APPLICATION___SECURITY___MESSAGE ERROR.'))
                return ___jsonresponse___error___(request=request, ___application___security___from___module___=___application___security___from___module___)
            if instance is not None and instance.___boolean___verify_password___(password=password):
                if instance.is_active or instance.is_superuser:
                    request.session['___APPLICATION___SECURITY___USER___MODEL___'] = ___application___security___user___model___
                    request.session['___APPLICATION___SECURITY___USER___PK___'] = instance.pk
                    request.___APPLICATION___SECURITY___USER___ = instance
                    boolean___error = True
                    for language in settings.LANGUAGES:
                        if instance.locale != '' and instance.locale in language[0]:
                            translation.activate(instance.locale)
                            request.session[translation.LANGUAGE_SESSION_KEY] = instance.locale
                            boolean___error = False
                            break
                    if boolean___error is True:
                        instance.locale = request.LANGUAGE_CODE
                        instance.save()
                    dict___data['___INT___IS_VALID_FORM___'] = 1
                else:
                    dict___data['___INT___IS_VALID_FORM___'] = 3
            else:
                dict___data['___INT___IS_VALID_FORM___'] = 2
        else:
            dict___data['___INT___IS_VALID_FORM___'] = 2
    else:
        dict___data['___BOOLEAN___IS_METHOD_POST___'] = False
    #
    dict_string___application___security___from___module = ___dict_string___application___security___from___module___(request=request, ___application___security___from___module___=___application___security___from___module___)
    string___modal = dict_string___application___security___from___module['string___modal']
    string___modal___message = dict_string___application___security___from___module['string___modal___message']
    if dict___data['___BOOLEAN___IS_METHOD_POST___']:
        if dict___data['___INT___IS_VALID_FORM___'] == 1:
            messages.add_message(request, messages.SUCCESS, _('APPLICATION___SECURITY___LOGIN___MESSAGE Welcome %(instance)s.') % {'instance': instance, })
            dict___data[string___modal] = ___html___template_modal___message___(request=request, ___application___security___from___module___=___application___security___from___module___)
            dict___data[string___modal___message] = ___html___template_message___(request=request, ___application___security___from___module___=___application___security___from___module___)
            return http.JsonResponse(dict___data)
        if dict___data['___INT___IS_VALID_FORM___'] == 2:
            messages.add_message(request, messages.ERROR, _('APPLICATION___SECURITY___LOGIN___MESSAGE The identifier and password are incorrect.'))
        elif dict___data['___INT___IS_VALID_FORM___'] == 3:
            messages.add_message(request, messages.WARNING, _('APPLICATION___SECURITY___LOGIN___MESSAGE The identifier and password are correct, but this user is not active.'))
        dict___data[string___modal] = ___html___template_modal___login___(request=request, ___application___security___from___module___=___application___security___from___module___, tab___localuserlogin=tab___localuserlogin, tab___ldapuserlogin=tab___ldapuserlogin, form___localuserlogin=form___localuserlogin, form___ldapuserlogin=form___ldapuserlogin)
        dict___data[string___modal___message] = ___html___template_message___(request=request, ___application___security___from___module___=___application___security___from___module___)
    else:
        dict___data[string___modal] = ___html___template_modal___login___(request=request, ___application___security___from___module___=___application___security___from___module___, tab___localuserlogin=tab___localuserlogin, tab___ldapuserlogin=tab___ldapuserlogin, form___localuserlogin=form___localuserlogin, form___ldapuserlogin=form___ldapuserlogin)
    return http.JsonResponse(dict___data)


def ___jsonresponse___login___forgot_credentials_1___(request, ___application___security___from___module___):
    tasks.___task___application___security___login___forgot_credentials___delete_instances___()
    dict___data = dict()
    dict___data['___BOOLEAN___ERROR___'] = False
    if request.___APPLICATION___SECURITY___USER___ is not None:
        messages.add_message(request, messages.ERROR, _('APPLICATION___SECURITY___MESSAGE ERROR.'))
        return ___jsonresponse___error___(request=request, ___application___security___from___module___=___application___security___from___module___)
    if request.GET.get('tab___localuserlogin___forgot_credentials'):
        tab___localuserlogin___forgot_credentials = True
        tab___ldapuserlogin___forgot_credentials = False
        formuserloginforgotcredentials1 = forms.LOCALUserLoginForgotCredentials1
        formuserloginforgotcredentials2 = forms.LOCALUserLoginForgotCredentials2
    elif request.GET.get('tab___ldapuserlogin___forgot_credentials'):
        tab___localuserlogin___forgot_credentials = False
        tab___ldapuserlogin___forgot_credentials = True
        formuserloginforgotcredentials1 = forms.LDAPUserLoginForgotCredentials1
        formuserloginforgotcredentials2 = forms.LDAPUserLoginForgotCredentials2
    else:
        messages.add_message(request, messages.ERROR, _('APPLICATION___SECURITY___MESSAGE ERROR.'))
        return ___jsonresponse___error___(request=request, ___application___security___from___module___=___application___security___from___module___)
    #
    instance = None
    form = formuserloginforgotcredentials1(data=request.POST or None, request=request)
    #
    if request.method == 'POST':
        dict___data['___BOOLEAN___IS_METHOD_POST___'] = True
        if form.is_valid():
            instance = form.save(commit=True)
            # Send mail with the verification code to the user who forgot their credentials.
            tasks.___task___application___security___login___forgot_credentials_1___send_mail___.apply_async(
                args=[],
                kwargs={
                    'string___email': instance.email,
                    'string___code': instance.code,
                },
                serializer='json'
            )
            messages.add_message(request, messages.SUCCESS, _('APPLICATION___SECURITY___LOGIN___FORGOT_CREDENTIALS___MESSAGE An email has been sent to %(email)s with a verification code that will be entered in the field called code confirmation.') % {'email': instance.email, })
            messages.add_message(request, messages.INFO, _('APPLICATION___SECURITY___LOGIN___FORGOT_CREDENTIALS___MESSAGE This window should not close and only works %(minutes_max)s minutes after sending the confirmation code to your email address.') % {'minutes_max': instance.___INT___MAXIMUM_TIME_OF_EXISTENCE___, })
            dict___data['___BOOLEAN___IS_VALID_FORM___'] = True
        else:
            dict___data['___BOOLEAN___IS_VALID_FORM___'] = False
    else:
        dict___data['___BOOLEAN___IS_METHOD_POST___'] = False
    #
    dict_string___application___security___from___module = ___dict_string___application___security___from___module___(request=request, ___application___security___from___module___=___application___security___from___module___)
    string___modal___modal = dict_string___application___security___from___module['string___modal___modal']
    string___modal___modal___message = dict_string___application___security___from___module['string___modal___modal___message']
    if dict___data['___BOOLEAN___IS_METHOD_POST___'] is True:
        if dict___data['___BOOLEAN___IS_VALID_FORM___'] is True:
            form = formuserloginforgotcredentials2(data=None, request=request, instance=instance)
            dict___data[string___modal___modal] = ___html___template_modal___login___forgot_credentials_2___(request=request, ___application___security___from___module___=___application___security___from___module___, tab___localuserlogin___forgot_credentials=tab___localuserlogin___forgot_credentials, tab___ldapuserlogin___forgot_credentials=tab___ldapuserlogin___forgot_credentials, form=form)
            dict___data[string___modal___modal___message] = ___html___template_message___(request=request, ___application___security___from___module___=___application___security___from___module___)
        else:
            dict___data[string___modal___modal] = ___html___template_modal___login___forgot_credentials_1___(request=request, ___application___security___from___module___=___application___security___from___module___, tab___localuserlogin___forgot_credentials=tab___localuserlogin___forgot_credentials, tab___ldapuserlogin___forgot_credentials=tab___ldapuserlogin___forgot_credentials, form=form)
    else:
        dict___data[string___modal___modal] = ___html___template_modal___login___forgot_credentials_1___(request=request, ___application___security___from___module___=___application___security___from___module___, tab___localuserlogin___forgot_credentials=tab___localuserlogin___forgot_credentials, tab___ldapuserlogin___forgot_credentials=tab___ldapuserlogin___forgot_credentials, form=form)
    return http.JsonResponse(dict___data)


def ___jsonresponse___login___forgot_credentials_2___(request, ___application___security___from___module___, pk):
    tasks.___task___application___security___login___forgot_credentials___delete_instances___()
    dict___data = dict()
    dict___data['___BOOLEAN___ERROR___'] = False
    if request.___APPLICATION___SECURITY___USER___ is not None:
        messages.add_message(request, messages.ERROR, _('APPLICATION___SECURITY___MESSAGE ERROR.'))
        return ___jsonresponse___error___(request=request, ___application___security___from___module___=___application___security___from___module___)
    try:
        pk = int(pk)
    except ValueError:
        messages.add_message(request, messages.ERROR, _('APPLICATION___SECURITY___MESSAGE ERROR.'))
        return ___jsonresponse___error___(request=request, ___application___security___from___module___=___application___security___from___module___)
    if request.GET.get('tab___localuserlogin___forgot_credentials'):
        tab___localuserlogin___forgot_credentials = True
        tab___ldapuserlogin___forgot_credentials = False
        model = models.LOCALUserForgotCredentials
        model_mirror = models.LOCALUser
        formuserloginforgotcredentials2 = forms.LOCALUserLoginForgotCredentials2
        formuserloginforgotcredentials3 = forms.LOCALUserLoginForgotCredentials3
    elif request.GET.get('tab___ldapuserlogin___forgot_credentials'):
        tab___localuserlogin___forgot_credentials = False
        tab___ldapuserlogin___forgot_credentials = True
        model = models.LDAPUserForgotCredentials
        model_mirror = models.LDAPUser
        formuserloginforgotcredentials2 = forms.LDAPUserLoginForgotCredentials2
        formuserloginforgotcredentials3 = forms.LDAPUserLoginForgotCredentials3
    else:
        messages.add_message(request, messages.ERROR, _('APPLICATION___SECURITY___MESSAGE ERROR.'))
        return ___jsonresponse___error___(request=request, ___application___security___from___module___=___application___security___from___module___)
    #
    instance = model.objects.___instance___by_pk___(pk=pk)
    if instance is None:
        messages.add_message(request, messages.ERROR, _('APPLICATION___SECURITY___MESSAGE ERROR.'))
        return ___jsonresponse___error___(request=request, ___application___security___from___module___=___application___security___from___module___)
    instance_mirror = model_mirror.objects.___instance___by_email___(email=instance.email)
    if instance_mirror is None:
        messages.add_message(request, messages.ERROR, _('APPLICATION___SECURITY___MESSAGE ERROR.'))
        return ___jsonresponse___error___(request=request, ___application___security___from___module___=___application___security___from___module___)
    form = formuserloginforgotcredentials2(data=request.POST or None, request=request, instance=instance)
    #
    if request.method == 'POST':
        dict___data['___BOOLEAN___IS_METHOD_POST___'] = True
        if form.is_valid():
            messages.add_message(request, messages.SUCCESS, _('APPLICATION___SECURITY___LOGIN___FORGOT_CREDENTIALS___MESSAGE Now you can change your password to access the application.'))
            minutes = instance.___int___time_of_existence___()
            minutes_max = instance.___INT___MAXIMUM_TIME_OF_EXISTENCE___
            if minutes_max < minutes:
                minutes = minutes_max
            messages.add_message(request, messages.INFO, _('APPLICATION___SECURITY___LOGIN___FORGOT_CREDENTIALS___MESSAGE This window should not close and only works %(minutes_max)s minutes after sending the confirmation code to your email address that was %(minutes)s minutes ago.') % {'minutes_max': minutes_max, 'minutes': minutes, })
            dict___data['___BOOLEAN___IS_VALID_FORM___'] = True
        else:
            dict___data['___BOOLEAN___IS_VALID_FORM___'] = False
    else:
        messages.add_message(request, messages.SUCCESS, _('APPLICATION___SECURITY___LOGIN___FORGOT_CREDENTIALS___MESSAGE An email has been sent to %(email)s with a verification code that will be entered in the field called code confirmation.') % {'email': instance.email, })
        minutes = instance.___int___time_of_existence___()
        minutes_max = instance.___INT___MAXIMUM_TIME_OF_EXISTENCE___
        if minutes_max < minutes:
            minutes = minutes_max
        messages.add_message(request, messages.INFO, _('APPLICATION___SECURITY___LOGIN___FORGOT_CREDENTIALS___MESSAGE This window should not close and only works %(minutes_max)s minutes after sending the confirmation code to your email address that was %(minutes)s minutes ago.') % {'minutes_max': minutes_max, 'minutes': minutes, })
        dict___data['___BOOLEAN___IS_METHOD_POST___'] = False
    #
    dict_string___application___security___from___module = ___dict_string___application___security___from___module___(request=request, ___application___security___from___module___=___application___security___from___module___)
    string___modal___modal = dict_string___application___security___from___module['string___modal___modal']
    string___modal___modal___message = dict_string___application___security___from___module['string___modal___modal___message']
    if dict___data['___BOOLEAN___IS_METHOD_POST___'] is True:
        if dict___data['___BOOLEAN___IS_VALID_FORM___'] is True:
            form = formuserloginforgotcredentials3(data=None, request=request, instance=instance, instance_mirror=instance_mirror)
            dict___data[string___modal___modal] = ___html___template_modal___login___forgot_credentials_3___(request=request, ___application___security___from___module___=___application___security___from___module___, tab___localuserlogin___forgot_credentials=tab___localuserlogin___forgot_credentials, tab___ldapuserlogin___forgot_credentials=tab___ldapuserlogin___forgot_credentials, form=form)
            dict___data[string___modal___modal___message] = ___html___template_message___(request=request, ___application___security___from___module___=___application___security___from___module___)
        else:
            dict___data[string___modal___modal] = ___html___template_modal___login___forgot_credentials_2___(request=request, ___application___security___from___module___=___application___security___from___module___, tab___localuserlogin___forgot_credentials=tab___localuserlogin___forgot_credentials, tab___ldapuserlogin___forgot_credentials=tab___ldapuserlogin___forgot_credentials, form=form)
    else:
        dict___data[string___modal___modal] = ___html___template_modal___login___forgot_credentials_2___(request=request, ___application___security___from___module___=___application___security___from___module___, tab___localuserlogin___forgot_credentials=tab___localuserlogin___forgot_credentials, tab___ldapuserlogin___forgot_credentials=tab___ldapuserlogin___forgot_credentials, form=form)
        dict___data[string___modal___modal___message] = ___html___template_message___(request=request, ___application___security___from___module___=___application___security___from___module___)
    return http.JsonResponse(dict___data)


def ___jsonresponse___login___forgot_credentials_3___(request, ___application___security___from___module___, pk):
    tasks.___task___application___security___login___forgot_credentials___delete_instances___()
    dict___data = dict()
    dict___data['___BOOLEAN___ERROR___'] = False
    if request.___APPLICATION___SECURITY___USER___ is not None:
        messages.add_message(request, messages.ERROR, _('APPLICATION___SECURITY___MESSAGE ERROR.'))
        return ___jsonresponse___error___(request=request, ___application___security___from___module___=___application___security___from___module___)
    try:
        pk = int(pk)
    except ValueError:
        messages.add_message(request, messages.ERROR, _('APPLICATION___SECURITY___MESSAGE ERROR.'))
        return ___jsonresponse___error___(request=request, ___application___security___from___module___=___application___security___from___module___)
    if request.GET.get('tab___localuserlogin___forgot_credentials'):
        tab___localuserlogin___forgot_credentials = True
        tab___ldapuserlogin___forgot_credentials = False
        model = models.LOCALUserForgotCredentials
        model_mirror = models.LOCALUser
        formuserloginforgotcredentials3 = forms.LOCALUserLoginForgotCredentials3
    elif request.GET.get('tab___ldapuserlogin___forgot_credentials'):
        tab___localuserlogin___forgot_credentials = False
        tab___ldapuserlogin___forgot_credentials = True
        model = models.LDAPUserForgotCredentials
        model_mirror = models.LDAPUser
        formuserloginforgotcredentials3 = forms.LDAPUserLoginForgotCredentials3
    else:
        messages.add_message(request, messages.ERROR, _('APPLICATION___SECURITY___MESSAGE ERROR.'))
        return ___jsonresponse___error___(request=request, ___application___security___from___module___=___application___security___from___module___)
    #
    instance = model.objects.___instance___by_pk___(pk=pk)
    if instance is None:
        messages.add_message(request, messages.ERROR, _('APPLICATION___SECURITY___MESSAGE ERROR.'))
        return ___jsonresponse___error___(request=request, ___application___security___from___module___=___application___security___from___module___)
    instance_mirror = model_mirror.objects.___instance___by_email___(email=instance.email)
    if instance_mirror is None:
        messages.add_message(request, messages.ERROR, _('APPLICATION___SECURITY___MESSAGE ERROR.'))
        return ___jsonresponse___error___(request=request, ___application___security___from___module___=___application___security___from___module___)
    form = formuserloginforgotcredentials3(data=request.POST or None, request=request, instance=instance, instance_mirror=instance_mirror)
    #
    if request.method == 'POST':
        dict___data['___BOOLEAN___IS_METHOD_POST___'] = True
        if form.is_valid():
            instance = form.save(commit=True)
            instance.delete()
            messages.add_message(request, messages.SUCCESS, _('APPLICATION___SECURITY___LOGIN___FORGOT_CREDENTIALS___MESSAGE Try to access the application.'))
            dict___data['___BOOLEAN___IS_VALID_FORM___'] = True
        else:
            dict___data['___BOOLEAN___IS_VALID_FORM___'] = False
    else:
        messages.add_message(request, messages.SUCCESS, _('APPLICATION___SECURITY___LOGIN___FORGOT_CREDENTIALS___MESSAGE Now you can change your password to access the application.'))
        minutes = instance.___int___time_of_existence___()
        minutes_max = instance.___INT___MAXIMUM_TIME_OF_EXISTENCE___
        if minutes_max < minutes:
            minutes = minutes_max
        messages.add_message(request, messages.INFO, _('APPLICATION___SECURITY___LOGIN___FORGOT_CREDENTIALS___MESSAGE This window should not close and only works %(minutes_max)s minutes after sending the confirmation code to your email address that was %(minutes)s minutes ago.') % {'minutes_max': minutes_max, 'minutes': minutes, })
        dict___data['___BOOLEAN___IS_METHOD_POST___'] = False
    #
    dict_string___application___security___from___module = ___dict_string___application___security___from___module___(request=request, ___application___security___from___module___=___application___security___from___module___)
    string___modal___modal = dict_string___application___security___from___module['string___modal___modal']
    string___modal___modal___message = dict_string___application___security___from___module['string___modal___modal___message']
    if dict___data['___BOOLEAN___IS_METHOD_POST___'] is True:
        if dict___data['___BOOLEAN___IS_VALID_FORM___'] is True:
            dict___data[string___modal___modal] = ___html___template_modal___message___(request=request, ___application___security___from___module___=___application___security___from___module___)
            dict___data[string___modal___modal___message] = ___html___template_message___(request=request, ___application___security___from___module___=___application___security___from___module___)
        else:
            dict___data[string___modal___modal] = ___html___template_modal___login___forgot_credentials_3___(request=request, ___application___security___from___module___=___application___security___from___module___, tab___localuserlogin___forgot_credentials=tab___localuserlogin___forgot_credentials, tab___ldapuserlogin___forgot_credentials=tab___ldapuserlogin___forgot_credentials, form=form)
    else:
        dict___data[string___modal___modal] = ___html___template_modal___login___forgot_credentials_3___(request=request, ___application___security___from___module___=___application___security___from___module___, tab___localuserlogin___forgot_credentials=tab___localuserlogin___forgot_credentials, tab___ldapuserlogin___forgot_credentials=tab___ldapuserlogin___forgot_credentials, form=form)
        dict___data[string___modal___modal___message] = ___html___template_message___(request=request, ___application___security___from___module___=___application___security___from___module___)
    return http.JsonResponse(dict___data)


def ___jsonresponse___login___request___(request, ___application___security___from___module___):
    dict___data = dict()
    dict___data['___BOOLEAN___ERROR___'] = False
    if request.___APPLICATION___SECURITY___USER___ is not None:
        return ___jsonresponse___error___(request=request, ___application___security___from___module___=___application___security___from___module___)
    if request.GET.get('tab___localuserlogin___request'):
        tab___localuserlogin___request = True
        tab___ldapuserlogin___request = False
        form = forms.LOCALUserLoginRequest(data=request.POST or None, request=request)
        string___user_model = ___APPLICATION___SECURITY___USER___MODEL___LOCALUSER___TEXT___
        string___identifier = ''
    elif request.GET.get('tab___ldapuserlogin___request'):
        tab___localuserlogin___request = False
        tab___ldapuserlogin___request = True
        form = forms.LDAPUserLoginRequest(data=request.POST or None, request=request)
        string___user_model = ___APPLICATION___SECURITY___USER___MODEL___LDAPUSER___TEXT___
        string___identifier = '%s_' % (settings.LDAP_SERVER_GROUPS_GROUP_CN.lower(),)
    else:
        return ___jsonresponse___error___(request=request, ___application___security___from___module___=___application___security___from___module___)
    #
    if request.method == 'POST':
        dict___data['___BOOLEAN___IS_METHOD_POST___'] = True
        if form.is_valid():
            instance = form.save(commit=True)
            # Send mail to users who approve the request.
            # Send mail to the user who made the request.
            tasks.___task___application___security___login___request___send_mail___.apply_async(
                args=[],
                kwargs={
                    'string___user_model': string___user_model,
                    'string___first_name': instance.first_name,
                    'string___last_name': instance.last_name,
                    'string___identifier': '%s%s' % (string___identifier, instance.identifier,),
                    'string___email': instance.email,
                    'string___detail': instance.detail,
                },
                serializer='json'
            )
            messages.add_message(request, messages.SUCCESS, _('APPLICATION___SECURITY___LOGIN___REQUEST___MESSAGE The application administrators have received your request, you will receive an email informing you if it was accepted or canceled.'))
            dict___data['___BOOLEAN___IS_VALID_FORM___'] = True
        else:
            dict___data['___BOOLEAN___IS_VALID_FORM___'] = False
    else:
        dict___data['___BOOLEAN___IS_METHOD_POST___'] = False
    #
    dict_string___application___security___from___module = ___dict_string___application___security___from___module___(request=request, ___application___security___from___module___=___application___security___from___module___)
    string___modal___modal = dict_string___application___security___from___module['string___modal___modal']
    string___modal___modal___message = dict_string___application___security___from___module['string___modal___modal___message']
    if dict___data['___BOOLEAN___IS_METHOD_POST___'] is True:
        if dict___data['___BOOLEAN___IS_VALID_FORM___'] is True:
            dict___data[string___modal___modal] = ___html___template_modal___message___(request=request, ___application___security___from___module___=___application___security___from___module___)
            dict___data[string___modal___modal___message] = ___html___template_message___(request=request, ___application___security___from___module___=___application___security___from___module___)
        else:
            dict___data[string___modal___modal] = ___html___template_modal___login___request___(request=request, ___application___security___from___module___=___application___security___from___module___, tab___localuserlogin___request=tab___localuserlogin___request, tab___ldapuserlogin___request=tab___ldapuserlogin___request, form=form)
    else:
        dict___data[string___modal___modal] = ___html___template_modal___login___request___(request=request, ___application___security___from___module___=___application___security___from___module___, tab___localuserlogin___request=tab___localuserlogin___request, tab___ldapuserlogin___request=tab___ldapuserlogin___request, form=form)
    return http.JsonResponse(dict___data)


def ___jsonresponse___logout___(request, ___application___security___from___module___):
    dict___data = dict()
    dict___data['___BOOLEAN___ERROR___'] = False
    instance = request.___APPLICATION___SECURITY___USER___
    if instance is None:
        messages.add_message(request, messages.ERROR, _('APPLICATION___SECURITY___MESSAGE ERROR.'))
        return ___jsonresponse___error___(request=request, ___application___security___from___module___=___application___security___from___module___)
    if request.method == 'POST':
        dict___data['___BOOLEAN___IS_METHOD_POST___'] = True
        if request.session.get('___APPLICATION___SECURITY___USER___MODEL___'):
            del request.session['___APPLICATION___SECURITY___USER___MODEL___']
        if request.session.get('___APPLICATION___SECURITY___USER___PK___'):
            del request.session['___APPLICATION___SECURITY___USER___PK___']
        request.___APPLICATION___SECURITY___USER___ = None
        messages.add_message(request, messages.SUCCESS, _('APPLICATION___SECURITY___LOGOUT___MESSAGE %(instance)s your session was successfully closed.') % {'instance': instance, })
        dict___data['___APPLICATION___SECURITY___USER___WITHOUT_PERMISSION___'] = True
        dict___data['___APPLICATION___SECURITY___USER___URL_REDIRECT___'] = urlresolvers.reverse(___APPLICATION___SECURITY___USER___URL_REVERSE___)
    else:
        dict___data['___BOOLEAN___IS_METHOD_POST___'] = False
    #
    dict_string___application___security___from___module = ___dict_string___application___security___from___module___(request=request, ___application___security___from___module___=___application___security___from___module___)
    string___modal = dict_string___application___security___from___module['string___modal']
    string___modal___message = dict_string___application___security___from___module['string___modal___message']
    if dict___data['___BOOLEAN___IS_METHOD_POST___']:
        dict___data[string___modal] = ___html___template_modal___message___(request=request, ___application___security___from___module___=___application___security___from___module___)
        dict___data[string___modal___message] = ___html___template_message___(request=request, ___application___security___from___module___=___application___security___from___module___)
    else:
        dict___data[string___modal] = ___html___template_modal___logout___(request=request, ___application___security___from___module___=___application___security___from___module___)
    return http.JsonResponse(dict___data)


def ___jsonresponse___profile___(request, ___application___security___from___module___):
    dict___data = dict()
    dict___data['___BOOLEAN___ERROR___'] = False
    instance = request.___APPLICATION___SECURITY___USER___
    if instance is None:
        messages.add_message(request, messages.ERROR, _('APPLICATION___SECURITY___MESSAGE ERROR.'))
        return ___jsonresponse___error___(request=request, ___application___security___from___module___=___application___security___from___module___)
    instance_current = copy.deepcopy(instance)
    if isinstance(instance, models.LOCALUser):
        form = forms.LOCALUserProfile(data=request.POST or None, files=request.FILES or None, request=request, instance=instance, instance_current=instance_current)
    elif isinstance(instance, models.LDAPUser):
        ldap.___messages___action___is_there_connection___(request=request)
        form = forms.LDAPUserProfile(data=request.POST or None, files=request.FILES or None, request=request, instance=instance, instance_current=instance_current)
    elif isinstance(instance, models.LDAPUserImported):
        form = forms.LDAPUserImportedProfile(data=request.POST or None, files=request.FILES or None, request=request, instance=instance, instance_current=instance_current)
    else:
        messages.add_message(request, messages.ERROR, _('APPLICATION___SECURITY___MESSAGE ERROR.'))
        return ___jsonresponse___error___(request=request, ___application___security___from___module___=___application___security___from___module___)
    if request.method == 'POST':
        dict___data['___BOOLEAN___IS_METHOD_POST___'] = True
        if form is not None and form.is_valid():
            instance = form.save(commit=True)
            request.___APPLICATION___SECURITY___USER___ = instance
            messages.add_message(request, messages.SUCCESS, _('APPLICATION___SECURITY___PROFILE___MESSAGE %(instance)s your profile was successfully update.') % {'instance': instance, })
            dict___data['___BOOLEAN___IS_VALID_FORM___'] = True
        else:
            dict___data['___BOOLEAN___IS_VALID_FORM___'] = False
    else:
        dict___data['___BOOLEAN___IS_METHOD_POST___'] = False
    #
    dict_string___application___security___from___module = ___dict_string___application___security___from___module___(request=request, ___application___security___from___module___=___application___security___from___module___)
    string___modal = dict_string___application___security___from___module['string___modal']
    string___modal___message = dict_string___application___security___from___module['string___modal___message']
    dict___data[string___modal] = ___html___template_modal___profile___(request=request, ___application___security___from___module___=___application___security___from___module___, form=form)
    dict___data[string___modal___message] = ___html___template_message___(request=request, ___application___security___from___module___=___application___security___from___module___)
    return http.JsonResponse(dict___data)


def ___jsonresponse___locale___(request, ___application___security___from___module___):
    dict___data = dict()
    dict___data['___BOOLEAN___ERROR___'] = False
    if request.GET.get('locale'):
        boolean___is_valid = False
        for language in settings.LANGUAGES:
            if request.GET.get('locale') in language[0]:
                translation.activate(request.GET.get('locale'))
                request.session[translation.LANGUAGE_SESSION_KEY] = request.GET.get('locale')
                if request.___APPLICATION___SECURITY___USER___ is not None:
                    request.___APPLICATION___SECURITY___USER___.locale = request.GET.get('locale')
                    request.___APPLICATION___SECURITY___USER___.save()
                    messages.add_message(request, messages.SUCCESS, _('APPLICATION___SECURITY___LOCALE___MESSAGE %(instance)s the language of the application was successfully update.') % {'instance': request.___APPLICATION___SECURITY___USER___, })
                else:
                    messages.add_message(request, messages.SUCCESS, _('APPLICATION___SECURITY___LOCALE___MESSAGE The language of the application was successfully update.'))
                boolean___is_valid = True
                break
        if boolean___is_valid is False:
            dict___data['___BOOLEAN___ERROR___'] = True
    else:
        dict___data['___BOOLEAN___ERROR___'] = True
    if dict___data['___BOOLEAN___ERROR___'] is True:
        messages.add_message(request, messages.ERROR, _('APPLICATION___SECURITY___MESSAGE ERROR.'))
    #
    dict_string___application___security___from___module = ___dict_string___application___security___from___module___(request=request, ___application___security___from___module___=___application___security___from___module___)
    string___modal = dict_string___application___security___from___module['string___modal']
    string___modal___message = dict_string___application___security___from___module['string___modal___message']
    dict___data[string___modal] = ___html___template_modal___message___(request=request, ___application___security___from___module___=___application___security___from___module___)
    dict___data[string___modal___message] = ___html___template_message___(request=request, ___application___security___from___module___=___application___security___from___module___)
    return http.JsonResponse(dict___data)
