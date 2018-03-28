# -*- coding: utf-8 -*-

# ****************
# Paramiko v2.4.0
# **************

# Se utiliza la librería paramiko para establecer conexiones ssh y sftp al servidor remoto

# Iniciar un cliente SSH #
# ssh_client = paramiko.SSHClient()

# Establecer política por defecto para localizar la llave del host localmente
# ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Establecer una conexión
# ssh_client.connect(hostname, port, username, password)

# Ejecutar un comando en el servidor
# h_input, h_output, h_error = ssh_client.exec_command(command)

# Leer los resultados de la ejecución del comando del buffer de salida estandar y error standar
# error = h_error.read()
# output = h_output.read()

# Abrir una conexión sftp
# sftp = ssh_client.open_sftp()

# Subir el archivo almacenado en local a la ruta en el servidor remoto
# output = sftp.put(local, remoto)


# Subir el archivo almacenado en local a la ruta en el servidor remoto
# output = sftp.get(remoto, local)

# Cerrar la conexión sftp
# sftp.close()

# Cerrar la conexión
# ssh_client.close()

from django.utils.translation import ugettext_lazy as _
from django.conf import settings
import paramiko
import logging


def ssh_exec(username, password, command):
    result = dict()
    ssh_client = paramiko.SSHClient()
    ssh_client.load_system_host_keys()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh_client.connect(
            hostname=settings.CLUSTER_SERVER_HOST,
            port=int(settings.CLUSTER_SERVER_PORT),
            username=username,
            password=password,
        )
        h_input, h_output, h_error = ssh_client.exec_command(command)
    except Exception as e:
        logging.exception(_('APPLICATION___HPC___SSH___MESSAGES_ServerNotAvailable'), e)
        result.update({
            'HAS_ERROR': True,
            'MESSAGE': _('APPLICATION___HPC___SSH___MESSAGES_ServerNotAvailable')
        })
    else:
        error = h_error.read().decode('utf-8')
        output = h_output.read()
        if error == '':
            result.update({
                'HAS_ERROR': False,
                'OUTPUT': str(output)[2:-3]
            })
        else:
            result.update({
                'HAS_ERROR': True,
                'MESSAGE': error
            })
    finally:
        ssh_client.close()
    return result


def ssh_sftp_put(username, password, local, remoto):
    result = dict()
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh_client.connect(
            hostname=settings.CLUSTER_SERVER_HOST,
            port=settings.CLUSTER_SERVER_PORT,
            username=username,
            password=password
        )
    except Exception as e:
        logging.exception(_('APPLICATION___HPC___SSH___MESSAGES_ServerNotAvailable'), e)
        result.update({
            'HAS_ERROR': True,
            'MESSAGE': _('APPLICATION___HPC___SSH___MESSAGES_ServerNotAvailable')
        })
    else:
        sftp = ssh_client.open_sftp()
        try:
            output = sftp.put(local, remoto)
            result.update({
                'HAS_ERROR': False
            })
        except Exception as e:
            logging.exception(_('APPLICATION___HPC___SSH___MESSAGES_UploadFilesException'), e)
            result.update({
                'HAS_ERROR': True,
                'MESSAGE': _('APPLICATION___HPC___SSH___MESSAGES_UploadFilesException')
            })
        sftp.close()
    finally:
        ssh_client.close()
    return result


def ssh_sftp_get(username, password, remoto, local):
    result = dict()
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh_client.connect(
            hostname=settings.CLUSTER_SERVER_HOST,
            port=settings.CLUSTER_SERVER_PORT,
            username=username,
            password=password
        )
    except Exception as e:
        logging.exception(_('APPLICATION___HPC___SSH___MESSAGES_ServerNotAvailable'), e)
        result.update({
            'HAS_ERROR': True,
            'MESSAGE': _('APPLICATION___HPC___SSH___MESSAGES_ServerNotAvailable')
        })
    else:
        sftp = ssh_client.open_sftp()
        try:
            output = sftp.get(remoto, local)
            result.update({
                'HAS_ERROR': False
            })
        except Exception as e:
            logging.exception(_('APPLICATION___HPC___SSH___MESSAGES_UploadFilesException'), e)
            result.update({
                'HAS_ERROR': True,
                'MESSAGE': _('APPLICATION___HPC___SSH___MESSAGES_DownloadFilesException'),
            })
        sftp.close()
    finally:
        ssh_client.close()
    return result
