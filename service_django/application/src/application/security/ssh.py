# -*- coding: utf-8 -*-
from django.conf import settings
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _

import paramiko
import os


def test__private__and__public__key(instance):
    """The function verifies the private key in the server where your application runs and a public key in the server
    with which you want to establish a connection.

    :param LDAPUser or LDAPUserImported instance:
    :return returns true if the keys match and false otherwise:
    """
    hostname = settings.CLUSTER_SERVER_HOST
    port = int(settings.CLUSTER_SERVER_PORT)
    if isinstance(hostname, str) and \
            isinstance(port, int) and \
            isinstance(instance.identifier, str):
        pass
    else:
        raise Exception('Incorrect parameters format')

    ssh_client = paramiko.SSHClient()
    ssh_client.load_system_host_keys()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        k = paramiko.RSAKey.from_private_key_file(instance.private_key)
        ssh_client.connect(
            hostname=settings.CLUSTER_SERVER_HOST,
            port=int(settings.CLUSTER_SERVER_PORT),
            username=instance.group_identifier(),
            pkey=k
        )
    except Exception:
        return False
    else:
        return True
    finally:
        ssh_client.close()


def generate__private__and__public__key(instance, password):
    """
    The function generates a private key in the server where your application runs and a public key in the server
    with which you want to establish a connection.

    :param LDAPUser or LDAPUserImported instance:
    :param str password:
    :return:
    """
    hostname = settings.CLUSTER_SERVER_HOST
    port = int(settings.CLUSTER_SERVER_PORT)
    if isinstance(hostname, str) and \
            isinstance(port, int) and \
            isinstance(instance.identifier, str) and \
            isinstance(password, str):
        pass
    else:
        raise Exception('Incorrect parameters format')

    os.makedirs('%s/.ssh' % instance.___string___folder_path___(), exist_ok=True)
    key = paramiko.RSAKey.generate(1024)
    key.write_private_key_file('%s/.ssh/id_rsa' % instance.___string___folder_path___())
    with open(instance.___string___folder_path___() + '/.ssh/id_rsa.pub', "w") as public:
        public.write("%s %s" % (key.get_name(), key.get_base64()))
    public.close()

    pubkey = open(instance.___string___folder_path___() + '/.ssh/id_rsa.pub').read()

    ssh_client = paramiko.SSHClient()
    ssh_client.load_system_host_keys()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh_client.connect(
            hostname=hostname,
            port=port,
            username=instance.group_identifier(),
            password=password
        )
        h_input, h_output, h_error = ssh_client.exec_command('mkdir -p ~/.ssh/')
        error__private__and__public__key(h_error)
        h_input, h_output, h_error = ssh_client.exec_command('echo "%s" > ~/.ssh/authorized_keys' % pubkey)
        error__private__and__public__key(h_error)
        h_input, h_output, h_error = ssh_client.exec_command('chmod 600 ~/.ssh/authorized_keys')
        error__private__and__public__key(h_error)
        h_input, h_output, h_error = ssh_client.exec_command('chmod 700 ~/.ssh/')
        error__private__and__public__key(h_error)
    except Exception:
        message = _('HPC___SSH___MESSAGES_BadConnection')
        return message
    finally:
        ssh_client.close()

    instance.private_key = instance.___string___folder_path___() + '/.ssh/id_rsa'
    instance.public_key = instance.___string___folder_path___() + '/.ssh/id_rsa.pub'
    instance.save()
    return True


def error__private__and__public__key(h_error):
    error = h_error.read().decode('utf-8')
    if error != '':
        raise Exception(error)
