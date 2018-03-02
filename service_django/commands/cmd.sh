#!/bin/bash

echo '***** Starting cmd.sh *****'

sh /service_django/commands/celery.sh

echo "[uwsgi]"
uwsgi \
        --chdir=./ \
        --module=wsgi.application.wsgi:application \
        --env DJANGO_SETTINGS_MODULE=settings.application.${APPLICATION_ENVIRONMENT} \
        --master \
        --http-socket=${DJANGO_HTTP_SOCKET_HOST}:${DJANGO_PORT} \
        --processes=5 \
        --threads=5 \
        --max-requests=5000 \
        --vacuum \
        --python-autoreload=1 \
