# -*- coding: utf-8 -*-
import re

entityMap = {
    '&': '&amp;',
    '<': '&lt;',
    '>': '&gt;',
    '"': '&quot;',
    "'": '&#39;',
    '/': '&#x2F;',
    '`': '&#x60;',
    '=': '&#x3D;'
}


def escape_html (string):
    """Produce entities within text."""
    return "".join(entityMap.get(c, c) for c in string)


def build(form):
    # l = []
    # for i in [1, 2, 3]:
    #     l.append(i+1)
    # a, b, c = l
    job_name = form.cleaned_data.get('job_name')
    export_variables = form.cleaned_data.get('export_variables')
    partition = form.cleaned_data.get('partition')
    nodes = form.cleaned_data.get('nodes')
    ntasks = form.cleaned_data.get('ntasks')
    tasks_per_node = form.cleaned_data.get('tasks_per_node', 0)
    cpus_per_task = form.cleaned_data.get('cpus_per_task', 0)
    mem = form.cleaned_data.get('mem', 0)
    size = form.cleaned_data.get('size')
    mem_per_cpu = form.cleaned_data.get('mem_per_cpu', 0)
    size_per_cpu = form.cleaned_data.get('size_per_cpu')
    time = form.cleaned_data.get('time')
    test = form.cleaned_data.get('test')
    require_gpus = form.cleaned_data.get('require_gpus')
    nodelist = form.cleaned_data.get('nodelist')
    exclude = form.cleaned_data.get('exclude')
    output = form.cleaned_data.get('output')
    error = form.cleaned_data.get('error')
    mail_user = form.cleaned_data.get('mail_user')
    mail_begin = form.cleaned_data.get('mail_begin')
    mail_end = form.cleaned_data.get('mail_end')
    mail_abort = form.cleaned_data.get('mail_abort')
    mail_requeue = form.cleaned_data.get('mail_requeue')
    script_body = form.cleaned_data.get('script_body')

    rc = '\n'
    content = "#!/bin/bash " + rc
    content += "#Submit this script with: sbatch thefilename " + rc

    if job_name or not export_variables or partition:
        content += rc + "### General options ### " + rc
        if job_name:
            content += '#SBATCH --job-name=' + escape_html(job_name) + rc
        if export_variables:
            content += '#SBATCH --export=ALL' + rc
        else:
            content += '#SBATCH --export=NONE' + rc
        if partition:
            content += '#SBATCH --partition=' + partition + rc

    if nodes or ntasks or tasks_per_node or cpus_per_task or mem or mem_per_cpu or time or test or require_gpus or nodelist or exclude:
        content += rc + "### Resource handling ###" + rc
        if nodes:
            content += '#SBATCH --nodes=' + escape_html(nodes) + rc
        if ntasks:
            content += '#SBATCH --ntasks=' + str(ntasks) + rc
        if tasks_per_node:
            content += '#SBATCH --tasks-per-node=' + str(tasks_per_node) + rc
        if cpus_per_task:
            content += '#SBATCH --cpus-per-task=' + str(cpus_per_task) + rc
        if mem:
            content += '#SBATCH --mem=' + str(mem) + size + rc
        if mem_per_cpu:
            content += '#SBATCH --mem-per-cpu=' + str(mem_per_cpu) + size_per_cpu + rc
        if time:
            content += '#SBATCH --time=' + escape_html(time) + rc
        if test:
            content += '#SBATCH --test-only' + rc
        if require_gpus:
            content += '#SBATCH --gres=gpu:2' + rc
        if nodelist:
            content += '#SBATCH --nodelist=' + escape_html(nodelist) + rc
        if exclude:
            content += '#SBATCH --exclude=' + escape_html(exclude) + rc

    if output or error:
        content += rc + "### Stream options ###" + rc
        if output:
            content += '#SBATCH --output=' + escape_html(output) + rc
        if error:
            content += '#SBATCH --error=' + escape_html(error) + rc

    if mail_user:
        content += rc + "### Mail options ###" + rc
        content += '#SBATCH --mail-user=' + mail_user + rc
        if mail_begin and mail_end and mail_abort and mail_requeue:
            content += '#SBATCH --mail-type=ALL' + rc
        elif mail_begin or mail_end or mail_abort or mail_requeue:
            if mail_begin:
                content += '#SBATCH --mail-type=BEGIN' + rc
            if mail_end:
                content += '#SBATCH --mail-type=END' + rc
            if mail_abort:
                content += '#SBATCH --mail-type=FAIL' + rc
            if mail_requeue:
                content += '#SBATCH --mail-type=REQUEUE' + rc
        else:
            content += '#SBATCH --mail-type=NONE' + rc

    content += (rc + "### Bash script ###" + rc + script_body + rc + "exit 0")
    return content
