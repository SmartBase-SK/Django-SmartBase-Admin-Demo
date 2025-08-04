from celery.schedules import crontab

from project.services import generate_dummy
from project.config.celery import app


@app.task(name="send_revision_notifications_task")
def generate_dummy_task():
    generate_dummy(full=False)


def register_celery_tasks():
    app.conf.beat_schedule.update(
        {
            "generate_dummy_task": {
                "task": "generate_dummy_task",
                "schedule": crontab(hour=7, minute=0),
            },
        }
    )
