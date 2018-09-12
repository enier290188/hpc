# -*- coding: utf-8 -*-
# django modules import
from django.contrib import messages

# python libraries import
import json

# user modules import
from . import ssh


def to_float(s):
    try:
        return float(s)
    except:
        return 0


def generate_data_dict(request, option, parameters=None):
    __dict__ = dict()
    str_in_bytes = run_command(request, option, parameters=parameters)
    if str_in_bytes:
        string_in_utf8 = str_in_bytes.decode('utf-8').rstrip('\n')
        if option == 'nodes':
            # sinfo -N --Format=all
            nodes = list()
            cpuload = cputotal = cpualloc = freemem = allocmem = 0
            for node in string_in_utf8.split('\n'):
                features = dict()
                for feature in node.split():
                    if len(feature.split('=')) == 2:
                        features.update({
                            feature.split('=')[0]: feature.split('=')[1]
                        })
                nodes.append(features)
                cpuload = cpuload + to_float(features['CPULoad'])
                cputotal = cputotal + to_float(features['CPUTot'])
                cpualloc = cpualloc + to_float(features['CPUAlloc'])
                freemem = freemem + to_float(features['FreeMem'])
                allocmem = allocmem + to_float(features['AllocMem'])
            __dict__['nodes'] = nodes
            __dict__['statistics'] = {'cpuload': cpuload/len(string_in_utf8.split('\n')), 'freemem': freemem, 'allocmem': allocmem, 'cputot': cputotal, 'cpualloc': cpualloc}
            __dict__.update(generate_data_dict(request, 'partitions-detail'))
        if option == 'partitions-detail':
            data = list()
            keys = string_in_utf8.split('\n')[0].split()
            for s in string_in_utf8.split('\n')[1:]:
                data.append(s.split())
            __dict__['partitions'] = {'data': data, 'keys': keys}
        if option == 'nodes-partitions':
            # sinfo -N --Format=all
            nodes = list()
            tmp = string_in_utf8.split('\n')
            keys = tmp[0].split('|')
            for node in tmp[1:]:
                nodes.append(node.split('|'))
            __dict__['keys'] = keys
            __dict__['nodes'] = nodes
        if option == 'cpusload':
            # sinfo -N --Format=nodelist,cpusload
            data = list()
            tmp = string_in_utf8.split('\n')
            keys = tmp[1].split()
            for node in tmp[1:]:
                data.append(node.split())
            __dict__['keys'] = keys
            __dict__['data'] = data
        if option == 'keys':
            tmp = string_in_utf8.split('\n')
            keys = tmp[1].split()
            __dict__['keys'] = keys
        if option == 'jobs all' or option == 'jobs group' or option == 'jobs user':
            tmp = string_in_utf8.split('\n')
            l = list()
            for data in tmp[2:]:
                if len(data.split()) > 9:
                    l.append(data.split()[0:8])
                    l[-1].append(" ".join(data.split()[8:]))
                elif len(data.split()) == 9:
                    l.append(data.split())
                else:
                    row = data.split()
                    row.append('')
                    l.append(row)
            __dict__['data'] = l
        if option == 'detail job':
            keys = [
                'JobId', 'JobName', 'UserId', 'GroupId', 'Priority', 'Account', 'QOS', 'JobState',
                'Reason', 'Requeue', 'Restarts', 'RunTime', 'TimeLimit', 'TimeMin', 'SubmitTime',
                'EligibleTime', 'StartTime', 'EndTime', 'Deadline', 'PreemptTime', 'SuspendTime',
                'SecsPreSuspend', 'Partition', 'AllocNode:Sid', 'ReqNodeList', 'NodeList', 'BatchHost',
                'NumNodes', 'NumCPUs', 'NumTasks', 'CPUs/Task', 'TRES', 'Command', 'WorkDir', 'StdErr',
                'StdIn', 'StdOut'
            ]
            fields = string_in_utf8.split()
            for key in keys:
                i = 0
                for field in fields:
                    if field.startswith(key):
                        if key == 'TRES':
                            __dict__['mem'] = field.split(',')[1].split('=')[1]
                        else:
                            __dict__[key] = field.split('=')[1]
                        break
                fields.pop(i)
            __dict__['Username'] = __dict__['UserId'].split('(')[0]
            __dict__['CPUsTask'] = __dict__.pop('CPUs/Task')
        if option == 'partitions':
            tmp = string_in_utf8.split('\n')
            data = list()
            for partition in tmp[1:]:
                data.append(partition)
            __dict__['data'] = data
        return __dict__


