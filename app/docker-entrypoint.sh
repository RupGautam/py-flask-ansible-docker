#!/bin/sh

#flask db init

#flask db migrate -m "entries table"

#flask db upgrade

#alembic upgrade head && gunicorn wsgi:app --host 0.0.0.0 --port 8000 --reload

exec flask run
