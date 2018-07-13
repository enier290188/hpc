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
    logger = paramiko.util.logging.getLogger()
    hdlr = logging.FileHandler('/service_django/error.log')
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
        logging.info(_('HPC___SSH___MESSAGES_BadHostKeyException'), badHostKeyException)
    except paramiko.SSHException as sshException:
        message = _('HPC___SSH___MESSAGES_SSHException')
        logging.info(_('HPC___SSH___MESSAGES_SSHException'), sshException)
    except Exception as e:
        message = _('HPC___SSH___MESSAGES_Exception') % settings.CLUSTER_SERVER_HOST
        logging.info(_('HPC___SSH___MESSAGES_Exception') % settings.CLUSTER_SERVER_HOST, e)
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
            logging.info(_('HPC___SSH___MESSAGES_OperationException'), e)
    finally:
        ssh_client.close()
    return True, message


def ssh_sftp_putfo(username, private_key_path, file, remotopath):
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
        logging.info(_('HPC___SSH___MESSAGES_BadHostKeyException'), badHostKeyException)
    except paramiko.SSHException as sshException:
        message = _('HPC___SSH___MESSAGES_SSHException')
        logging.info(_('HPC___SSH___MESSAGES_SSHException'), sshException)
    except Exception as e:
        message = _('HPC___SSH___MESSAGES_Exception') % settings.CLUSTER_SERVER_HOST
        logging.info(_('HPC___SSH___MESSAGES_Exception') % settings.CLUSTER_SERVER_HOST, e)
    else:
        sftp = ssh_client.open_sftp()
        try:
            sftp.putfo(file, remotopath)
            return False
        except Exception as e:
            message = _('HPC___SSH___MESSAGES_UploadFilesException') % file.name
            logging.info(_('HPC___SSH___MESSAGES_UploadFilesException'), e)
        finally:
            sftp.close()
    finally:
        ssh_client.close()
    return True, message


def ssh_sftp_getfo(username, private_key_path, remotopath, file):
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
        logging.info(_('HPC___SSH___MESSAGES_BadHostKeyException'), badHostKeyException)
    except paramiko.SSHException as sshException:
        message = _('HPC___SSH___MESSAGES_SSHException')
        logging.info(_('HPC___SSH___MESSAGES_SSHException'), sshException)
    except Exception as e:
        message = _('HPC___SSH___MESSAGES_Exception') % settings.CLUSTER_SERVER_HOST
        logging.info(_('HPC___SSH___MESSAGES_Exception') % settings.CLUSTER_SERVER_HOST, e)
    else:
        sftp = ssh_client.open_sftp()
        try:
            sftp.getfo(remotopath, file)
            return False
        except Exception as e:
            message = _('HPC___SSH___MESSAGES_DownloadFilesException') % remotopath.split('/')[-1]
            logging.info(_('HPC___SSH___MESSAGES_DownloadFilesException'), e)
        finally:
            sftp.close()
    finally:
        ssh_client.close()
    return True, message


def ssh_sftp_edit_file(username, private_key_path, remoto, content):
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
        logging.info(_('HPC___SSH___MESSAGES_BadHostKeyException'), badHostKeyException)
    except paramiko.SSHException as sshException:
        message = _('HPC___SSH___MESSAGES_SSHException')
        logging.info(_('HPC___SSH___MESSAGES_SSHException'), sshException)
    except Exception as e:
        message = _('HPC___SSH___MESSAGES_Exception') % settings.CLUSTER_SERVER_HOST
        logging.info(_('HPC___SSH___MESSAGES_Exception') % settings.CLUSTER_SERVER_HOST, e)
    else:
        sftp = ssh_client.open_sftp()
        try:
            file = sftp.file(remoto, "w", -1)
            file.write(content)
            file.flush()
            return False
        except Exception as e:
            message = _('HPC___SSH___MESSAGES_WriteIsNotPossible')
            logging.info(_('HPC___SSH___MESSAGES_WriteIsNotPossible'), e)
        finally:
            sftp.close()
    finally:
        ssh_client.close()
    return True, message


def ssh_sftp_open_file(username, private_key_path, remoto):
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
        logging.info(_('HPC___SSH___MESSAGES_BadHostKeyException'), badHostKeyException)
    except paramiko.SSHException as sshException:
        message = _('HPC___SSH___MESSAGES_SSHException')
        logging.info(_('HPC___SSH___MESSAGES_SSHException'), sshException)
    except Exception as e:
        message = _('HPC___SSH___MESSAGES_Exception') % settings.CLUSTER_SERVER_HOST
        logging.info(_('HPC___SSH___MESSAGES_Exception') % settings.CLUSTER_SERVER_HOST, e)
    else:
        sftp = ssh_client.open_sftp()
        try:
            file = sftp.file(remoto, "r", -1)
            file_content = file.read()
            return False, file_content
        except Exception as e:
            message = _('HPC___SSH___MESSAGES_OpenIsNotPossible')
            logging.info(_('HPC___SSH___MESSAGES_OpenIsNotPossible'), e)
        finally:
            sftp.close()
    finally:
        ssh_client.close()
    return True, message
