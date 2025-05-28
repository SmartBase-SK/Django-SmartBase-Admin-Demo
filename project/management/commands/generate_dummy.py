from django.core.management.base import BaseCommand

from project.services import generate_dummy


class Command(BaseCommand):
    help = "Fill the database with dummy manufacturers, products, and purchases."

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS("Seeding data..."))
        generate_dummy()
        self.stdout.write(self.style.SUCCESS("✅ Dummy data created successfully."))
