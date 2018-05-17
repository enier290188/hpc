# -*- coding: utf-8 -*-
from django.conf import settings
import paramiko
import os


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
    print(instance.___string___folder_path___() + '/.ssh/id_rsa.pub', password, hostname, port)
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

    print('#########', hostname, port, instance.group_identifier(), password)
    ssh_client = paramiko.SSHClient()
    ssh_client.load_system_host_keys()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=hostname, port=port, username=instance.group_identifier(), password=password)
    try:
        h_input, h_output, h_error = ssh_client.exec_command('mkdir -p ~/.ssh/')
        error__private__and__public__key(h_error)
        h_input, h_output, h_error = ssh_client.exec_command('echo "%s" > ~/.ssh/authorized_keys' % pubkey)
        error__private__and__public__key(h_error)
        h_input, h_output, h_error = ssh_client.exec_command('chmod 600 ~/.ssh/authorized_keys')
        error__private__and__public__key(h_error)
        h_input, h_output, h_error = ssh_client.exec_command('chmod 700 ~/.ssh/')
        error__private__and__public__key(h_error)
    except Exception as e:
        raise Exception(e.__str__())
    finally:
        ssh_client.close()

    instance.private_key = instance.___string___folder_path___() + '/.ssh/id_rsa'
    instance.public_key = instance.___string___folder_path___() + '/.ssh/id_rsa.pub'
    instance.save()
    '''
    ssh_client = paramiko.SSHClient()
    ssh_client.load_system_host_keys()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=hostname, port=port, username=instance.__str__(), key_filename=instance.private_key.path)
    try:
        h_input, h_output, h_error = ssh_client.exec_command('ls')
        error__private__and__public__key(h_error)
    except Exception as e:
        raise Exception(e.__str__())
    else:
        print(h_output.read().decode('utf-8'))
    finally:
        ssh_client.close()
    '''


def error__private__and__public__key(h_error):
    error = h_error.read().decode('utf-8')
    if error != '':
        raise Exception(error)
