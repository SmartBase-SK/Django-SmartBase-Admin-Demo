import random
from datetime import datetime, timedelta
from io import BytesIO

from PIL import Image
from django.core.files.base import ContentFile
from django.utils.text import slugify
from django.utils.timezone import make_aware

from project.catalog.models import (
    Domain,
    Manufacturer,
    Category,
    Product,
    ProductImage,
    Purchase,
    PurchaseItem,
)


def generate_image_file():
    image = Image.new("RGB", (100, 100), (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    buffer = BytesIO()
    image.save(buffer, format="PNG")
    return ContentFile(buffer.getvalue(), name="dummy.png")


def generate_dummy(full=True):
    PurchaseItem.objects.all().delete()
    Purchase.objects.all().delete()
    if full:
        ProductImage.objects.all().delete()
        Product.objects.all().delete()
        Category.objects.all().delete()
        Manufacturer.objects.all().delete()
        Domain.objects.all().delete()

        domain_1 = Domain.objects.create(name="www.domain1.com")
        domain_2 = Domain.objects.create(name="www.domain2.com")
        all_domains = [domain_1, domain_2]
    else:
        all_domains = Domain.objects.all()

    customer_names = [
        "Alice Johnson", "Bob Smith", "Charlie Davis", "Dana White", "Eve Thompson",
        "Frank Martin", "Grace Lee", "Henry Clark", "Isabel Scott", "Jack Turner",
        "Karen Mitchell", "Leo Rogers", "Mia Parker", "Noah Lewis", "Olivia Baker",
        "Paul Young", "Quinn Hill", "Rachel Adams", "Steve Morris", "Tina Carter"
    ]

    today = datetime.now().date()
    start_date = today - timedelta(days=365)

    for domain in all_domains:
        if full:
            manufacturers = []
            for name in ["Sony", "Apple", "Samsung", "Dell"]:
                manufacturers.append(Manufacturer.objects.create(name=name, domain=domain))

            # Domain-specific category names
            if domain == domain_1:
                electronics = Category.add_root(name="Electronics D1", slug="electronics-d1", domain=domain)
                phones = electronics.add_child(name="Phones D1", slug="phones-d1", domain=domain)
                laptops = electronics.add_child(name="Laptops D1", slug="laptops-d1", domain=domain)
            else:
                electronics = Category.add_root(name="Electronics D2", slug="electronics-d2", domain=domain)
                phones = electronics.add_child(name="Phones D2", slug="phones-d2", domain=domain)
                laptops = electronics.add_child(name="Laptops D2", slug="laptops-d2", domain=domain)

            categories = [phones, laptops]

            products = []
            for i in range(20):
                name = f"Product {i + 1} ({domain.name})"
                slug = slugify(name)
                sku = f"SKU-{domain.id}-{i + 1000}"
                price = round(random.uniform(50, 500), 2)
                is_active = random.choice([True, True, True, False])
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
        else:
            products = Product.objects.filter(domain = domain).all()

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
