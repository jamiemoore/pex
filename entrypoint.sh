#!/bin/sh
set -e
. /venv/bin/activate
exec gunicorn --bind 0.0.0.0:8080 --forwarded-allow-ips='*' src.pex.app:app