from typing import Any

from django.contrib import admin
from django.db.models import F
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _
from django_smartbase_admin.admin.admin_base import (
    SBAdmin,
    SBAdminTableInline,
)
from django_smartbase_admin.admin.site import sb_admin_site
from django_smartbase_admin.admin.widgets import SBAdminTreeWidget
from django_smartbase_admin.engine.const import DETAIL_STRUCTURE_RIGHT_CLASS
from django_smartbase_admin.engine.fake_inline import SBAdminFakeInlineMixin
from django_smartbase_admin.engine.field import SBAdminField

from .models import Product, Category, Manufacturer, ProductImage, Purchase, PurchaseItem
from .. import settings


class ProductImageInline(SBAdminTableInline):
    model = ProductImage
    fields = ("image", "alt_text")
    extra = 1


def status_formatter(object_id, value):
    if value:
        label = "✅"
    else:
        label = "❌"
    return f'<span>{label}</span>'


class ProductSameManufacturerInline(SBAdminFakeInlineMixin, SBAdminTableInline):
    model = Product
    fields = ["name", "is_current_product"]
    readonly_fields = [*fields]
    can_delete = False
    verbose_name = "Product from the same manufacturer"
    verbose_name_plural = "Products from the same manufacturer"

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def filter_fake_inline_identifier_by_parent_instance(
            self, inline_queryset, parent_instance
    ):
        return inline_queryset.filter(manufacturer=parent_instance.manufacturer)

    @admin.display(description=_("Current product"))
    def is_current_product(self, obj):
        return (
            mark_safe(
                f'<svg class="w-20 h-20 text-success"><use xlink:href="#Check"></use></svg>'
            )
            if obj.pk == self.parent_instance.pk
            else ""
        )


@admin.register(Product, site=sb_admin_site)
class ProductSBAdmin(SBAdmin):
    model = Product
    inlines = [ProductImageInline]

    sbadmin_fake_inlines = [ProductSameManufacturerInline]
    sbadmin_list_display = (
        "name",
        "sku",
        SBAdminField(name="price", title=_("Price")),
        SBAdminField(name="is_active", title=_("Active"), python_formatter=status_formatter),
        SBAdminField(
            name="manufacturer",
            title="Manufacturer",
            annotate=F("manufacturer__name"),
            filter_field="manufacturer__name",
        ),
        "netto_weight",
        "package_dims",
        "product_dims",
    )
    # sbadmin_list_view_config = [
    #     {
    #         "name": _("Inactive"),
    #         "url_params": {
    #             "filterData": {"is_active": {"value":False}}
    #         },
    #     }]
    sbadmin_tabs = {
        "General": [
            "Appearance",
            "Delivery",
            "Base settings"
        ],
        "Media": [
            ProductImageInline,
        ],
    }

    fieldsets = [
        (
            "Appearance",
            {
                "fields": [
                    "name",
                    "description",
                ]
            },
        ),
        (
            "Delivery",
            {
                "fields": [
                    ("netto_weight",
                     "package_dims",
                     "product_dims",)
                ]
            },
        ),
        (
            "Base settings",
            {
                "classes": [DETAIL_STRUCTURE_RIGHT_CLASS],
                "fields": [
                    "is_active",
                    "slug",
                    "sku",
                    "categories",
                    "manufacturer",
                    "price",
                    "created",
                ],
            },
        ),
    ]
    readonly_fields = ['created']


@admin.register(Category, site=sb_admin_site)
class CategorySBAdmin(SBAdmin):
    model = Category
    sbadmin_list_display = ("name", SBAdminField(name="domain", title="Domain", annotate=F("domain__name")),
                            )
    search_fields = ["name"]

    change_list_template = "sb_admin/actions/tree_list.html"
    sbadmin_list_display_data = ["depth", "path"]
    sbadmin_list_reorder_field = "path"
    ordering = ["path"]


    # enable this to use tree widget to order categories
    use_tree_ordering = True
    fieldsets = [
        (
            None,
            {
                "fields": ["name", "slug", "image", "path",]
            },
        )
    ]

    def get_tabulator_definition(self, request) -> dict[str, Any]:
        tabulator_definition = super().get_tabulator_definition(request)
        if self.is_reorder_active(request):
            return tabulator_definition
        tabulator_definition["tabulatorOptions"].update(
            {
                "rendercategory": "no-render",
                "renderHorizontal": "no-render",
            }
        )
        return tabulator_definition


    def action_list_json(self, request, modifier, page_size=None):
        if not self.is_reorder_active(request):
            page_size = 999999
        action = self.sbadmin_list_action_class(self, request, page_size=page_size)
        data = action.get_json_data()
        return JsonResponse(data=data, safe=False)

    def tree_list_json(self, request, modifier, page_size=None):
        action = self.sbadmin_list_action_class(self, request, page_size=999999)

        final_data = SBAdminTreeWidget(order_by=["path"]).get_tree_data(
            request,
            action.get_data_queryset(),
            values=action.get_data_queryset_values(),
        )
        return JsonResponse(data=final_data, safe=False)

    def get_extra_context(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context["tree_strings"] = SBAdminTreeWidget(order_by=["path"]).tree_strings
        extra_context["tree_json_url"] = self.get_action_url("tree_list_json")
        extra_context["fancytree_filter_settings"] = {"fuzzy": False}
        return extra_context

    def changelist_view(self, request, extra_context=None):
        extra_context = self.get_extra_context(request, extra_context)
        return super().changelist_view(request, extra_context)


@admin.register(Manufacturer, site=sb_admin_site)
class ManufacturerSBAdmin(SBAdmin):
    model = Manufacturer
    sbadmin_list_display = ["name", SBAdminField(name="domain", title="Domain", annotate=F("domain__name"))]
    search_fields = ["name"]
    fieldsets = [
        (
            None,
            {
                "fields": ["name", "logo"]
            },
        )
    ]


class PurchaseItemInline(SBAdminTableInline):
    model = PurchaseItem
    fields = ("product", "price")
    extra = 1


@admin.register(Purchase, site=sb_admin_site)
class PurchaseSBAdmin(SBAdmin):
    model = Purchase
    inlines = [PurchaseItemInline]

    sbadmin_list_display = (
        "customer_name",
        SBAdminField(name="total_price", title=_("Price")),
        SBAdminField(name="created_at", title=_("Created At")),
        SBAdminField(name="domain", title="Domain", annotate=F("domain__name")),
    )

    search_fields = ["customer_name"]
    list_filter = ["created_at"]

    ordering = ["-created_at"]

    fieldsets = [
        (
            None,
            {
                "fields": [
                    "customer_name",
                    "total_price",
                ],
            },
        ),
        (
            _("Meta"),
            {
                "fields": ["created_at"],
            },
        ),
    ]

    readonly_fields = ["created_at"]
