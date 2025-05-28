from django.core.management import BaseCommand


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            "run_stage",
            type=str,
            help="Build Phase: before_rsync, before_migrations, after_migrations",
        )

    def handle(self, *args, **options):
        pass

