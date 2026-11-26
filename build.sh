#!/usr/bin/env bash
# start.sh — Inicia Celery (Worker + Beat) y Gunicorn en Render


# El disco en Render es efímero, así que el archivo de control de Beat va a /tmp
celery -A core worker -l info --pool=solo --beat --schedule=/tmp/celerybeat-schedule &


# Inicia Gunicorn (la página web)
gunicorn core.wsgi:application