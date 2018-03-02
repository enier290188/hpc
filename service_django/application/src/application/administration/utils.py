# -*- coding: utf-8 -*-
from django import http
from django.core import paginator
from django.contrib import messages
from django.template import loader
from django.utils.translation import ugettext_lazy as _
import copy

# Templates
___APPLICATION___ADMINISTRATION___TEMPLATE___INDEX___ = 'index'
___APPLICATION___ADMINISTRATION___TEMPLATE___LIST___ = 'list'
___APPLICATION___ADMINISTRATION___TEMPLATE___CREATE___ = 'create'
___APPLICATION___ADMINISTRATION___TEMPLATE___DETAIL___ = 'detail'
___APPLICATION___ADMINISTRATION___TEMPLATE___UPDATE___ = 'update'
___APPLICATION___ADMINISTRATION___TEMPLATE___DELETE___ = 'delete'
___APPLICATION___ADMINISTRATION___TEMPLATE___APPROVE___ = 'approve'
___APPLICATION___ADMINISTRATION___TEMPLATE___DISAPPROVE___ = 'disapprove'


def ___html___template___(request, context, template_name):
    return loader.render_to_string(
        template_name=template_name,
        context=context,
        request=request
    )


def ___html___template_message___(request):
    return loader.render_to_string(
        template_name='application/administration/___includes___/modal/___includes___/message/message.html',
        context={
            'ctx___messages': messages.get_messages(request=request),
        },
        request=request
    )


def ___html___template_index___table_tbody___(request, ___utils___module___, ___utils___module_model___, page):
    return loader.render_to_string(
        template_name='application/administration/___includes___/content/center/%s/%s/___includes___/%s.html' % (___utils___module___.___MODULE_PATH___, ___utils___module_model___.___MODEL_PATH___, ___APPLICATION___ADMINISTRATION___TEMPLATE___LIST___,),
        context={
            'ctx___page': page,
        },
        request=request
    )


def ___html___template_index___pagination___(request, ___utils___module___, ___utils___module_model___, page):
    search = request.GET.get('search')
    if search is not None:
        search = ' '.join(search.split())
    else:
        search = ''
    return loader.render_to_string(
        template_name='application/administration/___includes___/content/center/___includes___/pagination/pagination.html',
        context={
            'ctx___page': page,
            'ctx___data_url': 'application___administration:modules:%s:%s:list' % (___utils___module___.___MODULE_PATH___, ___utils___module_model___.___MODEL_PATH___,),
            'ctx___search': search
        },
        request=request
    )


def ___html___template_modal___(request, ___utils___module___, ___utils___module_model___, ___application___administration___template___, form):
    return loader.render_to_string(
        template_name='application/administration/___includes___/modal/%s/%s/%s.html' % (___utils___module___.___MODULE_PATH___, ___utils___module_model___.___MODEL_PATH___, ___application___administration___template___,),
        context={
            'ctx___form': form,
        },
        request=request
    )


def ___html___template_modal___message___(request):
    return loader.render_to_string(
        template_name='application/administration/___includes___/modal/message/message.html',
        context={
            'ctx___messages': messages.get_messages(request=request),
        },
        request=request
    )


