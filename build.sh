#!/usr/bin/env bash
# exit on error
set -o errexit

#poetry install
pip install -r requirment.txt
web: gunicorn ABCblog.wsgi --log-file -

python manage.py collectstatic --no-input
python manage.py migrate