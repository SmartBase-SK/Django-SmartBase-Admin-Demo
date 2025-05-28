from django.db import models
from django.utils.translation import gettext_lazy as _
import random
from datetime import datetime, timedelta
from django.utils.timezone import make_aware

class Manufacturer(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to="manufacturers", null=True, blank=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to="categories", null=True, blank=True)
    parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.SET_NULL, related_name="children")

    node_order_by = ['name']

    class Meta:
        app_label = "catalog"
        abstract = False
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(
            blank=True, null=True, verbose_name=_("Description")
        )
    slug = models.SlugField(unique=True)
    sku = models.CharField(max_length=100, unique=True)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.SET_NULL, null=True, blank=True)
    categories = models.ManyToManyField(Category, related_name="products", blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    netto_weight = models.DecimalField(
        max_digits=6,
        blank=True,
        null=True,
        decimal_places=3,
        verbose_name=_("Netto weight (kg)"),
    )
    package_dims = models.CharField(
        max_length=32,
        blank=True,
        null=True,
        verbose_name=_("Package dimensions"),

    )
    product_dims = models.CharField(
        max_length=48,
        blank=True,
        null=True,
        verbose_name=_("Product dimensions"),

    )
    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="products")
    alt_text = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Image for {self.product.name}"


class Purchase(models.Model):
    customer_name = models.CharField(max_length=255, verbose_name=_("Customer Name"))
    total_price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name=_("Total Price")
    )
    created_at = models.DateTimeField(verbose_name=_("Created At"))

    class Meta:
        verbose_name = _("Purchase")
        verbose_name_plural = _("Purchases")
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.customer_name} – {self.total_price} €"

    @staticmethod
    def create_dummy():
        customer_names = ["Alice", "Bob", "Charlie", "Dana", "Eve", "Frank", "Grace"]

        Purchase.objects.all().delete()

        start_date = datetime(datetime.now().year, 1, 1)
        for month in range(1, 12):
            for _ in range(random.randint(5, 15)):  # Random purchases per month
                date = start_date.replace(month=month, day=random.randint(1, 28))
                Purchase.objects.create(
                    customer_name=random.choice(customer_names),
                    total_price=round(random.uniform(20, 200), 2),
                    created_at=date,
                )
class PurchaseItem(models.Model):
    purchase = models.ForeignKey(Purchase, related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = _("Purchase Item")
        verbose_name_plural = _("Purchase Items")

    def __str__(self):
        return f"{self.product.name} – {self.price} €"
