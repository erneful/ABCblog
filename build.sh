#!/usr/bin/env bash
# Exit on error.
set -o errexit

pip install -r requirements.txt

python app/manage.py check --deploy --fail-level ERROR
python app/manage.py collectstatic --no-input
python app/manage.py migrate