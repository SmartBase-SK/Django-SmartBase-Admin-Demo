"""SMTP email backend class."""
import base64
import os
import smtplib

import post_office
from constance import config
from django.conf import settings
from django.core.mail.backends.smtp import EmailBackend
from django.core.mail.message import sanitize_address


class ErrorEmailBackend(EmailBackend):
    def __init__(self, host=None, port=None, username=None, password=None, use_tls=None, fail_silently=False, use_ssl=None, timeout=None, ssl_keyfile=None, ssl_certfile=None, **kwargs):
        host = os.environ.get('STAGING_SMTP_HOST', '')
        port = int(os.environ.get('STAGING_SMTP_PORT', '25'))
        username = os.environ.get('STAGING_SMTP_USER', '')
        password = base64.b64decode(os.environ.get('STAGING_SMTP_PASSWORD_ENCODED', '')).decode('utf-8')
        use_tls = True
        timeout = 15.0
        super().__init__(host, port, username, password, use_tls, fail_silently, use_ssl, timeout, ssl_keyfile, ssl_certfile, **kwargs)

    def send_messages(self, email_messages):
        for email_message in email_messages:
            email_message.from_email = os.environ.get('STAGING_SMTP_USER', '')
        return super().send_messages(email_messages)


class EmailAllToAdminBackend(EmailBackend):

    def _send(self, email_message):
        """A helper method that does the actual sending."""
        if not email_message.recipients():
            return False
        email_message.subject += ' (Original to: {})'.format(",".join(email_message.to))
        encoding = email_message.encoding or settings.DEFAULT_CHARSET
        admin_mails = []
        for admin in settings.ADMINS:
            if isinstance(admin, tuple):
                admin_mails.append(admin[1])
            else:
                admin_mails.append(admin)

        from_email = sanitize_address(email_message.from_email, encoding)
        recipients = config.TESTING_MAILS.split(";")
        message = email_message.message()
        try:
            self.connection.sendmail(from_email, recipients, message.as_bytes(linesep='\r\n'))
        except smtplib.SMTPException:
            if not self.fail_silently:
                raise
            return False
        return True
