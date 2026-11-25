#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input --clear
python manage.py migrate
python manage.py loaddata productos.json || true
python manage.py loaddata usuarios.json || true