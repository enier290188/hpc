# -*- coding: utf-8 -*-
from ...ssh import ssh_exec
import json


def exec_cmd(instance, parameters):
    username = "42110027" # instance.username
    password = "12345*abc" # instance.get__password
    # retorna tres variables (STATUS, MESSAGE, DATA)
    if isinstance(parameters, list):
        val = parameters[0]
    else:
        val = parameters
    cmd = str()
    if val == 'keys':
        cmd = 'squeue -all'
    if val == 'jobs all':
        cmd = 'squeue -all'
    if val == 'jobs group':
        result = ssh_exec(username, password, 'groups ' + username)
        if not result['HAS_ERROR']:
            cmd = 'squeue -all -A ' + result['OUTPUT'].split(' : ')[1]
    if val == 'jobs user':
        cmd = 'squeue -all --users=' + parameters[1]
    if val == 'detail job':
        cmd = 'scontrol show job -o ' + parameters[1]
    result = ssh_exec(username, password, cmd)
    if result['HAS_ERROR']:
        return True, result['MESSAGE']
    return False, generate_data(val, result['OUTPUT'])


def generate_data(val, output):
    __json__ = dict()
    if val == 'keys':
        output = output.split('\\n')
        keys = output[1].split()
        __json__['keys'] = keys
    if val == 'jobs all' or val == 'jobs group' or val == 'jobs user':
        output = output.split('\\n')
        l = list()
        for data in output[2:]:
            if len(data.split()) > 9:
                l.append(data.split()[0:8])
                l[-1].append(" ".join(data.split()[8:]))

            else:
                l.append(data.split())
        __json__['data'] = l
    if val == 'detail job':
        keys = [
            'JobId', 'JobName', 'UserId', 'GroupId', 'Priority', 'Account', 'QOS', 'JobState',
            'Reason', 'Requeue', 'Restarts', 'RunTime', 'TimeLimit', 'TimeMin', 'SubmitTime',
            'EligibleTime', 'StartTime', 'EndTime', 'Deadline', 'PreemptTime', 'SuspendTime',
            'SecsPreSuspend', 'Partition', 'AllocNode:Sid', 'ReqNodeList', 'NodeList', 'BatchHost',
            'NumNodes', 'NumCPUs', 'NumTasks', 'CPUs/Task', 'TRES', 'Command', 'WorkDir', 'StdErr',
            'StdIn', 'StdOut'
        ]
        fields = output.split()
        for key in keys:
            i = 0
            for field in fields:
                if field.startswith(key):
                    if key == 'TRES':
                        __json__['mem'] = field.split(',')[1].split('=')[1]
                    else:
                        __json__[key] = field.split('=')[1]
                    break
            fields.pop(i)
    return __json__
