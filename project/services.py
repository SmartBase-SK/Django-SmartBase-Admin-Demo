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
    PurchaseItem, EditableListModel, QuickSearchModel, ReorderModel, ListActionModel,
)


def generate_image_file():
    image = Image.new("RGB", (100, 100), (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    buffer = BytesIO()
    image.save(buffer, format="PNG")
    return ContentFile(buffer.getvalue(), name="dummy.png")


def cat_slug(name, suffix):
    return slugify(f"{name} {suffix}")


def generate_dummy(full=True):
    PurchaseItem.objects.all().delete()
    Purchase.objects.all().delete()
    if full:
        ProductImage.objects.all().delete()
        Product.objects.all().delete()
        Category.objects.all().delete()
        Manufacturer.objects.all().delete()
        Domain.objects.all().delete()
        EditableListModel.objects.all().delete()
        QuickSearchModel.objects.all().delete()
        ReorderModel.objects.all().delete()
        ListActionModel.objects.all().delete()

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
    start_date = today - timedelta(days=2 * 365)

    for domain in all_domains:
        if full:
            for i in range(1, 1500):
                EditableListModel.objects.create(
                    name=f"Item {i} - {domain.name}",
                    domain=domain,
                    value_1=f"Value",
                    value_2=f"Value"
                )
                QuickSearchModel.objects.create(
                    domain=domain,
                    name=f"Item {i} - {domain.name}",
                )
                ReorderModel.objects.create(
                    domain=domain,
                    name=f"Item {i} - {domain.name}",
                )
                ListActionModel.objects.create(
                    domain=domain,
                    name=f"Item {i} - {domain.name}",
                )

            manufacturers = []
            for name in ["Sony", "Apple", "Samsung", "Dell"]:
                manufacturers.append(Manufacturer.objects.create(name=name, domain=domain))

            if domain == domain_1:
                suffix = "d1"

                # 1. Electronics
                electronics = Category.add_root(name="Electronics", slug=cat_slug("Electronics", suffix), domain=domain)
                computers = electronics.add_child(name="Computers", slug=cat_slug("Computers", suffix), domain=domain)
                laptops = computers.add_child(name="Laptops", slug=cat_slug("Laptops", suffix), domain=domain)
                gaming_laptops = laptops.add_child(name="Gaming Laptops", slug=cat_slug("Gaming Laptops", suffix), domain=domain)
                ultrabooks = laptops.add_child(name="Ultrabooks", slug=cat_slug("Ultrabooks", suffix), domain=domain)

                # 2. Mobile
                mobile = Category.add_root(name="Mobile", slug=cat_slug("Mobile", suffix), domain=domain)
                smartphones = mobile.add_child(name="Smartphones", slug=cat_slug("Smartphones", suffix), domain=domain)
                android = smartphones.add_child(name="Android Phones", slug=cat_slug("Android Phones", suffix), domain=domain)
                ios = smartphones.add_child(name="iPhones", slug=cat_slug("iPhones", suffix), domain=domain)

                accessories = mobile.add_child(name="Accessories", slug=cat_slug("Accessories", suffix), domain=domain)
                chargers = accessories.add_child(name="Chargers", slug=cat_slug("Chargers", suffix), domain=domain)
                cases = accessories.add_child(name="Cases", slug=cat_slug("Cases", suffix), domain=domain)

                # 3. Home & Kitchen
                home = Category.add_root(name="Home & Kitchen", slug=cat_slug("Home & Kitchen", suffix), domain=domain)
                appliances = home.add_child(name="Appliances", slug=cat_slug("Appliances", suffix), domain=domain)
                kitchen = appliances.add_child(name="Kitchen Appliances", slug=cat_slug("Kitchen Appliances", suffix), domain=domain)
                coffee_machines = kitchen.add_child(name="Coffee Machines", slug=cat_slug("Coffee Machines", suffix), domain=domain)

                # 4. Furniture
                furniture = Category.add_root(name="Furniture", slug=cat_slug("Furniture", suffix), domain=domain)
                living_room = furniture.add_child(name="Living Room", slug=cat_slug("Living Room", suffix), domain=domain)
                sofas = living_room.add_child(name="Sofas", slug=cat_slug("Sofas", suffix), domain=domain)
                bedroom = furniture.add_child(name="Bedroom", slug=cat_slug("Bedroom", suffix), domain=domain)
                beds = bedroom.add_child(name="Beds", slug=cat_slug("Beds", suffix), domain=domain)

                # 5. Sports & Outdoors
                sports = Category.add_root(name="Sports & Outdoors", slug=cat_slug("Sports & Outdoors", suffix), domain=domain)
                fitness = sports.add_child(name="Fitness", slug=cat_slug("Fitness", suffix), domain=domain)
                yoga = fitness.add_child(name="Yoga", slug=cat_slug("Yoga", suffix), domain=domain)
                yoga_mats = yoga.add_child(name="Yoga Mats", slug=cat_slug("Yoga Mats", suffix), domain=domain)

                # 6. Clothing
                clothing = Category.add_root(name="Clothing", slug=cat_slug("Clothing", suffix), domain=domain)
                men = clothing.add_child(name="Men", slug=cat_slug("Men", suffix), domain=domain)
                men_shirts = men.add_child(name="Shirts", slug=cat_slug("Men Shirts", suffix), domain=domain)
                women = clothing.add_child(name="Women", slug=cat_slug("Women", suffix), domain=domain)
                women_dresses = women.add_child(name="Dresses", slug=cat_slug("Women Dresses", suffix), domain=domain)

                # 7. Footwear
                footwear = Category.add_root(name="Footwear", slug=cat_slug("Footwear", suffix), domain=domain)
                sneakers = footwear.add_child(name="Sneakers", slug=cat_slug("Sneakers", suffix), domain=domain)
                boots = footwear.add_child(name="Boots", slug=cat_slug("Boots", suffix), domain=domain)

                # 8. Books
                books = Category.add_root(name="Books", slug=cat_slug("Books", suffix), domain=domain)
                fiction = books.add_child(name="Fiction", slug=cat_slug("Fiction", suffix), domain=domain)
                mystery = fiction.add_child(name="Mystery", slug=cat_slug("Mystery", suffix), domain=domain)
                nonfiction = books.add_child(name="Non-Fiction", slug=cat_slug("Non-Fiction", suffix), domain=domain)

                # 9. Beauty & Health
                beauty = Category.add_root(name="Beauty & Health", slug=cat_slug("Beauty & Health", suffix), domain=domain)
                skincare = beauty.add_child(name="Skincare", slug=cat_slug("Skincare", suffix), domain=domain)
                serums = skincare.add_child(name="Face Serums", slug=cat_slug("Face Serums", suffix), domain=domain)
                makeup = beauty.add_child(name="Makeup", slug=cat_slug("Makeup", suffix), domain=domain)

                # 10. Toys & Baby
                toys = Category.add_root(name="Toys & Baby", slug=cat_slug("Toys & Baby", suffix), domain=domain)
                infants = toys.add_child(name="Infant Toys", slug=cat_slug("Infant Toys", suffix), domain=domain)
                educational = toys.add_child(name="Educational Toys", slug=cat_slug("Educational Toys", suffix), domain=domain)

                # Final category list (only deep leaves)
                categories = [
                    gaming_laptops, ultrabooks, android, ios, chargers, cases,
                    coffee_machines, sofas, beds, yoga_mats,
                    men_shirts, women_dresses, sneakers, boots,
                    mystery, nonfiction, serums, makeup,
                    infants, educational
                ]



            else:

                suffix = "d2"

                # 1. Fashion

                fashion = Category.add_root(name="Fashion", slug=cat_slug("Fashion", suffix), domain=domain)

                menswear = fashion.add_child(name="Menswear", slug=cat_slug("Menswear", suffix), domain=domain)

                formal = menswear.add_child(name="Formal", slug=cat_slug("Formal", suffix), domain=domain)

                shirts = formal.add_child(name="Shirts", slug=cat_slug("Shirts", suffix), domain=domain)

                casual = menswear.add_child(name="Casual", slug=cat_slug("Casual", suffix), domain=domain)

                womenswear = fashion.add_child(name="Womenswear", slug=cat_slug("Womenswear", suffix), domain=domain)

                evening = womenswear.add_child(name="Evening Dresses", slug=cat_slug("Evening Dresses", suffix), domain=domain)

                workwear = womenswear.add_child(name="Workwear", slug=cat_slug("Workwear", suffix), domain=domain)

                # 2. Accessories

                accessories = Category.add_root(name="Accessories", slug=cat_slug("Accessories", suffix), domain=domain)

                bags = accessories.add_child(name="Bags", slug=cat_slug("Bags", suffix), domain=domain)

                backpacks = bags.add_child(name="Backpacks", slug=cat_slug("Backpacks", suffix), domain=domain)

                handbags = bags.add_child(name="Handbags", slug=cat_slug("Handbags", suffix), domain=domain)

                jewelry = accessories.add_child(name="Jewelry", slug=cat_slug("Jewelry", suffix), domain=domain)

                watches = jewelry.add_child(name="Watches", slug=cat_slug("Watches", suffix), domain=domain)

                # 3. Smart Tech

                tech = Category.add_root(name="Smart Tech", slug=cat_slug("Smart Tech", suffix), domain=domain)

                smart_home = tech.add_child(name="Smart Home", slug=cat_slug("Smart Home", suffix), domain=domain)

                security = smart_home.add_child(name="Security Cameras", slug=cat_slug("Security Cameras", suffix), domain=domain)

                assistants = smart_home.add_child(name="Voice Assistants", slug=cat_slug("Voice Assistants", suffix), domain=domain)

                wearables = tech.add_child(name="Wearables", slug=cat_slug("Wearables", suffix), domain=domain)

                trackers = wearables.add_child(name="Fitness Trackers", slug=cat_slug("Fitness Trackers", suffix), domain=domain)

                watches_smart = wearables.add_child(name="Smart Watches", slug=cat_slug("Smart Watches", suffix), domain=domain)

                # 4. Health

                health = Category.add_root(name="Health & Wellness", slug=cat_slug("Health & Wellness", suffix), domain=domain)

                nutrition = health.add_child(name="Nutrition", slug=cat_slug("Nutrition", suffix), domain=domain)

                supplements = nutrition.add_child(name="Supplements", slug=cat_slug("Supplements", suffix), domain=domain)

                protein = nutrition.add_child(name="Protein Powders", slug=cat_slug("Protein Powders", suffix), domain=domain)

                fitness = health.add_child(name="Fitness", slug=cat_slug("Fitness", suffix), domain=domain)

                yoga = fitness.add_child(name="Yoga", slug=cat_slug("Yoga", suffix), domain=domain)

                mats = yoga.add_child(name="Yoga Mats", slug=cat_slug("Yoga Mats", suffix), domain=domain)

                # 5. Beauty

                beauty = Category.add_root(name="Beauty", slug=cat_slug("Beauty", suffix), domain=domain)

                skincare = beauty.add_child(name="Skincare", slug=cat_slug("Skincare", suffix), domain=domain)

                moisturizers = skincare.add_child(name="Moisturizers", slug=cat_slug("Moisturizers", suffix), domain=domain)

                cleansers = skincare.add_child(name="Cleansers", slug=cat_slug("Cleansers", suffix), domain=domain)

                makeup = beauty.add_child(name="Makeup", slug=cat_slug("Makeup", suffix), domain=domain)

                lipsticks = makeup.add_child(name="Lipsticks", slug=cat_slug("Lipsticks", suffix), domain=domain)

                # 6. Kids

                kids = Category.add_root(name="Kids & Baby", slug=cat_slug("Kids & Baby", suffix), domain=domain)

                baby_gear = kids.add_child(name="Baby Gear", slug=cat_slug("Baby Gear", suffix), domain=domain)

                strollers = baby_gear.add_child(name="Strollers", slug=cat_slug("Strollers", suffix), domain=domain)

                toys = kids.add_child(name="Toys", slug=cat_slug("Toys", suffix), domain=domain)

                puzzles = toys.add_child(name="Puzzles", slug=cat_slug("Puzzles", suffix), domain=domain)

                # 7. Books

                books = Category.add_root(name="Books", slug=cat_slug("Books", suffix), domain=domain)

                fiction = books.add_child(name="Fiction", slug=cat_slug("Fiction", suffix), domain=domain)

                sci_fi = fiction.add_child(name="Sci-Fi", slug=cat_slug("Sci-Fi", suffix), domain=domain)

                drama = fiction.add_child(name="Drama", slug=cat_slug("Drama", suffix), domain=domain)

                nonfiction = books.add_child(name="Non-Fiction", slug=cat_slug("Non-Fiction", suffix), domain=domain)

                biography = nonfiction.add_child(name="Biography", slug=cat_slug("Biography", suffix), domain=domain)

                # 8. Grocery

                grocery = Category.add_root(name="Grocery & Gourmet", slug=cat_slug("Grocery & Gourmet", suffix), domain=domain)

                pantry = grocery.add_child(name="Pantry Essentials", slug=cat_slug("Pantry Essentials", suffix), domain=domain)

                spices = pantry.add_child(name="Spices", slug=cat_slug("Spices", suffix), domain=domain)

                oils = pantry.add_child(name="Cooking Oils", slug=cat_slug("Cooking Oils", suffix), domain=domain)

                beverages = grocery.add_child(name="Beverages", slug=cat_slug("Beverages", suffix), domain=domain)

                coffee = beverages.add_child(name="Coffee & Tea", slug=cat_slug("Coffee & Tea", suffix), domain=domain)

                # 9. Automotive

                auto = Category.add_root(name="Automotive", slug=cat_slug("Automotive", suffix), domain=domain)

                car_care = auto.add_child(name="Car Care", slug=cat_slug("Car Care", suffix), domain=domain)

                cleaners = car_care.add_child(name="Interior Cleaners", slug=cat_slug("Interior Cleaners", suffix), domain=domain)

                accessories_auto = auto.add_child(name="Accessories", slug=cat_slug("Car Accessories", suffix), domain=domain)

                phone_mounts = accessories_auto.add_child(name="Phone Mounts", slug=cat_slug("Phone Mounts", suffix), domain=domain)

                # 10. Pet Supplies

                pets = Category.add_root(name="Pet Supplies", slug=cat_slug("Pet Supplies", suffix), domain=domain)

                dogs = pets.add_child(name="Dogs", slug=cat_slug("Dogs", suffix), domain=domain)

                dog_food = dogs.add_child(name="Dog Food", slug=cat_slug("Dog Food", suffix), domain=domain)

                grooming = dogs.add_child(name="Grooming", slug=cat_slug("Dog Grooming", suffix), domain=domain)

                cats = pets.add_child(name="Cats", slug=cat_slug("Cats", suffix), domain=domain)

                litter = cats.add_child(name="Litter Boxes", slug=cat_slug("Litter Boxes", suffix), domain=domain)

                categories = [

                    shirts, casual, evening, workwear,

                    backpacks, handbags, watches,

                    security, assistants, trackers, watches_smart,

                    supplements, protein, mats,

                    moisturizers, cleansers, lipsticks,

                    strollers, puzzles,

                    sci_fi, drama, biography,

                    spices, oils, coffee,

                    cleaners, phone_mounts,

                    dog_food, grooming, litter

                ]

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
            products = Product.objects.filter(domain=domain).all()

        # Assign related products randomly after all products are created
        for product in products:
            others = [p for p in products if p != product]
            related_sample = random.sample(others, k=min(len(others), random.randint(2, 4)))
            product.related_products.set(related_sample)

        current_date = start_date
        while current_date <= today:
            if random.random() >= 0.7:
                continue
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
