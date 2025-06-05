from __future__ import absolute_import, unicode_literals

import logging
import os
from importlib import import_module

# set the default Django settings module for the 'celery' program.
from celery import Celery
from celery.schedules import crontab
from django.conf import settings
from django.core.cache import cache
from django.db.models import Count

logger = logging.getLogger(__name__)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

app = Celery('project')
app.conf.broker_url = settings.BROKER_URL
app.conf.timezone = 'Europe/Bratislava'
app.conf.task_serializer = 'pickle'
app.conf.accept_content = ['json', 'pickle']
app.conf.worker_prefetch_multiplier = 1
app.conf.task_acks_late = True
app.conf.task_time_limit = 1 * 60 * 60
app.conf.worker_max_tasks_per_child = 20

app.conf.ONCE = {
    'backend': 'celery_once.backends.Redis',
    'settings': {
        'url': 'redis://{}:{}'.format(os.environ.get('REDIS_HOST'), os.environ.get('REDIS_PORT')) if os.environ.get('REDIS_HOST') else 'redis://localhost:6379/0',
        'default_timeout': 60 * 30
    }
}

# Using a string here means the worker don't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


@app.task(name='send_queued_mail', time_limit=40)
def send_queued_mail():
    from post_office.mail import send_queued

    task_lock = cache.lock('send-queued-mail-in-progress', timeout=50)
    if task_lock.acquire(blocking=False):
        send_queued(1)
        task_lock.release()


@app.task(name='send_failed_mails')
def send_failed_mails():
    from post_office.models import Email, STATUS, Log

    max_retries = getattr(settings, 'EMAIL_MAX_RETRIES', 5)
    # select FAILED email WHERE num_logs <= max
    query_set = Email.objects.annotate(num_logs=Count('logs')).filter(status=STATUS.failed).filter(num_logs__lte=max_retries).all()
    logs = []
    for mail in query_set:
        if mail.logs.count() == max_retries:
            logger.error('Unable to send mail with id: {} from: {}, to: {}'.format(mail.id, mail.from_email, mail.to))
            # here we create new log to stop sending over and over
            logs.append(Log(email=mail, status=STATUS.failed, message='maximum retries exceeded', exception_type='maximum retries exceeded'))
        else:
            mail.status = STATUS.queued
        mail.save()
    Log.objects.bulk_create(logs)