def ___list_instance___search___(request, ___utils___module___, ___utils___module_model___):
    instances = ___utils___module_model___.___MODEL___.objects.___instances___(request=request)
    list_instance___search = instances
    search = request.GET.get('search')
    if search is not None:
        list_string___search = search.split()
        if list_string___search:
            list_instance___search = list()
            for instance in instances:
                boolean___add_instance = False
                for string___search in list_string___search:
                    temporal_string___search = string___search.lower()
                    temporal_string___instance = instance.__str__().lower()
                    if temporal_string___instance.find(temporal_string___search) >= 0 or temporal_string___search.find(temporal_string___instance) >= 0:
                        boolean___add_instance = True
                        break
                if boolean___add_instance is False and hasattr(instance, 'ldap_group'):
                    for string___search in list_string___search:
                        temporal_string___search = string___search.lower()
                        temporal_string___instance_ldap_group = instance.ldap_group.lower()
                        if temporal_string___instance_ldap_group.find(temporal_string___search) >= 0 or temporal_string___search.find(temporal_string___instance_ldap_group) >= 0:
                            boolean___add_instance = True
                            break
                if boolean___add_instance is False and hasattr(instance, 'identifier'):
                    for string___search in list_string___search:
                        temporal_string___search = string___search.lower()
                        temporal_string___instance_identifier = instance.identifier.lower()
                        if temporal_string___instance_identifier.find(temporal_string___search) >= 0 or temporal_string___search.find(temporal_string___instance_identifier) >= 0:
                            boolean___add_instance = True
                            break
                if boolean___add_instance is False and hasattr(instance, 'email'):
                    for string___search in list_string___search:
                        temporal_string___search = string___search.lower()
                        temporal_string___instance_email = instance.email.lower()
                        if temporal_string___instance_email.find(temporal_string___search) >= 0 or temporal_string___search.find(temporal_string___instance_email) >= 0:
                            boolean___add_instance = True
                            break
                # Este codigo debe estar al final de todas las condiciones
                if hasattr(instance, 'is_active'):
                    list_string___is_active = [_('APPLICATION___ADMINISTRATION___CONTENT___OPTION_YES').lower(), _('APPLICATION___ADMINISTRATION___CONTENT___OPTION_NO').lower()]
                    if instance.is_active:
                        string___is_active = list_string___is_active[0]
                    else:
                        string___is_active = list_string___is_active[1]
                    if list_string___search[-1].lower() in list_string___is_active:
                        if boolean___add_instance is True and list_string___search[-1].lower() == string___is_active:
                            boolean___add_instance = True
                        else:
                            if boolean___add_instance is True:
                                boolean___add_instance = False
                            else:
                                if len(list_string___search) == 1 and list_string___search[-1].lower() == string___is_active:
                                    boolean___add_instance = True
                                else:
                                    boolean___add_instance = False
                if boolean___add_instance is True:
                    list_instance___search.append(instance)
    return list_instance___search


def ___int___number_page___(request, ___utils___module___, ___utils___module_model___, list_instance___search, pk):
    int___position = 0
    for instance___search in list_instance___search:
        int___position += 1
        if instance___search.pk == pk:
            break
    if int___position <= ___utils___module_model___.___INT___PAGINATOR_AMOUNT_PER_PAGE___:
        int___number_page = 1
    else:
        int___number_page = int___position // ___utils___module_model___.___INT___PAGINATOR_AMOUNT_PER_PAGE___
        int___rest = int___position % ___utils___module_model___.___INT___PAGINATOR_AMOUNT_PER_PAGE___
        if int___rest > 0:
            int___number_page += 1
    return int___number_page


def ___instance___page___(request, ___utils___module___, ___utils___module_model___, list_instance___search, int___number_page):
    instance___paginator = paginator.Paginator(object_list=list_instance___search, per_page=___utils___module_model___.___INT___PAGINATOR_AMOUNT_PER_PAGE___)
    try:
        if int___number_page == 0:
            page = instance___paginator.page(number=request.GET.get('page'))
        else:
            page = instance___paginator.page(number=int___number_page)
    except paginator.PageNotAnInteger:
        # If page is not an integer, deliver first page.
        page = instance___paginator.page(number=1)
    except paginator.EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        page = instance___paginator.page(number=instance___paginator.num_pages)
    return page


def ___jsonresponse___error___(request):
    if len(messages.get_messages(request=request)) <= 0:
        messages.add_message(request, messages.ERROR, _('APPLICATION___SECURITY___MESSAGE ERROR.'))
    dict___data = dict()
    dict___data['___BOOLEAN___ERROR___'] = True
    dict___data['___HTML___APPLICATION___ADMINISTRATION___MODAL___'] = ___html___template_modal___message___(request=request)
    dict___data['___HTML___APPLICATION___ADMINISTRATION___MODAL___MESSAGE___'] = ___html___template_message___(request=request)
    return http.JsonResponse(dict___data)


def ___jsonresponse___index___(request, ___utils___module___, ___utils___module_model___):
    dict___data = dict()
    dict___data['___BOOLEAN___ERROR___'] = False
    dict___data['___HTML___APPLICATION___ADMINISTRATION___CONTENT___CENTER___'] = ___html___template___(
        request=request,
        context=dict(),
        template_name='application/administration/___includes___/content/center/%s/%s/%s.html' % (___utils___module___.___MODULE_PATH___, ___utils___module_model___.___MODEL_PATH___, ___APPLICATION___ADMINISTRATION___TEMPLATE___INDEX___)
    )
    return http.JsonResponse(dict___data)


