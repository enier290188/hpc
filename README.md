# HPC 
> Web application for the HPC.

The application works in two modes:
+ ***development***
+ ***production***

To work you must go to the root of the project and write depending on the way you want the application to work:
``` [bash]
sudo ./docker_development.sh –compose
sudo ./docker_production.sh –compose
```

But first inside the folder ***environment/*** you must create the files:
+ ***application.env***
+ ***development.env***
+ ***production.env***

Also in the folders ***service_nginx/nginx/ssl/*** and ***service_pgadmin/pgadmin/ssl/*** you must create the files:
+ ***certificate.crt***
+ ***certificate_key.key***

The ***application.env*** file must have the environment variables:
```
# APPLICATION
APPLICATION=application
```

The ***development.env*** file must have the environment variables:
```
# APPLICATION
APPLICATION_ENVIRONMENT=development
APPLICATION_VERSION=latest
# SERVICE_POSTGRES
POSTGRES_HOST=service_postgres
POSTGRES_PORT=5432
POSTGRES_DB=hpc
POSTGRES_USER=hpc
POSTGRES_PASSWORD=p455word
PGDATA=/var/lib/postgresql/data
# SERVICE_PGADMIN
PGADMIN_HOST=service_pgadmin
PGADMIN_PORT=444
PGADMIN_DEFAULT_EMAIL=hpc.pgadmin@domain.com
PGADMIN_DEFAULT_PASSWORD=p455word
PGADMIN_ENABLE_TLS=True
PGADMIN_SERVER_NAME=hpc.pgadmin.domain.com
# SERVICE_RABBITMQ
RABBITMQ_HOST=service_rabbitmq
RABBITMQ_PORT=5672
RABBITMQ_DEFAULT_USER=hpc
RABBITMQ_DEFAULT_PASS=p455word
# SERVICE_DJANGO
DJANGO_HOST=service_django
DJANGO_HTTP_SOCKET_HOST=0.0.0.0
DJANGO_PORT=8080
DJANGO_SECRET_KEY='d^1v!34h_+0jjl%yh5))vb2j0j=)=&jygpym$%u$+ja6i14@ge'
# SERVICE_DJANGO_EMAILS
DJANGO_EMAIL_HOST=192.168.195.111
DJANGO_EMAIL_PORT=25
DJANGO_EMAIL_USER_NOREPLY='noreply@domain.com'
# SERVICE_DJANGO_LDAP
DJANGO_LDAP_SERVER_HOST=192.168.195.110
DJANGO_LDAP_SERVER_USER='cn=admin,dc=domain,dc=com'
DJANGO_LDAP_SERVER_PASSWORD='p455word'
DJANGO_LDAP_SERVER_GROUPS_SEARCH_BASE='ou=Groups,dc=domain,dc=com'
DJANGO_LDAP_SERVER_GROUPS_LIST='HPC001 HPC002 HPC003 HPC004 HPC005'
DJANGO_LDAP_SERVER_GROUPS_GROUP_CN='HPC001'
DJANGO_LDAP_SERVER_GROUPS_GROUP_GIDNUMBER='5001'
DJANGO_LDAP_SERVER_USERS_SEARCH_BASE='ou=AllPeople,dc=domain,dc=com'
DJANGO_LDAP_SERVER_USERS_HPC_SEARCH_BASE='ou=People,dc=domain,dc=com'
DJANGO_LDAP_SERVER_USERS_HOMEDIRECTORY='/home/CLUSTER/'
# SERVICE_DJANGO_CELERY_RESULTS
DJANGO_CELERY_RESULTS_HOST=service_django_celery_results
# SERVICE_DJANGO_CELERY_BEAT
DJANGO_CELERY_BEAT_HOST=service_django_celery_beat
# SERVICE_NGINX
NGINX_HOST=service_nginx
NGINX_PORT_HTTP=80
NGINX_PORT_HTTPS=443
NGINX_SERVER_NAME=hpc.domain.com
```

The ***production.env*** file must have the environment variables:
```
# APPLICATION
APPLICATION_ENVIRONMENT=production
APPLICATION_VERSION=1.0
# SERVICE_POSTGRES
POSTGRES_HOST=service_postgres
POSTGRES_PORT=5432
POSTGRES_DB=hpc
POSTGRES_USER=hpc
POSTGRES_PASSWORD=p455word
PGDATA=/var/lib/postgresql/data
# SERVICE_PGADMIN
PGADMIN_HOST=service_pgadmin
PGADMIN_PORT=444
PGADMIN_DEFAULT_EMAIL=hpc.pgadmin@domain.com
PGADMIN_DEFAULT_PASSWORD=p455word
PGADMIN_ENABLE_TLS=True
PGADMIN_SERVER_NAME=hpc.pgadmin.domain.com
# SERVICE_RABBITMQ
RABBITMQ_HOST=service_rabbitmq
RABBITMQ_PORT=5672
RABBITMQ_DEFAULT_USER=hpc
RABBITMQ_DEFAULT_PASS=p455word
# SERVICE_DJANGO
DJANGO_HOST=service_django
DJANGO_HTTP_SOCKET_HOST=0.0.0.0
DJANGO_PORT=8080
DJANGO_SECRET_KEY='d^1v!34h_+0jjl%yh5))vb2j0j=)=&jygpym$%u$+ja6i14@ge'
# SERVICE_DJANGO_EMAILS
DJANGO_EMAIL_HOST=192.168.195.111
DJANGO_EMAIL_PORT=25
DJANGO_EMAIL_USER_NOREPLY='noreply@domain.com'
# SERVICE_DJANGO_LDAP
DJANGO_LDAP_SERVER_HOST=192.168.195.110
DJANGO_LDAP_SERVER_USER='cn=admin,dc=domain,dc=com'
DJANGO_LDAP_SERVER_PASSWORD='p455word'
DJANGO_LDAP_SERVER_GROUPS_SEARCH_BASE='ou=Groups,dc=domain,dc=com'
DJANGO_LDAP_SERVER_GROUPS_LIST='HPC001 HPC002 HPC003 HPC004 HPC005'
DJANGO_LDAP_SERVER_GROUPS_GROUP_CN='HPC001'
DJANGO_LDAP_SERVER_GROUPS_GROUP_GIDNUMBER='5001'
DJANGO_LDAP_SERVER_USERS_SEARCH_BASE='ou=AllPeople,dc=domain,dc=com'
DJANGO_LDAP_SERVER_USERS_HPC_SEARCH_BASE='ou=People,dc=domain,dc=com'
DJANGO_LDAP_SERVER_USERS_HOMEDIRECTORY='/home/CLUSTER/'
# SERVICE_DJANGO_CELERY_RESULTS
DJANGO_CELERY_RESULTS_HOST=service_django_celery_results
# SERVICE_DJANGO_CELERY_BEAT
DJANGO_CELERY_BEAT_HOST=service_django_celery_beat
# SERVICE_NGINX
NGINX_HOST=service_nginx
NGINX_PORT_HTTP=80
NGINX_PORT_HTTPS=443
NGINX_SERVER_NAME=hpc.domain.com
```
