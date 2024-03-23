#!/bin/bash

alembic upgrade head

gunicorn app.main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --config /usr/src/app/gunicorn_conf.py