def ___jsonresponse___list___(request, ___utils___module___, ___utils___module_model___):
    dict___data = dict()
    dict___data['___BOOLEAN___ERROR___'] = False
    list_instance___search = ___list_instance___search___(request=request, ___utils___module___=___utils___module___, ___utils___module_model___=___utils___module_model___)
    page = ___instance___page___(request=request, ___utils___module___=___utils___module___, ___utils___module_model___=___utils___module_model___, int___number_page=0, list_instance___search=list_instance___search)
    dict___data['___HTML___APPLICATION___ADMINISTRATION___CONTENT___CENTER___CONTENT___TABLE___TBODY___'] = ___html___template_index___table_tbody___(request=request, ___utils___module___=___utils___module___, ___utils___module_model___=___utils___module_model___, page=page)
    dict___data['___HTML___APPLICATION___ADMINISTRATION___CONTENT___CENTER___CONTENT___PAGINATION___'] = ___html___template_index___pagination___(request=request, ___utils___module___=___utils___module___, ___utils___module_model___=___utils___module_model___, page=page)
    return http.JsonResponse(dict___data)


def ___jsonresponse___list___tree___(request, ___utils___module___, ___utils___module_model___):
    try:
        pk = int(request.GET.get('pk'))
        int___parent = int(request.GET.get('parent'))
        int___position = int(request.GET.get('position'))
    except ValueError:
        messages.add_message(request, messages.ERROR, _('APPLICATION___SECURITY___MESSAGE ERROR.'))
        return ___jsonresponse___error___(request=request)
    dict___data = dict()
    instance = ___utils___module_model___.___MODEL___.objects.___instance___(request=request, pk=pk)
    if instance is None:
        messages.add_message(request, messages.ERROR, _('APPLICATION___SECURITY___MESSAGE ERROR.'))
        return ___jsonresponse___error___(request=request)
    if int___parent < 0:
        messages.add_message(request, messages.ERROR, _('APPLICATION___SECURITY___MESSAGE ERROR.'))
        return ___jsonresponse___error___(request=request)
    instance_parent = None
    if 0 < int___parent:  # when int___parent==0: this instance have parent==null in the data base
        instance_parent = ___utils___module_model___.___MODEL___.objects.___instance___(request=request, pk=int___parent)
        if instance_parent is None:
            messages.add_message(request, messages.ERROR, _('APPLICATION___SECURITY___MESSAGE ERROR.'))
            return ___jsonresponse___error___(request=request)
    instances = ___utils___module_model___.___MODEL___.objects.___instances___(request=request)
    if not (0 < int___position <= len(instances)):
        messages.add_message(request, messages.ERROR, _('APPLICATION___SECURITY___MESSAGE ERROR.'))
        return ___jsonresponse___error___(request=request)
    # get parents of instance
    list_int___parent = []
    temporal_int___parent = instance.parent
    while temporal_int___parent != 0:
        list_int___parent.append(temporal_int___parent)
        temporal_instance___parent = ___utils___module_model___.___MODEL___.objects.___instance___(request=request, pk=temporal_int___parent)
        temporal_int___parent = temporal_instance___parent.parent
    list_int___parent.append(0)
    # count children of the instance
    int___children_amount = 0
    for temporal_instance in instances[instance.position:]:
        if temporal_instance.parent in list_int___parent:
            break
        int___children_amount += 1
    # change positions
    if instance.position < int___position:
        for temporal_instance in instances[instance.position + int___children_amount:int___position + int___children_amount]:
            temporal_instance.position -= (1 + int___children_amount)
            temporal_instance.save()
        instances[instance.position - 1].parent = int___parent
        temporal_int___position = int___position
        for temporal_instance in instances[instance.position - 1:instance.position + int___children_amount]:
            temporal_instance.position = temporal_int___position
            temporal_int___position += 1
            temporal_instance.save()
    elif int___position < instance.position:
        instances[instance.position - 1].parent = int___parent
        temporal_int___position = int___position
        for temporal_instance in instances[instance.position - 1:instance.position + int___children_amount]:
            temporal_instance.position = temporal_int___position
            temporal_int___position += 1
            temporal_instance.save()
        for temporal_instance in instances[int___position - 1:instance.position - 1]:
            temporal_instance.position += (int___children_amount + 1)
            temporal_instance.save()
    else:  # instance.position == position
        instances[instance.position - 1].parent = int___parent
        instances[instance.position - 1].save()
    # change is_active
    if 0 < int___parent:  # when int___parent==0: this instance have parent==null in the data base
        if instance_parent.is_active is False and instance.is_active is True:
            instances = ___utils___module_model___.___MODEL___.objects.___instances___(request=request)
            for temporal_instance in instances[int___position - 1:int___position + int___children_amount]:
                temporal_instance.is_active = False
                temporal_instance.save()
            dict___data['LOCALE___is_active'] = dict()
            dict___data['LOCALE___is_active']['option_no'] = '%s' % (_('APPLICATION___ADMINISTRATION___CONTENT___OPTION_NO'),)
    #
    if hasattr(___utils___module_model___, '___void___list___tree___'):
        instance = ___utils___module_model___.___MODEL___.objects.___instance___(request=request, pk=pk)
        ___utils___module_model___.___void___list___tree___(request=request, dict___data=dict___data, instance=instance)
    #
    messages.add_message(request, messages.SUCCESS, _('APPLICATION___ADMINISTRATION___CONTENT___MESSAGE %(instance)s was successfully updated.') % {'instance': instance, })
    dict___data['___HTML___APPLICATION___ADMINISTRATION___MODAL___'] = ___html___template_modal___message___(request=request)
    dict___data['___HTML___APPLICATION___ADMINISTRATION___MODAL___MESSAGE___'] = ___html___template_message___(request=request)
    dict___data['___BOOLEAN___ERROR___'] = False
    return http.JsonResponse(dict___data)


