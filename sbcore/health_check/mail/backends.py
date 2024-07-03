import logging

import post_office
from django.utils import timezone

from health_check.backends import BaseHealthCheckBackend
from health_check.exceptions import ServiceUnavailable
from post_office.models import Email

logger = logging.getLogger(__name__)


class MailHealthCheck(BaseHealthCheckBackend):
    """Health check for email."""

    def check_status(self):
        """Check Emails by checking mail status"""
        if Email.objects.filter(status=post_office.models.STATUS.failed).count():
            self.add_error(ServiceUnavailable("Failed emails"))
        if Email.objects.filter(status=post_office.models.STATUS.queued, last_updated__lte=(timezone.now() - timezone.timedelta(minutes=5))).count():
            self.add_error(ServiceUnavailable("Failed emails - queued too long"))
