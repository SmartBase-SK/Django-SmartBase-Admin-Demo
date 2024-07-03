import time

from django.core.cache import cache
from django.utils import timezone
from health_check.backends import BaseHealthCheckBackend
from health_check.exceptions import (
    ServiceUnavailable
)

from .tasks import create_cache_timestamp, CELERY_HEALTH_CHECK_KEY


class CeleryHealthCheck(BaseHealthCheckBackend):
    def check_status(self):
        try:
            create_cache_timestamp.apply_async()
            celery_result = cache.get(CELERY_HEALTH_CHECK_KEY, None)
            if not celery_result:
                celery_result = timezone.now()
                cache.set(CELERY_HEALTH_CHECK_KEY, celery_result, timeout=None)
            if celery_result < timezone.now() - timezone.timedelta(minutes=15):
                self.add_error(ServiceUnavailable("Celery cached last result: {}".format(celery_result)))

        except IOError as e:
            self.add_error(ServiceUnavailable("IOError"), e)
        except BaseException as e:
            self.add_error(ServiceUnavailable("Unknown error"), e)