def ___jsonresponse___create___(request, ___utils___module___, ___utils___module_model___):
    dict___data = dict()
    if hasattr(___utils___module_model___, '___boolean___create___initial___'):
        boolean___request = ___utils___module_model___.___boolean___create___initial___(request=request, dict___data=dict___data)
        if boolean___request is False:
            return ___jsonresponse___error___(request=request)
    form = ___utils___module_model___.___FORM___CREATE___(data=request.POST or None, request=request)
    if request.method == 'POST':
        dict___data['___BOOLEAN___IS_METHOD_POST___'] = True
        if form.is_valid():
            instance = form.save(commit=True)
            list_instance___search = ___list_instance___search___(request=request, ___utils___module___=___utils___module___, ___utils___module_model___=___utils___module_model___)
            int___number_page = ___int___number_page___(request=request, ___utils___module___=___utils___module___, ___utils___module_model___=___utils___module_model___, list_instance___search=list_instance___search, pk=instance.pk)
            page = ___instance___page___(request=request, ___utils___module___=___utils___module___, ___utils___module_model___=___utils___module_model___, list_instance___search=list_instance___search, int___number_page=int___number_page)
            messages.add_message(request, messages.SUCCESS, _('APPLICATION___ADMINISTRATION___CONTENT___MESSAGE %(instance)s was successfully created.') % {'instance': instance, })
            dict___data['___BOOLEAN___IS_VALID_FORM___'] = True
            dict___data['___HTML___APPLICATION___ADMINISTRATION___CONTENT___CENTER___CONTENT___TABLE___TBODY___'] = ___html___template_index___table_tbody___(request=request, ___utils___module___=___utils___module___, ___utils___module_model___=___utils___module_model___, page=page)
            dict___data['___HTML___APPLICATION___ADMINISTRATION___CONTENT___CENTER___CONTENT___PAGINATION___'] = ___html___template_index___pagination___(request=request, ___utils___module___=___utils___module___, ___utils___module_model___=___utils___module_model___, page=page)
            if request.GET.get('action_create_update') and request.GET.get('action_create_update') == 'active':
                instance_current = copy.deepcopy(instance)
                form = ___utils___module_model___.___FORM___UPDATE___(data=None, files=None, request=request, instance=instance, instance_current=instance_current)
                dict___data['___HTML___APPLICATION___ADMINISTRATION___MODAL___'] = ___html___template_modal___(request=request, ___utils___module___=___utils___module___, ___utils___module_model___=___utils___module_model___, ___application___administration___template___=___APPLICATION___ADMINISTRATION___TEMPLATE___UPDATE___, form=form)
                dict___data['___HTML___APPLICATION___ADMINISTRATION___MODAL___MESSAGE___'] = ___html___template_message___(request=request)
                dict___data['___BOOLEAN___ERROR___'] = False
                return http.JsonResponse(dict___data)
            else:
                form = ___utils___module_model___.___FORM___CREATE___(data=None, request=request)
        else:
            if form.errors.as_data().get('__all__') is not None:
                messages.add_message(request, messages.ERROR, form.errors['__all__'][0])
            dict___data['___BOOLEAN___IS_VALID_FORM___'] = False
    else:
        dict___data['___BOOLEAN___IS_METHOD_POST___'] = False
    dict___data['___HTML___APPLICATION___ADMINISTRATION___MODAL___'] = ___html___template_modal___(request=request, ___utils___module___=___utils___module___, ___utils___module_model___=___utils___module_model___, ___application___administration___template___=___APPLICATION___ADMINISTRATION___TEMPLATE___CREATE___, form=form)
    dict___data['___HTML___APPLICATION___ADMINISTRATION___MODAL___MESSAGE___'] = ___html___template_message___(request=request)
    dict___data['___BOOLEAN___ERROR___'] = False
    return http.JsonResponse(dict___data)


