#!/bin/bash

if [[ "${1}" == "celery" ]]; then
  celery --app=app.tasks.celery:celery_app worker --loglevel=INFO --beat
#elif [[ "${1}" == "beat" ]]; then
##  celery -A app.tasks.celery:celery_app beat  --loglevel=INFO
#  celery -A app.tasks.celery:celery_app beat -l info
elif [[ "${1}" == "flower" ]]; then
  celery --app=app.tasks.celery:celery_app flower
 fi