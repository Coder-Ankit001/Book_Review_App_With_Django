#!/bin/bash
set -e
python manage.py collectstatic --noinput
python manage.py migrate --noinput
gunicorn --bind 0.0.0.0:8000 --workers 3 akashic_records.wsgi:application
