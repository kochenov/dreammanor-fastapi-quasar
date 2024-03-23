from celery.schedules import crontab
from celery import Celery

celery_app = Celery(
    "tasks",
    broker="redis://redis:6379",
    include=["app.tasks.tasks"],
    backend="redis://redis:6379",
    broker_connection_retry_on_startup=True
)
celery_app.conf.beat_schedule = {
    "call_endpoint": {
        "task": "parsing_links_task",
        "schedule": crontab(minute='*/5'),
    },
}
