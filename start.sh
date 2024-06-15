#!/bin/sh

until python manage.py migrate
do
    echo "..."
    sleep 10

done
python manage.py collectstatic --noinput

gunicorn --bind 0.0.0.0:8000 bg2b.wsgi