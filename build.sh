#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate
python manage.py crear_grupos
python manage.py crear_sitio
python manage.py cargar_zapatos