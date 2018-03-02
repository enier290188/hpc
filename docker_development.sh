#!/bin/bash

# Variables defined will be exported into this script's environment:
set -a
source ./environment/application.env
source ./environment/development.env

# Give permission to execute.
sudo chmod +x ./service_django/commands/cmd.sh
sudo chmod +x ./service_django/commands/entrypoint.sh
sudo chmod +x ./service_django/commands/celery.sh

if [ "$1" == '--compose' ]
then
    # Create network
    docker network create network_${APPLICATION}

    # To avoid substituting nginx variables, which also use the shell syntax, we'll specify only the variables that will be used in our nginx config:
    NGINX_ARGUMENTS='$DJANGO_HOST:$DJANGO_PORT:$NGINX_SERVER_NAME:$NGINX_PORT_HTTP:$NGINX_PORT_HTTPS'
    # Now lets populate our nginx config templates to get an actual nginx config (which will be loaded into our nginx container):
    envsubst "$NGINX_ARGUMENTS" < ./service_nginx/nginx/nginx_envsubst.conf > ./service_nginx/nginx/nginx.conf

    # Let's populate the variables in our compose file template, then deploy it!
    cat docker.yml | envsubst | docker-compose -f - -p ${APPLICATION} build
    cat docker.yml | envsubst | docker-compose -f - -p ${APPLICATION} up -d --force-recreate

    # Necessary for the pgadmin volume to work.
    docker exec container_${APPLICATION}_${PGADMIN_HOST} chown apache:1000 -R /var/lib/pgadmin/

elif [ "$1" == '--bash' ]
then
    docker exec -i -t container_${APPLICATION}_${DJANGO_HOST} /bin/bash

else
    echo "[options]"
    echo "--compose"
    echo "--bash"

fi