def ___jsonresponse___detail___(request, ___utils___module___, ___utils___module_model___, pk):
    dict___data = dict()
    try:
        pk = int(pk)
    except ValueError:
        messages.add_message(request, messages.ERROR, _('APPLICATION___SECURITY___MESSAGE ERROR.'))
        return ___jsonresponse___error___(request=request)
    instance = ___utils___module_model___.___MODEL___.objects.___instance___(request=request, pk=pk)
    if instance is None:
        messages.add_message(request, messages.ERROR, _('APPLICATION___SECURITY___MESSAGE ERROR.'))
        return ___jsonresponse___error___(request=request)
    if hasattr(___utils___module_model___, '___boolean___detail___initial___'):
        boolean___request = ___utils___module_model___.___boolean___detail___initial___(request=request, dict___data=dict___data)
        if boolean___request is False:
            return ___jsonresponse___error___(request=request)
    form = ___utils___module_model___.___FORM___DETAIL___(data=None, request=request, instance=instance)
    if hasattr(form, '___detail___'):
        form.___detail___()
    dict___data['___HTML___APPLICATION___ADMINISTRATION___MODAL___'] = ___html___template_modal___(request=request, ___utils___module___=___utils___module___, ___utils___module_model___=___utils___module_model___, ___application___administration___template___=___APPLICATION___ADMINISTRATION___TEMPLATE___DETAIL___, form=form)
    dict___data['___HTML___APPLICATION___ADMINISTRATION___MODAL___MESSAGE___'] = ___html___template_message___(request=request)
    dict___data['___BOOLEAN___ERROR___'] = False
    return http.JsonResponse(dict___data)


def ___jsonresponse___update___(request, ___utils___module___, ___utils___module_model___, pk):
    dict___data = dict()
    try:
        pk = int(pk)
    except ValueError:
        messages.add_message(request, messages.ERROR, _('APPLICATION___SECURITY___MESSAGE ERROR.'))
        return ___jsonresponse___error___(request=request)
    instance = ___utils___module_model___.___MODEL___.objects.___instance___(request=request, pk=pk)
    if instance is None:
        messages.add_message(request, messages.ERROR, _('APPLICATION___SECURITY___MESSAGE ERROR.'))
        return ___jsonresponse___error___(request=request)
    if hasattr(___utils___module_model___, '___boolean___update___initial___'):
        boolean___request = ___utils___module_model___.___boolean___update___initial___(request=request, dict___data=dict___data)
        if boolean___request is False:
            return ___jsonresponse___error___(request=request)
    instance_current = copy.deepcopy(instance)
    form = ___utils___module_model___.___FORM___UPDATE___(data=request.POST or None, files=request.FILES or None, request=request, instance=instance, instance_current=instance_current)
    if request.method == 'POST':
        dict___data['___BOOLEAN___IS_METHOD_POST___'] = True
        if form.is_valid():
            instance = form.save(commit=True)
            list_instance___search = ___list_instance___search___(request=request, ___utils___module___=___utils___module___, ___utils___module_model___=___utils___module_model___)
            int___number_page = ___int___number_page___(request=request, ___utils___module___=___utils___module___, ___utils___module_model___=___utils___module_model___, list_instance___search=list_instance___search, pk=instance.pk)
            page = ___instance___page___(request=request, ___utils___module___=___utils___module___, ___utils___module_model___=___utils___module_model___, list_instance___search=list_instance___search, int___number_page=int___number_page)
            messages.add_message(request, messages.SUCCESS, _('APPLICATION___ADMINISTRATION___CONTENT___MESSAGE %(instance)s was successfully updated.') % {'instance': instance, })
            dict___data['___BOOLEAN___IS_VALID_FORM___'] = True
            dict___data['___HTML___APPLICATION___ADMINISTRATION___CONTENT___CENTER___CONTENT___TABLE___TBODY___'] = ___html___template_index___table_tbody___(request=request, ___utils___module___=___utils___module___, ___utils___module_model___=___utils___module_model___, page=page)
            dict___data['___HTML___APPLICATION___ADMINISTRATION___CONTENT___CENTER___CONTENT___PAGINATION___'] = ___html___template_index___pagination___(request=request, ___utils___module___=___utils___module___, ___utils___module_model___=___utils___module_model___, page=page)
        else:
            if form.errors.as_data().get('__all__') is not None:
                messages.add_message(request, messages.ERROR, form.errors['__all__'][0])
            dict___data['___BOOLEAN___IS_VALID_FORM___'] = False
    else:
        dict___data['___BOOLEAN___IS_METHOD_POST___'] = False
    dict___data['___HTML___APPLICATION___ADMINISTRATION___MODAL___'] = ___html___template_modal___(request=request, ___utils___module___=___utils___module___, ___utils___module_model___=___utils___module_model___, ___application___administration___template___=___APPLICATION___ADMINISTRATION___TEMPLATE___UPDATE___, form=form)
    dict___data['___HTML___APPLICATION___ADMINISTRATION___MODAL___MESSAGE___'] = ___html___template_message___(request=request)
    dict___data['___BOOLEAN___ERROR___'] = False
    return http.JsonResponse(dict___data)


