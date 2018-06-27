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
# ssh_client.connect(hostname, port, username, key_filename)

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


def ssh_exec(username, private_key_path, command):
    logger = paramiko.util.logging.getLogger()
    hdlr = logging.FileHandler('/app.log')
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    hdlr.setFormatter(formatter)
    logger.addHandler(hdlr)
    logger.setLevel(logging.INFO)

    result = dict()
    ssh_client = paramiko.SSHClient()
    ssh_client.load_system_host_keys()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    boolean = True
    while boolean:
        try:
            k = paramiko.RSAKey.from_private_key_file(private_key_path)
            ssh_client.connect(
                hostname=settings.CLUSTER_SERVER_HOST,
                port=int(settings.CLUSTER_SERVER_PORT),
                username=username,
                # key_filename=private_key_path,
                pkey=k
            )
            h_input, h_output, h_error = ssh_client.exec_command(command)
        except Exception as e:
            logging.debug(e)
            logging.info('Error connecting to Server')
            logging.exception('Error connecting to Server', e)
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
                    'OUTPUT': output
                })
            else:
                result.update({
                    'HAS_ERROR': True,
                    'MESSAGE': error
                })
            boolean = False
        finally:
            ssh_client.close()
    return result


def ssh_sftp_putfo(username, private_key_path, file, remotopath):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(
        hostname=settings.CLUSTER_SERVER_HOST,
        port=settings.CLUSTER_SERVER_PORT,
        username=username,
        key_filename=private_key_path
    )
    sftp = ssh_client.open_sftp()
    sftp.putfo(file, remotopath)
    sftp.close()
    ssh_client.close()


def ssh_sftp_getfo(username, private_key_path, remotopath, file):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(
        hostname=settings.CLUSTER_SERVER_HOST,
        port=settings.CLUSTER_SERVER_PORT,
        username=username,
        key_filename=private_key_path
    )
    sftp = ssh_client.open_sftp()
    sftp.getfo(remotopath, file)
    sftp.close()
    ssh_client.close()


def ssh_sftp_put(username, private_key_path, local, remoto):
    result = dict()
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    boolean = True
    while boolean:
        try:
            ssh_client.connect(
                hostname=settings.CLUSTER_SERVER_HOST,
                port=settings.CLUSTER_SERVER_PORT,
                username=username,
                key_filename=private_key_path
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
            boolean = False
        finally:
            ssh_client.close()
    return result


def ssh_sftp_get(username, private_key_path, remoto, local):
    result = dict()
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh_client.connect(
            hostname=settings.CLUSTER_SERVER_HOST,
            port=settings.CLUSTER_SERVER_PORT,
            username=username,
            key_filename=private_key_path
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
            logging.exception(_('APPLICATION___HPC___SSH___MESSAGES_DownloadFilesException'), e)
            result.update({
                'HAS_ERROR': True,
                'MESSAGE': _('APPLICATION___HPC___SSH___MESSAGES_DownloadFilesException'),
            })
        sftp.close()
    finally:
        ssh_client.close()
    return result


def ssh_sftp_edit_file(username, private_key_path, remoto, content):
    ssh_client = paramiko.SSHClient()
    ssh_client.load_system_host_keys()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    boolean = True
    while boolean:
        try:
            ssh_client.connect(
                hostname=settings.CLUSTER_SERVER_HOST,
                port=int(settings.CLUSTER_SERVER_PORT),
                username=username,
                key_filename=private_key_path
            )

            sftp = ssh_client.open_sftp()
            file = sftp.file(remoto, "w", -1)
            file.write(content)
            file.flush()
            sftp.close()
        except Exception as e:
            logging.exception('Write file is not posible.', e)
        else:
            return False
        finally:
            ssh_client.close()


def ssh_sftp_open_file(username, private_key_path, remoto):
    ssh_client = paramiko.SSHClient()
    ssh_client.load_system_host_keys()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    boolean = True
    while boolean:
        try:
            ssh_client.connect(
                hostname=settings.CLUSTER_SERVER_HOST,
                port=int(settings.CLUSTER_SERVER_PORT),
                username=username,
                key_filename=private_key_path
            )
            sftp = ssh_client.open_sftp()
            file = sftp.file(remoto, "r", -1)
            file_content = file.read()
            sftp.close()
        except Exception as e:
            logging.exception('Open file is not posible.', e)
        else:
            return file_content
        finally:
            ssh_client.close()
