import random
from datetime import datetime, timedelta
from io import BytesIO

from PIL import Image
from django.core.files.base import ContentFile
from django.utils.text import slugify
from django.utils.timezone import make_aware

from project.catalog.models import (
    Manufacturer,
    Category,
    Product,
    ProductImage,
    Purchase,
    PurchaseItem,
    Domain,
)


def generate_dummy():
    # Clean up
    PurchaseItem.objects.all().delete()
    Purchase.objects.all().delete()
    ProductImage.objects.all().delete()
    Product.objects.all().delete()
    Category.objects.all().delete()
    Manufacturer.objects.all().delete()
    Domain.objects.all().delete()

    # Create Domains
    domain_1 = Domain.objects.create(name="www.domain1.com")
    domain_2 = Domain.objects.create(name="www.domain2.com")
    all_domains = [domain_1, domain_2]

    customer_names = [
        "Alice Johnson", "Bob Smith", "Charlie Davis", "Dana White", "Eve Thompson",
        "Frank Martin", "Grace Lee", "Henry Clark", "Isabel Scott", "Jack Turner",
        "Karen Mitchell", "Leo Rogers", "Mia Parker", "Noah Lewis", "Olivia Baker",
        "Paul Young", "Quinn Hill", "Rachel Adams", "Steve Morris", "Tina Carter"
    ]

    today = datetime.now().date()
    start_date = today - timedelta(days=365)

    for domain in all_domains:
        # Manufacturers
        manufacturers = []
        for name in ["Sony", "Apple", "Samsung", "Dell"]:
            manufacturers.append(Manufacturer.objects.create(name=name, domain=domain))

        # Categories
        electronics = Category.objects.create(name="Electronics", slug=f"electronics-{domain.id}", domain=domain)
        phones = Category.objects.create(name="Phones", slug=f"phones-{domain.id}", parent=electronics, domain=domain)
        laptops = Category.objects.create(name="Laptops", slug=f"laptops-{domain.id}", parent=electronics, domain=domain)
        categories = [phones, laptops]

        # Products
        products = []
        for i in range(20):
            name = f"Product {i + 1} ({domain.name})"
            slug = slugify(name)
            sku = f"SKU-{domain.id}-{i + 1000}"
            price = round(random.uniform(50, 500), 2)
            is_active = random.choice([True, True, True, False])  # ~25% inactive
            netto_weight = round(random.uniform(0.1, 5.0), 3)
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
                domain=domain
            )
            product.categories.add(random.choice(categories))
            ProductImage.objects.create(product=product, image=generate_image_file(), domain=domain)
            products.append(product)

        # Purchases & PurchaseItems for each day
        current_date = start_date
        while current_date <= today:
            for _ in range(random.randint(1, 3)):
                aware_date = make_aware(datetime.combine(current_date, datetime.min.time()))
                purchase = Purchase.objects.create(
                    customer_name=random.choice(customer_names),
                    total_price=0,
                    created_at=aware_date,
                    domain=domain
                )
                total = 0
                for _ in range(random.randint(1, 4)):
                    product = random.choice(products)
                    item_price = product.price
                    PurchaseItem.objects.create(
                        purchase=purchase,
                        product=product,
                        price=item_price,
                        domain=domain
                    )
                    total += item_price
                purchase.total_price = round(total, 2)
                purchase.save()
            current_date += timedelta(days=1)


def generate_image_file():
    """Create a dummy image file in memory."""
    image = Image.new("RGB", (100, 100), (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    buffer = BytesIO()
    image.save(buffer, format="PNG")
    return ContentFile(buffer.getvalue(), name="dummy.png")
