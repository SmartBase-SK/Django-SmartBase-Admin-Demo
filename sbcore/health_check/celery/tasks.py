
from celery import shared_task
from django.core.cache import cache
from django.utils import timezone


CELERY_HEALTH_CHECK_KEY = 'celery_health_check_datetime'


@shared_task()
def create_cache_timestamp():
    cache.set(CELERY_HEALTH_CHECK_KEY, timezone.now())
