# -*- coding: utf-8 -*-
from django import forms
from django.core.validators import ValidationError, RegexValidator
from django.utils.translation import ugettext_lazy as _
from ... import slurm
import re


class ScriptForm(forms.Form):
    # General options
    script_name = forms.CharField(
        required=True,
        validators=[RegexValidator('^[a-zA-Z0-9_]+[a-zA-Z0-9_.-]*$', message=_('HPC___CONTENT___SCRIPT___ERROR___SCRIPT_NAME')), ],
        widget=forms.TextInput(attrs={
            'autofocus': 'autofocus',
            'class': 'form-control',
            'name': 'script_name',
            'placeholder': _('HPC___CONTENT___SCRIPT___FIELD___SCRIPT_NAME___PLACEHOLDER')
        }),
    )
    job_name = forms.CharField(
        required=False,
        validators=[RegexValidator('^[a-zA-Z0-9_]+[a-zA-Z0-9_.]*$', message=_('HPC___CONTENT___SCRIPT___ERROR___SCRIPT_NAME')), ],
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'name': 'job_name',
            'placeholder': _('HPC___CONTENT___SCRIPT___FIELD___JOB_NAME___PLACEHOLDER')
        }),
    )
    export_variables = forms.BooleanField(
        required=False,
        initial=True,
        widget=forms.CheckboxInput(attrs={
            'name': 'export_variables',
        }),
    )
    partition = forms.ChoiceField(
        required=False,
        error_messages={
            'invalid_choice': _("HPC___CONTENT___SCRIPT___ERROR___PARTITION___INVALID_CHOICE"),
        },
        widget=forms.Select(attrs={
            'class': 'form-control',
            'name': 'partition',
        }),
    )
    # Resource handling
    nodes = forms.CharField(
        required=False,
        validators=[RegexValidator('^\d{1,3}(-\d{1,3})?$', message=_('HPC___CONTENT___SCRIPT___ERROR___NODES')), ],
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'name': 'nodes',
            'placeholder': _("HPC___CONTENT___SCRIPT___FIELD___RESOURCE_LIST_NODES___PLACEHOLDER")
        }),
    )
    ntasks = forms.IntegerField(
        required=False,
        min_value=1,
        error_messages={
            'invalid': _("HPC___CONTENT___SCRIPT___ERROR___TASKS___INVALID"),
            'min_value': _("HPC___CONTENT___SCRIPT___ERROR___TASKS___MIN_VALUE")
        },
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'name': 'ntaks',
            'placeholder': _("HPC___CONTENT___SCRIPT___FIELD___RESOURCE_LIST_NODES___PLACEHOLDER_2")
        }),
    )
    tasks_per_node = forms.IntegerField(
        required=False,
        min_value=1,
        error_messages={
            'invalid': _("HPC___CONTENT___SCRIPT___ERROR___TASKS_PER_NODE___INVALID"),
            'min_value': _("HPC___CONTENT___SCRIPT___ERROR___TASKS_PER_NODE___MIN_VALUE")
        },
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'name': 'tasks_per_node',
            'placeholder': _("HPC___CONTENT___SCRIPT___FIELD___RESOURCE_LIST_PROCESSES___PLACEHOLDER")
        }),
    )
    cpus_per_task = forms.IntegerField(
        required=False,
        min_value=1,
        error_messages={
            'invalid': _("HPC___CONTENT___SCRIPT___ERROR___CPUS_PER_TASK___INVALID"),
            'min_value': _("HPC___CONTENT___SCRIPT___ERROR___CPUS_PER_TASK___MIN_VALUE")
        },
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'name': 'cpus_per_task',
            'placeholder': _("HPC___CONTENT___SCRIPT___FIELD___RESOURCE_LIST_PROCESSES___PLACEHOLDER_2")
        }),
    )
    mem = forms.IntegerField(
        required=False,
        error_messages={
            'invalid': _("HPC___CONTENT___SCRIPT___ERROR___MEM___INVALID"),
        },
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'name': 'mem',
            'placeholder': _("HPC___CONTENT___SCRIPT___FIELD___MEMORY___PLACEHOLDER")
        }),
    )
    size = forms.ChoiceField(
        error_messages={
            'invalid_choice': _("HPC___CONTENT___SCRIPT___ERROR___SIZE___INVALID_CHOICE"),
        },
        widget=forms.Select(attrs={
            'class': 'form-control',
            'name': 'size',
            'style': 'min-width: 52px'
        }),
        choices=[('K', 'K'), ('M', 'M'), ('G', 'G')],
        initial='M'
    )
    mem_per_cpu = forms.IntegerField(
        required=False,
        error_messages={
            'invalid': _("HPC___CONTENT___SCRIPT___ERROR___MEM_PER_CPU___INVALID"),
        },
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'name': 'mem_per_cpu',
            'placeholder': _("HPC___CONTENT___SCRIPT___FIELD___MEMORY___PLACEHOLDER_2")
        }),
    )
    size_per_cpu = forms.ChoiceField(
        error_messages={
            'invalid_choice': _("HPC___CONTENT___SCRIPT___ERROR___SIZE_PER_CPU___INVALID_CHOICE"),
        },
        widget=forms.Select(attrs={
            'class': 'form-control',
            'name': 'size_per_cpu',
            'style': 'min-width: 52px'
        }),
        choices=[('K', 'K'), ('M', 'M'), ('G', 'G')],
        initial='M'
    )
    time = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'name': 'time',
            'placeholder': _("HPC___CONTENT___SCRIPT___FIELD___WALLTIME___PLACEHOLDER")
        }),
    )
    test = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={
            'name': 'test'
        }),
    )
    require_gpus = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={
            'name': 'require_gpus'
        }),
    )
    nodelist = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'name': 'nodelist',
            'placeholder': _("HPC___CONTENT___SCRIPT___FIELD___NODELIST___PLACEHOLDER")
        }),
    )
    exclude = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'name': 'exclude',
            'placeholder': _("HPC___CONTENT___SCRIPT___FIELD___EXCLUDE___PLACEHOLDER")
        }),
    )
    # Output stream options
    output = forms.CharField(
        required=False,
        max_length=100,
        validators=[RegexValidator('^[a-zA-Z0-9_]+[a-zA-Z0-9_.-]*$', message=_('HPC___CONTENT___SCRIPT___ERROR___SCRIPT_NAME')), ],
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'name': 'output',
            'placeholder': _("HPC___CONTENT___SCRIPT___FIELD___OUTPUT_STREAM___PLACEHOLDER")
        }),
    )
    error = forms.CharField(
        required=False,
        max_length=100,
        validators=[RegexValidator('^[a-zA-Z0-9_]+[a-zA-Z0-9_.-]*$', message=_('HPC___CONTENT___SCRIPT___ERROR___SCRIPT_NAME')), ],
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'name': 'error',
            'placeholder': _("HPC___CONTENT___SCRIPT___FIELD___ERROR_STREAM___PLACEHOLDER")
        }),
    )
    # Mail options
    mail_user = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'name': 'mail_user',
            'placeholder': _('HPC___CONTENT___SCRIPT___FIELD___MAIL_ADDRESS___PLACEHOLDER')
        }),
    )

    mail_begin = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={
            'name': 'mail_begin',
            'style': 'display: none'
        }),
    )
    mail_end = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={
            'name': 'mail_end',
            'style': 'display: none'
        }),
    )
    mail_abort = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={
            'name': 'mail_abort',
            'style': 'display: none'
        }),
    )
    mail_requeue = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={
            'name': 'mail_requeue',
            'style': 'display: none'
        }),
    )

    # Script body
    script_body = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'name': 'script_body',
            'rows': '6',
            'placeholder': _('HPC___CONTENT___SCRIPT___FIELD___BODY_SCRIPT___PLACEHOLDER')
        }),
    )

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super().__init__(*args, **kwargs)
        dict___data = slurm.generate_data_dict(self.request, 'partitions')
        if dict___data:
            self.fields['partition'].choices = parse(dict___data['data'])
        else:
            self.fields['partition'].choices = [('', _('HPC___CONTENT___SCRIPT___ERROR___PARTITION')), ]

    def clean_nodes(self):
        nodes = self.cleaned_data['nodes'] or ''
        if nodes:
            if nodes.find('-') != -1:
                mi, ma = nodes.split('-')
                if mi > ma:
                    raise ValidationError(_('HPC___CONTENT___SCRIPT___ERROR___NODES'))
        return nodes

    def clean_mail_user(self):
        mail_user = self.cleaned_data['mail_user'] or ''
        if mail_user:
            mails = mail_user.split(',')
            for mail in mails:
                if re.match(' *\w[\w\.-]*@\w[\w\.-]+\.\w+', mail) is None:
                    raise ValidationError(_('HPC___CONTENT___SCRIPT___ERROR___MAIL_ADDRESS'))
        return mail_user

    def clean_time(self):
        time = self.cleaned_data['time'] or ''
        message = _('HPC___CONTENT___SCRIPT___ERROR___TIME')
        if time:
            try:
                int(time)
                return time
            except ValueError:
                pass
            try:
                if time.find('-') != -1:
                    d, t = time.split('-')
                    int(d)
                else:
                    t = time
                components = t.split(':')
                if len(components) > 3:
                    assert False
                for c in components:
                    int(c)
            except:
                raise ValidationError(message)
        return time

    def clean_nodelist(self):
        nodelist = self.cleaned_data['nodelist'] or ''
        message = _('HPC___CONTENT___SCRIPT___ERROR___NODELIST')
        # regex = RegexValidator(r'^nodo(\[([(d{3})(d{3}-d{3})]\,)*[(d{3})(d{3}-d{3})]\])d{3}$')
        # if not regex.regex.match(nodelist):
        #     raise ValidationError(message)
        return nodelist

    def clean_exclude(self):
        exclude = self.cleaned_data['exclude'] or ''
        message = _('HPC___CONTENT___SCRIPT___ERROR___EXCLUDE')
        # regex = RegexValidator(r'^nodo(\[([(d{3})(d{3}-d{3})]\,)*[(d{3})(d{3}-d{3})]\])d{3}$')
        # if not regex.regex.match(exclude):
        #     raise ValidationError(message)
        return exclude


def parse(choices):
    # return [('partition1', 'partition1')]
    l = list()
    for choice in choices:
        l.append((choice, choice))
    return l
