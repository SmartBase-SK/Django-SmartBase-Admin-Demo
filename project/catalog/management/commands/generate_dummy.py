import random
from datetime import datetime, timedelta
from django.core.management.base import BaseCommand
from django.utils.text import slugify
from django.utils.timezone import make_aware
from project.catalog.models import (
    Manufacturer,
    Category,
    Product,
    ProductImage,
    Purchase,
    PurchaseItem,
)
from django.core.files.base import ContentFile
from io import BytesIO
from PIL import Image


def generate_image_file():
    """Create a dummy image file in memory."""
    image = Image.new("RGB", (100, 100), (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    buffer = BytesIO()
    image.save(buffer, format="PNG")
    return ContentFile(buffer.getvalue(), name="dummy.png")


class Command(BaseCommand):
    help = "Fill the database with dummy manufacturers, products, and purchases."

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS("Seeding data..."))
        PurchaseItem.objects.all().delete()
        Manufacturer.objects.all().delete()
        Category.objects.all().delete()
        Product.objects.all().delete()
        Purchase.objects.all().delete()

        # Manufacturers
        manufacturers = []
        for name in ["Sony", "Apple", "Samsung", "Dell"]:
            manufacturers.append(Manufacturer.objects.create(name=name))

        # Categories
        electronics = Category.objects.create(name="Electronics", slug="electronics")
        phones = Category.objects.create(name="Phones", slug="phones", parent=electronics)
        laptops = Category.objects.create(name="Laptops", slug="laptops", parent=electronics)

        categories = [phones, laptops]

        # Products
        products = []
        for i in range(20):
            name = f"Product {i + 1}"
            slug = slugify(name)
            sku = f"SKU-{i + 1000}"
            price = round(random.uniform(50, 500), 2)
            is_active = random.choice([True, True, True, False])  # ~25% inactive

            netto_weight = round(random.uniform(0.1, 5.0), 3)  # in kg
            dims = lambda: f"{random.randint(5, 50)}x{random.randint(5, 50)}x{random.randint(1, 30)} cm"

            product = Product.objects.create(
                name=name,
                slug=slug,
                sku=sku,
                price=price,
                is_active=is_active,
                manufacturer=random.choice(manufacturers),
                netto_weight=netto_weight,
                package_dims=dims(),
                product_dims=dims(),
            )
            product.categories.add(random.choice(categories))
            ProductImage.objects.create(product=product, image=generate_image_file())
            products.append(product)

        # Purchases & PurchaseItems for each day in the past year
        customer_names = [
            "Alice Johnson",
            "Bob Smith",
            "Charlie Davis",
            "Dana White",
            "Eve Thompson",
            "Frank Martin",
            "Grace Lee",
            "Henry Clark",
            "Isabel Scott",
            "Jack Turner",
            "Karen Mitchell",
            "Leo Rogers",
            "Mia Parker",
            "Noah Lewis",
            "Olivia Baker",
            "Paul Young",
            "Quinn Hill",
            "Rachel Adams",
            "Steve Morris",
            "Tina Carter"
        ]

        today = datetime.now().date()
        start_date = today - timedelta(days=365)

        current_date = start_date
        while current_date <= today:
            for _ in range(random.randint(1, 5)):  # Random purchases per day
                aware_date = make_aware(datetime.combine(current_date, datetime.min.time()))
                purchase = Purchase.objects.create(
                    customer_name=random.choice(customer_names),
                    total_price=0,
                    created_at=aware_date,
                )
                total = 0
                for _ in range(random.randint(1, 5)):
                    product = random.choice(products)
                    item_price = product.price
                    PurchaseItem.objects.create(purchase=purchase, product=product, price=item_price)
                    total += item_price
                purchase.total_price = round(total, 2)
                purchase.save()
            current_date += timedelta(days=1)

        self.stdout.write(self.style.SUCCESS("✅ Dummy data created successfully."))
