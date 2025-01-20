#!/bin/bash

echo "make sure packeages are installed again"
pip3 install -r requirements.txt

echo "Collecting static files..."
python3 manage.py collectstatic --noinput

echo "run migration..."
python3 manage.py migrate

echo "Starting server..."
#python3 manage.py runserver 0.0.0.0:8000
cd /app && gunicorn --config=gunicorn_conf/gunicorn_config_prod.py macroseat.wsgi