from django.shortcuts import redirect
from django.urls import reverse

from project.catalog.models import Product, Purchase


def home_redirect(request):
    return redirect("/sb-admin")


from django.shortcuts import redirect
from django.urls import reverse


def redirect_to_last_product(request):
    tab = request.GET.get('tab', '')
    last_product = Product.objects.last()

    url = reverse("sb_admin:catalog_product_change", kwargs={"object_id": last_product.id})
    return redirect(f"{url}#{tab}")

def redirect_to_last_purchase(request):
    tab = request.GET.get('tab', '')
    last = Purchase.objects.last()

    url = reverse("sb_admin:catalog_purchase_change", kwargs={"object_id": last.id})
    return redirect(f"{url}#{tab}")