def ___jsonresponse___delete___(request, ___utils___module___, ___utils___module_model___, pk):
    dict___data = dict()
    try:
        pk = int(pk)
    except ValueError:
        messages.add_message(request, messages.ERROR, _('APPLICATION___SECURITY___MESSAGE ERROR.'))
        return ___jsonresponse___error___(request=request)
    instance = ___utils___module_model___.___MODEL___.objects.___instance___(request=request, pk=pk)
    if instance is None:
        messages.add_message(request, messages.ERROR, _('APPLICATION___SECURITY___MESSAGE ERROR.'))
        return ___jsonresponse___error___(request=request)
    if hasattr(___utils___module_model___, '___boolean___delete___initial___'):
        boolean___request = ___utils___module_model___.___boolean___delete___initial___(request=request, dict___data=dict___data)
        if boolean___request is False:
            return ___jsonresponse___error___(request=request)
    form = ___utils___module_model___.___FORM___DELETE___(data=request.POST or None, request=request, instance=instance)
    if request.method == 'POST':
        dict___data['___BOOLEAN___IS_METHOD_POST___'] = True
        if form.is_valid():
            list_instance___search = ___list_instance___search___(request=request, ___utils___module___=___utils___module___, ___utils___module_model___=___utils___module_model___)
            int___number_page = ___int___number_page___(request=request, ___utils___module___=___utils___module___, ___utils___module_model___=___utils___module_model___, list_instance___search=list_instance___search, pk=instance.pk)
            if hasattr(form, '___delete___'):
                form.___delete___()
            else:
                instance.delete()
            list_instance___search = ___list_instance___search___(request=request, ___utils___module___=___utils___module___, ___utils___module_model___=___utils___module_model___)
            page = ___instance___page___(request=request, ___utils___module___=___utils___module___, ___utils___module_model___=___utils___module_model___, list_instance___search=list_instance___search, int___number_page=int___number_page)
            messages.add_message(request, messages.SUCCESS, _('APPLICATION___ADMINISTRATION___CONTENT___MESSAGE %(instance)s was successfully deleted.') % {'instance': instance, })
            dict___data['___BOOLEAN___IS_VALID_FORM___'] = True
            dict___data['___HTML___APPLICATION___ADMINISTRATION___MODAL___'] = ___html___template_modal___message___(request=request)
            dict___data['___HTML___APPLICATION___ADMINISTRATION___MODAL___MESSAGE___'] = ___html___template_message___(request=request)
            dict___data['___HTML___APPLICATION___ADMINISTRATION___CONTENT___CENTER___CONTENT___TABLE___TBODY___'] = ___html___template_index___table_tbody___(request=request, ___utils___module___=___utils___module___, ___utils___module_model___=___utils___module_model___, page=page)
            dict___data['___HTML___APPLICATION___ADMINISTRATION___CONTENT___CENTER___CONTENT___PAGINATION___'] = ___html___template_index___pagination___(request=request, ___utils___module___=___utils___module___, ___utils___module_model___=___utils___module_model___, page=page)
            dict___data['___BOOLEAN___ERROR___'] = False
            return http.JsonResponse(dict___data)
        else:
            if form.errors.as_data().get('__all__') is not None:
                messages.add_message(request, messages.ERROR, form.errors['__all__'][0])
            dict___data['___BOOLEAN___IS_VALID_FORM___'] = False
    else:
        dict___data['___BOOLEAN___IS_METHOD_POST___'] = False
    dict___data['___HTML___APPLICATION___ADMINISTRATION___MODAL___'] = ___html___template_modal___(request=request, ___utils___module___=___utils___module___, ___utils___module_model___=___utils___module_model___, ___application___administration___template___=___APPLICATION___ADMINISTRATION___TEMPLATE___DELETE___, form=form)
    dict___data['___HTML___APPLICATION___ADMINISTRATION___MODAL___MESSAGE___'] = ___html___template_message___(request=request)
    dict___data['___BOOLEAN___ERROR___'] = False
    return http.JsonResponse(dict___data)


