from django.apps import AppConfig

from health_check.plugins import plugin_dir


class HealthCheckConfig(AppConfig):
    name = 'sbcore.health_check.mail'

    def ready(self):
        from .backends import MailHealthCheck
        plugin_dir.register(MailHealthCheck)
