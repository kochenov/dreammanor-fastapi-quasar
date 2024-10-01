from celery.schedules import crontab
from celery import Celery

from app.core import settings

celery_app = Celery(
    "tasks",
    broker=f"redis://{settings.REDIS_HOST}:6379/0",
    include=["app.tasks.tasks"],
    backend=f"redis://{settings.REDIS_HOST}:6379/0",
    broker_connection_retry_on_startup=True,
)

celery_app.conf.beat_schedule = {
    "call_endpoint": {
        "task": "parsing_links_task",
        "schedule": crontab(minute=f"*/{settings.CELERY_TASK_INTERVAL}"),
    },
}