def generate_data_json(request, option, parameters=None):
    __dict__ = generate_data_dict(request, option, parameters=parameters)
    if __dict__:
        return json.dumps(generate_data_dict(request, option, parameters=parameters))


def run_command(request, option, parameters=None):
    instance = request.___APPLICATION___SECURITY___USER___
    command = 'ls'

    # hpc jobs ########
    if option == 'keys':
        command = 'squeue -all'
    if option == 'jobs all':
        command = 'squeue -all --states=all -o "%i %T %j %u %P %M %l %D %R"'
        # command = 'squeue -o "%i %T %j %u %P %M %l %D %R"'
    if option == 'detail job':  # job id in parameters
        command = 'scontrol show job -o ' + parameters[0]
    if option == 'job kill':
        command = 'scancel --signal=KILL ' + parameters[0]  # Cancela el trabajo de la cola de ejecución.
    if option == 'job hold':
        command = 'scontrol hold ' + parameters[0]  # Impide que se inicie una tarea pendiente (establece su prioridad en 0) si se esta ejecutando su prioridad se establece en 0 en caso de una nueva ejecución
    if option == 'job release':
        command = 'scontrol release ' + parameters[0]  # Libere un trabajo retenido anteriormente para comenzar la ejecución.
    if option == 'job suspend':
        command = 'scontrol suspend ' + parameters[0]  # Suspender un trabajo en ejecución. Si se pone en cola un trabajo suspendido, se colocará en estado retenido.
    if option == 'job resume':
        command = 'scontrol resume ' + parameters[0]  # Reanudar un trabajo previamente suspendido. Un trabajo suspendido libera sus CPU para su asignación a otros trabajos.
    if option == 'job requeue':
        command = 'scontrol requeue ' + parameters[0]  # Re-encolar un trabajo por lotes Slurm en ejecución, suspendido o terminado en estado pendiente.
    if option == 'job continue':
        command = 'scancel --signal=CONT ' + parameters[0]  # Reanuda la ejecución de un trabajo suspendido con sus recursos retenidos.
    if option == 'job stop':
        command = 'scancel --signal=STOP ' + parameters[0]  # Suspender un trabajo en ejecución y retiene los recursos asignados.
    if option == 'jobs group':
        group = run_command(request, 'groups user') or None
        if group:
            command = 'squeue -all --states=all -A ' + group.split(':')[1]
        else:
            return
    if option == 'groups user':
        command = 'groups ' + instance.__str__()

    # hpc script ########
    if option == 'partitions':
        command = 'sinfo --format=%R'
    if option == 'execute':
        command = 'sbatch "' + parameters[0] + '/' + parameters[1] + '"'

    # hpc nodes ########
    if option == 'nodes':
        command = 'scontrol show nodes -o'
    if option == 'nodes-partitions':
        command = 'sinfo -N --Format=all'
    if option == 'cpusload':
        command = 'sinfo -N --Format=nodelist,cpusload'
    if option == 'partitions-detail':
        command = 'sinfo --format="%R %a %D %N"'

    err, out = ssh.ssh_exec(username=instance.group_identifier(), private_key_path=instance.private_key.path, command=command)
    if err:
        messages.add_message(request, messages.ERROR, out)
    else:
        return out
