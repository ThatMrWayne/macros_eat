#!/bin/bash

echo "Collecting static files..."
python3 manage.py collectstatic --noinput

echo "run migration..."
python3 manage.py migrate

echo "Starting server..."
python3 manage.py runserver 0.0.0.0:8000