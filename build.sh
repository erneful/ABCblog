#!/usr/bin/env bash
# Exit on error.
set -o errexit

pip install -r requirements.txt


python app/manage.py check --deploy --fail-level ERROR
python app/manage.py collectstatic --no-input
p#!/usr/local/bin/python3.9.5

#-*- coding: utf-8 -*-
import re
import sys

from gunicorn.app.wsgiapp import run


if __name__ == '__main__':
        sys.argv[0] = re.sub(r'(-script\.pyw|\.exe)?$','',sys.argv[0])
        sys.exit(run())ython app/manage.py migrate