from __future__ import absolute_import, unicode_literals

import logging
import os

from django.conf import settings

# set the default Django settings module for the 'celery' program.
from celery import Celery

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
