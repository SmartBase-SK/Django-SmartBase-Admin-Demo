from django.apps import AppConfig


class ProjectConfig(AppConfig):
    name = 'project'

    def ready(self):
        super().ready()
        from project.tasks import register_celery_tasks
        register_celery_tasks()
