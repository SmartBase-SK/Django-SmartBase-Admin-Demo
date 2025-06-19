import random
from datetime import datetime

from django.db import models
from django.utils.translation import gettext_lazy as _
from treebeard.mp_tree import MP_Node


class BaseDomainModel(models.Model):
    domain = models.ForeignKey("Domain", on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        abstract = True


class Domain(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Manufacturer(BaseDomainModel):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to="manufacturers", null=True, blank=True)

    def __str__(self):
        return self.name


class Category(BaseDomainModel,
               MP_Node,
               ):
    path = models.CharField(max_length=255)

    order_by = models.PositiveIntegerField(default=0, blank=False, null=False)

    is_active = models.BooleanField(default=True, verbose_name="Is active")
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to="categories", null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


RELEASE_CHOICES = [
    ("standard", "Standard Release"),
    ("limited", "Limited Edition"),
    ("exclusive", "Online Exclusive"),
]


class Product(BaseDomainModel):
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
    created = models.DateTimeField(auto_now_add=True, verbose_name="Created")
    related_products = models.ManyToManyField(
        "self",
        symmetrical=False,
        blank=True,
        related_name="related_to",
        verbose_name=_("Related Products")
    )
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

    available_from = models.DateField(
        null=True,
        blank=True,
        verbose_name=_("Available From")
    )

    is_featured = models.BooleanField(
        default=False,
        verbose_name=_("Featured Product")
    )

    stock_quantity = models.IntegerField(
        default=0,
        verbose_name=_("Stock Quantity")
    )

    tags = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text=_("Comma-separated list of tags"),
        verbose_name=_("Tags")
    )

    barcode = models.CharField(
        max_length=64,
        blank=True,
        null=True,
        unique=True,
        verbose_name=_("Ean code")
    )

    release_type = models.CharField(
        max_length=20,
        choices=RELEASE_CHOICES,
        default="standard",
        verbose_name=_("Release Type")
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")


class ProductImage(BaseDomainModel):
    product = models.ForeignKey(Product, related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="products")
    alt_text = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Image for {self.product.name}"


class Purchase(BaseDomainModel):
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


class PurchaseItem(BaseDomainModel):
    purchase = models.ForeignKey(Purchase, related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = _("Purchase Item")
        verbose_name_plural = _("Purchase Items")

    def __str__(self):
        return f"{self.product.name} – {self.price} €"


class EditableListModel(BaseDomainModel):
    name = models.CharField("Name", max_length=100, )
    value_1 = models.CharField("Value 1", max_length=100, )
    value_2 = models.CharField("Value 2", max_length=100, )

    class Meta:
        verbose_name = _("Editable list item")
        verbose_name_plural = _("Editable list items")

    def __str__(self):
        return self.name


class QuickSearchModel(BaseDomainModel):
    name = models.CharField("Name", max_length=100, )

    class Meta:
        verbose_name = _("Item")
        verbose_name_plural = _("Items")

    def __str__(self):
        return self.name


class ReorderModel(BaseDomainModel):
    name = models.CharField("Name", max_length=100, )
    order_by = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta:
        verbose_name = _("Item")
        verbose_name_plural = _("Items")

    def __str__(self):
        return self.name

class ListActionModel(BaseDomainModel):
    name = models.CharField("Name", max_length=100, )

    class Meta:
        verbose_name = _("Item")
        verbose_name_plural = _("Items")

    def __str__(self):
        return self.name