def ___jsonresponse___approve___(request, ___utils___module___, ___utils___module_model___, pk):
    dict___data = dict()
    try:
        pk = int(pk)
    except ValueError:
        messages.add_message(request, messages.ERROR, _('APPLICATION___SECURITY___MESSAGE ERROR.'))
        return ___jsonresponse___error___(request=request)
    instance = ___utils___module_model___.___MODEL___.objects.___instance___(request=request, pk=pk)
    if instance is None:
        messages.add_message(request, messages.ERROR, _('APPLICATION___SECURITY___MESSAGE ERROR.'))
        return ___jsonresponse___error___(request=request)
    if hasattr(___utils___module_model___, '___boolean___approve___initial___'):
        boolean___request = ___utils___module_model___.___boolean___approve___initial___(request=request, dict___data=dict___data)
        if boolean___request is False:
            return ___jsonresponse___error___(request=request)
    form = ___utils___module_model___.___FORM___APPROVE___(data=request.POST or None, request=request, instance=instance)
    if request.method == 'POST':
        dict___data['___BOOLEAN___IS_METHOD_POST___'] = True
        if form.is_valid():
            if hasattr(form, '___approve___'):
                instance_mirror = form.___approve___()
                messages.add_message(request, messages.SUCCESS, _('APPLICATION___ADMINISTRATION___CONTENT___MESSAGE %(instance)s was successfully approved.') % {'instance': instance_mirror, })
            else:
                messages.add_message(request, messages.ERROR, _('APPLICATION___SECURITY___MESSAGE ERROR.'))
                return ___jsonresponse___error___(request=request)
            list_instance___search = ___list_instance___search___(request=request, ___utils___module___=___utils___module___, ___utils___module_model___=___utils___module_model___)
            int___number_page = ___int___number_page___(request=request, ___utils___module___=___utils___module___, ___utils___module_model___=___utils___module_model___, list_instance___search=list_instance___search, pk=instance.pk)
            if hasattr(form, '___delete___'):
                form.___delete___()
            else:
                instance.delete()
            list_instance___search = ___list_instance___search___(request=request, ___utils___module___=___utils___module___, ___utils___module_model___=___utils___module_model___)
            page = ___instance___page___(request=request, ___utils___module___=___utils___module___, ___utils___module_model___=___utils___module_model___, list_instance___search=list_instance___search, int___number_page=int___number_page)
            dict___data['___BOOLEAN___IS_VALID_FORM___'] = True
            dict___data['___HTML___APPLICATION___ADMINISTRATION___MODAL___'] = ___html___template_modal___message___(request=request)
            dict___data['___HTML___APPLICATION___ADMINISTRATION___MODAL___MESSAGE___'] = ___html___template_message___(request=request)
            dict___data['___HTML___APPLICATION___ADMINISTRATION___CONTENT___CENTER___CONTENT___TABLE___TBODY___'] = ___html___template_index___table_tbody___(request=request, ___utils___module___=___utils___module___, ___utils___module_model___=___utils___module_model___, page=page)
            dict___data['___HTML___APPLICATION___ADMINISTRATION___CONTENT___CENTER___CONTENT___PAGINATION___'] = ___html___template_index___pagination___(request=request, ___utils___module___=___utils___module___, ___utils___module_model___=___utils___module_model___, page=page)
            dict___data['___BOOLEAN___ERROR___'] = False
            return http.JsonResponse(dict___data)
        else:
            if form.errors.as_data().get('__all__') is not None:
                messages.add_message(request, messages.ERROR, form.errors['__all__'][0])
            dict___data['___BOOLEAN___IS_VALID_FORM___'] = False
    else:
        dict___data['___BOOLEAN___IS_METHOD_POST___'] = False
    dict___data['___HTML___APPLICATION___ADMINISTRATION___MODAL___'] = ___html___template_modal___(request=request, ___utils___module___=___utils___module___, ___utils___module_model___=___utils___module_model___, ___application___administration___template___=___APPLICATION___ADMINISTRATION___TEMPLATE___APPROVE___, form=form)
    dict___data['___HTML___APPLICATION___ADMINISTRATION___MODAL___MESSAGE___'] = ___html___template_message___(request=request)
    dict___data['___BOOLEAN___ERROR___'] = False
    return http.JsonResponse(dict___data)


