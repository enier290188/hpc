# -*- coding: utf-8 -*-
# django modules import
from django.contrib import messages

# python libraries import
import json

# user modules import
from . import ssh


def edit_file(request, remoto, content):
    instance = request.___APPLICATION___SECURITY___USER___
    return ssh.ssh_sftp_edit_file(username=instance.group_identifier(), private_key_path=instance.private_key.path, remoto=remoto, content=content)


def open_file(request, remoto):
    instance = request.___APPLICATION___SECURITY___USER___
    return ssh.ssh_sftp_open_file(username=instance.group_identifier(), private_key_path=instance.private_key.path, remoto=remoto)


def generate_data_dict(request, option, parameters=None):
    __dict__ = dict()
    str_in_bytes = run_command(request, option, parameters=parameters)
    if str_in_bytes:
        string_in_utf8 = str_in_bytes.decode('utf-8').rstrip('\n')
        if option == 'envVars':
            tmp = string_in_utf8.split()
            __dict__ = {'USER': tmp[0], 'UID': tmp[1], 'HOME': tmp[2], 'PATH': tmp[3], 'SHELL': tmp[4]}
        if option == 'path':
            __dict__ = string_in_utf8
        if option == 'list' or option == 'goto':
            folders = list()
            files = list()
            lines = string_in_utf8.split('\n')
            for line in lines[1:]:
                array = columns7(line)
                e = {'inode': array[0], 'name': array[7], 'size': array[3], 'date': array[4], 'time': array[5].split('.')[0]}
                if array[1][0] == 'd':
                    folders.append(e)
                else:
                    files.append(e)
            __dict__['folders'] = folders
            __dict__['files'] = files
        return __dict__
    if option in ['goto', 'rename', 'delete', 'folder', 'file', 'paste']:
        return generate_data_dict(request, 'list', parameters[:1])
    return None


def generate_data_json(request, option, parameters=None):
    __dict__ = generate_data_dict(request, option, parameters=parameters)
    if __dict__:
        return json.dumps(generate_data_dict(request, option, parameters=parameters))


def run_command(request, option, parameters=None):
    instance = request.___APPLICATION___SECURITY___USER___
    command = 'ls'
    if option == 'envVars':
        command = 'echo $USER $UID $HOME $PATH $SHELL'
    if option == 'path':
        command = 'pwd'
    if parameters:
        parameters = list_escape(parameters)
        if option == 'list':
            command = 'ls --full-time -igGh --group-directories-first "' + parameters[0] + '"'
        if option == 'goto':
            command = 'ls --full-time -igGh --group-directories-first "' + parameters[0] + '/' + parameters[1] + '"'
        if len(parameters) > 1:
            if option == 'rename':
                command = 'mv ' \
                          '"' + parameters[0] + '/' + parameters[1] + '" ' \
                          '"' + parameters[0] + '/' + parameters[2] + '"'
            if option == 'folder':
                command = 'mkdir ' \
                          '"' + parameters[0] + '/' + parameters[1] + '"'
            if option == 'file':
                command = 'touch ' \
                          '"' + parameters[0] + '/' + parameters[1] + '"'
            if option == 'paste':
                command = 'cp '
                for file in parameters[2:]:
                    command += '"' + parameters[1] + '/' + file + '" '
                command += '"' + parameters[0] + '" '
            if option == 'delete':
                string = ''
                for p in parameters[1:]:
                    string += ' "' + parameters[0] + '/' + p + '"'
                command = 'rm -r' + string
    err, out = ssh.ssh_exec(username=instance.group_identifier(), private_key_path=instance.private_key.path, command=command)
    if err:
        messages.add_message(request, messages.ERROR, out)
    else:
        return out


def list_escape(array):
    new_array = list()
    for string in array:
        new_array.append(escape(string))
    return new_array


def escape(string):
    character_map = {
        '$': '\$',
        '"': '\\"',
        "'": "\'",
        '\\': '\\\\',
    }
    s = ''
    for index, char in enumerate(string):
        if char in character_map.keys():
            s += character_map[char]
        else:
            s += char
    return s


def columns7(line):
    array = list()
    space = False
    counter = 0
    string = ''
    for index, char in enumerate(line.lstrip()):
        if counter < 7:
            if space:
                if char != " ":
                    string += char
                    space = False
            else:
                if char != " ":
                    string += char
                else:
                    array.append(string)
                    string = ''
                    counter += 1
                    space = True
        else:
            string += char
    array.append(string)
    return array
