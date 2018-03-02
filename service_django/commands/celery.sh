#!/bin/bash

echo '***** Starting celery.sh *****'

echo "[makemigrations]"
python manage.py makemigrations --no-input

echo "[migrate]"
python manage.py migrate --no-input

echo "[worker]"
rm -f /service_django/volumes/celery/celeryd.pid
celery -A src worker \
--detach \
-l INFO \
--logfile /service_django/volumes/celery/celeryd.log \
--pidfile /service_django/volumes/celery/celeryd.pid \

echo "[beat]"
rm -f /service_django/volumes/celery/celerybeat.pid
celery -A src beat \
--detach \
-l INFO \
--logfile /service_django/volumes/celery/celerybeat.log \
--pidfile /service_django/volumes/celery/celerybeat.pid \
--schedule /service_django/volumes/celery/celerybeat-schedule.db \
--scheduler django_celery_beat.schedulers:DatabaseScheduler \