def ___jsonresponse___disapprove___(request, ___utils___module___, ___utils___module_model___, pk):
    dict___data = dict()
    try:
        pk = int(pk)
    except ValueError:
        messages.add_message(request, messages.ERROR, _('APPLICATION___SECURITY___MESSAGE ERROR.'))
        return ___jsonresponse___error___(request=request)
    instance = ___utils___module_model___.___MODEL___.objects.___instance___(request=request, pk=pk)
    if instance is None:
        messages.add_message(request, messages.ERROR, _('APPLICATION___SECURITY___MESSAGE ERROR.'))
        return ___jsonresponse___error___(request=request)
    if hasattr(___utils___module_model___, '___boolean___disapprove___initial___'):
        boolean___request = ___utils___module_model___.___boolean___disapprove___initial___(request=request, dict___data=dict___data)
        if boolean___request is False:
            return ___jsonresponse___error___(request=request)
    form = ___utils___module_model___.___FORM___DISAPPROVE___(data=request.POST or None, request=request, instance=instance)
    if request.method == 'POST':
        dict___data['___BOOLEAN___IS_METHOD_POST___'] = True
        if form.is_valid():
            if hasattr(form, '___disapprove___'):
                form.___disapprove___()
                messages.add_message(request, messages.SUCCESS, _('APPLICATION___ADMINISTRATION___CONTENT___MESSAGE %(instance)s was successfully disapproved.') % {'instance': instance, })
            else:
                messages.add_message(request, messages.ERROR, _('APPLICATION___SECURITY___MESSAGE ERROR.'))
                return ___jsonresponse___error___(request=request)
            list_instance___search = ___list_instance___search___(request=request, ___utils___module___=___utils___module___, ___utils___module_model___=___utils___module_model___)
            int___number_page = ___int___number_page___(request=request, ___utils___module___=___utils___module___, ___utils___module_model___=___utils___module_model___, list_instance___search=list_instance___search, pk=instance.pk)
            if hasattr(form, '___delete___'):
                form.___delete___()
            else:
                instance.delete()
            list_instance___search = ___list_instance___search___(request=request, ___utils___module___=___utils___module___, ___utils___module_model___=___utils___module_model___)
            page = ___instance___page___(request=request, ___utils___module___=___utils___module___, ___utils___module_model___=___utils___module_model___, list_instance___search=list_instance___search, int___number_page=int___number_page)
            dict___data['___BOOLEAN___IS_VALID_FORM___'] = True
            dict___data['___HTML___APPLICATION___ADMINISTRATION___MODAL___'] = ___html___template_modal___message___(request=request)
            dict___data['___HTML___APPLICATION___ADMINISTRATION___MODAL___MESSAGE___'] = ___html___template_message___(request=request)
            dict___data['___HTML___APPLICATION___ADMINISTRATION___CONTENT___CENTER___CONTENT___TABLE___TBODY___'] = ___html___template_index___table_tbody___(request=request, ___utils___module___=___utils___module___, ___utils___module_model___=___utils___module_model___, page=page)
            dict___data['___HTML___APPLICATION___ADMINISTRATION___CONTENT___CENTER___CONTENT___PAGINATION___'] = ___html___template_index___pagination___(request=request, ___utils___module___=___utils___module___, ___utils___module_model___=___utils___module_model___, page=page)
            dict___data['___BOOLEAN___ERROR___'] = False
            return http.JsonResponse(dict___data)
        else:
            if form.errors.as_data().get('__all__') is not None:
                messages.add_message(request, messages.ERROR, form.errors['__all__'][0])
            dict___data['___BOOLEAN___IS_VALID_FORM___'] = False
    else:
        dict___data['___BOOLEAN___IS_METHOD_POST___'] = False
    dict___data['___HTML___APPLICATION___ADMINISTRATION___MODAL___'] = ___html___template_modal___(request=request, ___utils___module___=___utils___module___, ___utils___module_model___=___utils___module_model___, ___application___administration___template___=___APPLICATION___ADMINISTRATION___TEMPLATE___DISAPPROVE___, form=form)
    dict___data['___HTML___APPLICATION___ADMINISTRATION___MODAL___MESSAGE___'] = ___html___template_message___(request=request)
    dict___data['___BOOLEAN___ERROR___'] = False
    return http.JsonResponse(dict___data)
