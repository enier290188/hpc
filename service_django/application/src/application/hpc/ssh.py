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
# ssh_client.connect(hostname, port, username, pkey)

# Ejecutar un comando en el servidor
# stdin, stdout, stderr = ssh_client.exec_command(command)

# Leer los resultados de la ejecución del comando del buffer de salida estandar y error standar
# err = stderr.read()
# out = stdout.read()

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


def config_logger():
    logger = logging.getLogger()
    hdlr = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    hdlr.setFormatter(formatter)
    logger.addHandler(hdlr)
    logger.setLevel(logging.INFO)


def ssh_exec(username, private_key_path, command):
    config_logger()

    ssh_client = paramiko.SSHClient()
    ssh_client.load_system_host_keys()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        k = paramiko.RSAKey.from_private_key_file(private_key_path)
        ssh_client.connect(
            hostname=settings.CLUSTER_SERVER_HOST,
            port=int(settings.CLUSTER_SERVER_PORT),
            username=username,
            pkey=k
        )
    except paramiko.AuthenticationException as authenticationException:
        message = _('HPC___SSH___MESSAGES_AuthenticationException')
        logging.info(_('HPC___SSH___MESSAGES_AuthenticationException'), authenticationException)
    except paramiko.BadHostKeyException as badHostKeyException:
        message = _('HPC___SSH___MESSAGES_BadHostKeyException')
    except paramiko.SSHException as sshException:
        message = _('HPC___SSH___MESSAGES_SSHException')
    except Exception as e:
        message = _('HPC___SSH___MESSAGES_Exception') % settings.CLUSTER_SERVER_HOST
    else:
        try:
            stdin, stdout, stderr = ssh_client.exec_command(command)
            err = stderr.read()
            if len(err) > 0:
                message = _('HPC___SSH___MESSAGES_CommandError') % err.decode('utf')
            else:
                out = stdout.read()
                return False, out
        except Exception as e:
            message = _('HPC___SSH___MESSAGES_OperationException')
    finally:
        ssh_client.close()
    return True, message


def ssh_sftp_putfo(username, private_key_path, file, remotopath):
    ssh_client = paramiko.SSHClient()
    ssh_client.load_system_host_keys()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        k = paramiko.RSAKey.from_private_key_file(private_key_path)
        ssh_client.connect(
            hostname=settings.CLUSTER_SERVER_HOST,
            port=int(settings.CLUSTER_SERVER_PORT),
            username=username,
            pkey=k
        )
    except paramiko.AuthenticationException as authenticationException:
        message = _('HPC___SSH___MESSAGES_AuthenticationException')
    except paramiko.BadHostKeyException as badHostKeyException:
        message = _('HPC___SSH___MESSAGES_BadHostKeyException')
    except paramiko.SSHException as sshException:
        message = _('HPC___SSH___MESSAGES_SSHException')
    except Exception as e:
        message = _('HPC___SSH___MESSAGES_Exception') % settings.CLUSTER_SERVER_HOST
    else:
        sftp = ssh_client.open_sftp()
        try:
            sftp.putfo(file, remotopath)
            return False
        except Exception as e:
            message = _('HPC___SSH___MESSAGES_UploadFilesException') % file.name
        finally:
            sftp.close()
    finally:
        ssh_client.close()
    return True, message


def ssh_sftp_getfo(username, private_key_path, remotopath, file):
    ssh_client = paramiko.SSHClient()
    ssh_client.load_system_host_keys()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        k = paramiko.RSAKey.from_private_key_file(private_key_path)
        ssh_client.connect(
            hostname=settings.CLUSTER_SERVER_HOST,
            port=int(settings.CLUSTER_SERVER_PORT),
            username=username,
            pkey=k
        )
    except paramiko.AuthenticationException as authenticationException:
        message = _('HPC___SSH___MESSAGES_AuthenticationException')
    except paramiko.BadHostKeyException as badHostKeyException:
        message = _('HPC___SSH___MESSAGES_BadHostKeyException')
    except paramiko.SSHException as sshException:
        message = _('HPC___SSH___MESSAGES_SSHException')
    except Exception as e:
        message = _('HPC___SSH___MESSAGES_Exception') % settings.CLUSTER_SERVER_HOST
    else:
        sftp = ssh_client.open_sftp()
        try:
            sftp.getfo(remotopath, file)
            return False
        except Exception as e:
            message = _('HPC___SSH___MESSAGES_DownloadFilesException') % remotopath.split('/')[-1]
        finally:
            sftp.close()
    finally:
        ssh_client.close()
    return True, message


def ssh_sftp_edit_file(username, private_key_path, remoto, content):
    ssh_client = paramiko.SSHClient()
    ssh_client.load_system_host_keys()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        k = paramiko.RSAKey.from_private_key_file(private_key_path)
        ssh_client.connect(
            hostname=settings.CLUSTER_SERVER_HOST,
            port=int(settings.CLUSTER_SERVER_PORT),
            username=username,
            pkey=k
        )
    except paramiko.AuthenticationException as authenticationException:
        message = _('HPC___SSH___MESSAGES_AuthenticationException')
    except paramiko.BadHostKeyException as badHostKeyException:
        message = _('HPC___SSH___MESSAGES_BadHostKeyException')
    except paramiko.SSHException as sshException:
        message = _('HPC___SSH___MESSAGES_SSHException')
    except Exception as e:
        message = _('HPC___SSH___MESSAGES_Exception') % settings.CLUSTER_SERVER_HOST
    else:
        sftp = ssh_client.open_sftp()
        try:
            file = sftp.file(remoto, "w", -1)
            file.write(content)
            file.flush()
            return False
        except Exception as e:
            message = _('HPC___SSH___MESSAGES_WriteIsNotPossible')
        finally:
            sftp.close()
    finally:
        ssh_client.close()
    return True, message


def ssh_sftp_open_file(username, private_key_path, remoto):
    ssh_client = paramiko.SSHClient()
    ssh_client.load_system_host_keys()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        k = paramiko.RSAKey.from_private_key_file(private_key_path)
        ssh_client.connect(
            hostname=settings.CLUSTER_SERVER_HOST,
            port=int(settings.CLUSTER_SERVER_PORT),
            username=username,
            pkey=k
        )
    except paramiko.AuthenticationException as authenticationException:
        message = _('HPC___SSH___MESSAGES_AuthenticationException')
    except paramiko.BadHostKeyException as badHostKeyException:
        message = _('HPC___SSH___MESSAGES_BadHostKeyException')
    except paramiko.SSHException as sshException:
        message = _('HPC___SSH___MESSAGES_SSHException')
    except Exception as e:
        message = _('HPC___SSH___MESSAGES_Exception') % settings.CLUSTER_SERVER_HOST
    else:
        sftp = ssh_client.open_sftp()
        try:
            file = sftp.file(remoto, "r", -1)
            file_content = file.read()
            return False, file_content
        except Exception as e:
            message = _('HPC___SSH___MESSAGES_OpenIsNotPossible')
        finally:
            sftp.close()
    finally:
        ssh_client.close()
    return True, message
