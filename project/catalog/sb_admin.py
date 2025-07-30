import json
from typing import Any

from django.contrib import admin, messages
from django.db.models import (
    F,
    Q,
)
from django.http import HttpResponse
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _
from django_smartbase_admin.admin.admin_base import (
    SBAdmin,
    SBAdminTableInline, SBAdminStackedInline,
)
from django_smartbase_admin.admin.site import sb_admin_site
from django_smartbase_admin.engine.actions import SBAdminCustomAction
from django_smartbase_admin.engine.const import (
    DETAIL_STRUCTURE_RIGHT_CLASS, FilterVersions,
)
from django_smartbase_admin.engine.fake_inline import (
    SBAdminFakeInlineMixin,
)
from django_smartbase_admin.engine.field import SBAdminField
from django_smartbase_admin.services.xlsx_export import SBAdminXLSXExportService
from django_smartbase_admin.utils import render_notifications

from .models import Product, Category, Manufacturer, ProductImage, Purchase, PurchaseItem, EditableListModel, QuickSearchModel, ReorderModel, ListActionModel
from .sb_admin_forms import ProductCategoryTreeInlineForm
from .sb_admin_widgets import CategoryTreeWidget, CategoryTreeFilterWidget


class ProductImageInline(SBAdminTableInline):
    model = ProductImage
    fields = ("image", "alt_text")
    extra = 1
    sb_admin_add_modal = True


def button_formatter(object_id, value):
    html = f'<a class="btn btn-small btn-icon"><span>Button</span></a>'
    return mark_safe(html)


def boolean_icon_formatter(object_id, value):
    return mark_safe("✅" if value else "❌")


def currency_formatter(object_id, value):
    return mark_safe(f'<span class="badge badge-simple badge-positive">{value:.2f} €</span>')


def dimensions_formatter(object_id, value):
    return mark_safe(f'<span class="badge badge-simple ">{value or "-"}</span>')


def manufacturer_formatter(object_id, value):
    return value or _("—")


def weight_formatter(object_id, value):
    return f"{value:.3f} kg" if value else "-"


class ProductSameManufacturerInline(SBAdminFakeInlineMixin, SBAdminTableInline):
    model = Product
    fields = ["name", "price", "is_active", "created", "is_current_product"]
    readonly_fields = fields
    can_delete = False
    verbose_name = "Product from the same manufacturer - Fake inline example"
    verbose_name_plural = "Products from the same manufacturer - Fake inline example"

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


class RelatedProductsOutgoingInline(SBAdminFakeInlineMixin, SBAdminTableInline):
    model = Product
    fields = ["name", "price", "is_active", "manufacturer"]
    readonly_fields = fields
    can_delete = False
    verbose_name_plural = _("Related products (linked from this product) - Fake inline of the field 'related_products'")

    def has_add_permission(self, request, obj=None):
        return False

    def filter_fake_inline_identifier_by_parent_instance(self, inline_queryset, parent_instance):
        return inline_queryset.filter(pk__in=parent_instance.related_products.all())


class RelatedProductsIncomingInline(SBAdminFakeInlineMixin, SBAdminTableInline):
    model = Product
    fields = ["name", "price", "is_active", "manufacturer"]
    readonly_fields = fields
    can_delete = False
    verbose_name_plural = _("Related products (linked to this product) - Second Fake inline of the field 'related_products'")

    def has_add_permission(self, request, obj=None):
        return False

    def filter_fake_inline_identifier_by_parent_instance(self, inline_queryset, parent_instance):
        return inline_queryset.filter(related_products=parent_instance)


class ProductCategoryTreeInline(SBAdminFakeInlineMixin, SBAdminTableInline):
    model = Product
    form = ProductCategoryTreeInlineForm
    title = _("Categories - Tree Widget example")

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def filter_fake_inline_identifier_by_parent_instance(
            self, inline_queryset, parent_instance
    ):
        return inline_queryset.filter(pk=parent_instance.id)


class RelatedProductsInline(SBAdminTableInline):
    model = Product.related_products.through
    fk_name = "from_product"
    extra = 1
    verbose_name = "Related product"
    verbose_name_plural = "Related products - Many To Many inline example"


@admin.register(Product, site=sb_admin_site)
class ProductSBAdmin(SBAdmin):
    model = Product
    inlines = [ProductImageInline, RelatedProductsInline]
    sbadmin_fake_inlines = [ProductSameManufacturerInline, ProductCategoryTreeInline, RelatedProductsOutgoingInline,
                            RelatedProductsIncomingInline, ]
    sbadmin_list_display = (
        "get_image",
        "name",
        "sku",
        SBAdminField(name="price", title=_("Price (€)"), python_formatter=currency_formatter),
        SBAdminField(name="is_active", title=_("Active"), python_formatter=boolean_icon_formatter),
        "is_featured",
        SBAdminField(
            name="manufacturer",
            title=_("Manufacturer"),
            annotate=F("manufacturer__name"),
            filter_field="manufacturer__name",
            python_formatter=manufacturer_formatter,
        ),
        SBAdminField(name="netto_weight", title=_("Weight (kg)"), python_formatter=weight_formatter),
        SBAdminField(name="package_dims", title=_("Package"), python_formatter=dimensions_formatter),
        SBAdminField(name="product_dims", title=_("Product"), python_formatter=dimensions_formatter),
        SBAdminField(name="created", title=_("Created")),
        SBAdminField(name="slug", title=_("Action"), python_formatter=button_formatter),
        SBAdminField(
            name="categories",
            title=_("Categories"),
            annotate=F("categories__name"),
            filter_widget=CategoryTreeFilterWidget(
                search_query_lambda=lambda request, qs, model, search_term, language_code: qs.filter(
                    name__icontains=search_term
                ),
                filter_query_lambda=lambda request, filter_value: Q(
                    is_active=True
                ),
            ),
        ),
    )

    sbadmin_tabs = {
        "General": [
            "Appearance",
            "Delivery",
            "Other settings",
            RelatedProductsInline,
            "Base settings",
        ],
        "Media": [
            ProductImageInline,
        ],
        "Tree Widget": [
            ProductCategoryTreeInline,
        ],
        "Fake inline": [
            ProductSameManufacturerInline,
            RelatedProductsOutgoingInline,
            RelatedProductsIncomingInline,
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
        ), (
            "Other settings",
            {
                "fields": [
                    ("stock_quantity", "barcode",),
                    "tags",
                ]
            },
        ),
        (
            "Base settings",
            {
                "classes": [DETAIL_STRUCTURE_RIGHT_CLASS],
                "fields": [
                    "is_active",
                    "is_featured",
                    "release_type",
                    "slug",
                    "sku",
                    "manufacturer",
                    "price",
                    "created",

                ],
            },
        ),
    ]
    readonly_fields = ['created']

    @admin.display(ordering="tags", description="Image")
    def get_image(self, object_id, value=None, **kwargs):
        product = Product.objects.prefetch_related("images").get(pk=object_id)
        first_image = product.images.first()
        image_url = first_image.image.url if first_image else ""
        return mark_safe(
            f'<div class="catalog-image w-40 h-40 border border-dark-200 rounded-xs overflow-hidden">'
            f'<img src="{image_url}" width="40" height="40" /></div>'
        )


@admin.register(Category, site=sb_admin_site)
class CategorySBAdmin(SBAdmin):
    model = Category
    sbadmin_list_display = ("name", SBAdminField(name="domain", title="Domain", annotate=F("domain__name")),)
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
                "fields": ["name", "slug", "image", "path", ]
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

        final_data = CategoryTreeWidget.get_tree_data(
            request,
            action.get_data_queryset(),
            values=action.get_data_queryset_values(),
        )
        return JsonResponse(data=final_data, safe=False)

    def get_extra_context(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context["tree_strings"] = CategoryTreeWidget.tree_strings
        extra_context["tree_json_url"] = self.get_action_url("tree_list_json")
        extra_context["fancytree_filter_settings"] = {"fuzzy": False}
        return extra_context

    def changelist_view(self, request, extra_context=None):
        extra_context = self.get_extra_context(request, extra_context)
        return super().changelist_view(request, extra_context)


@admin.register(Manufacturer, site=sb_admin_site)
class ManufacturerSBAdmin(SBAdmin):
    model = Manufacturer
    sbadmin_list_display = ["name"]
    search_fields = ["name"]
    fieldsets = [
        (
            None,
            {
                "fields": ["name", "logo"]
            },
        )
    ]


@admin.register(QuickSearchModel, site=sb_admin_site)
class QuickSearchModelSBAdmin(SBAdmin):
    model = QuickSearchModel
    sbadmin_list_display = ["name"]
    search_fields = ["name"]
    filters_version = FilterVersions.FILTERS_VERSION_2
    fieldsets = [
        (
            None,
            {
                "fields": ["name"]
            },
        )
    ]


@admin.register(EditableListModel, site=sb_admin_site)
class EditableListModelSBAdmin(SBAdmin):
    model = EditableListModel
    sbadmin_list_display = ["name", SBAdminField(
        name="value_1",
        tabulator_editor="input",
    ), SBAdminField(
        name="value_2",
        tabulator_editor="input",
    )]
    search_fields = ["name"]
    fieldsets = [
        (None, {"fields": ["name", "value_1", "value_2"]}),
    ]

    def get_tabulator_definition(self, request):
        tabulator_definition = super().get_tabulator_definition(request)
        tabulator_definition["modules"] = [
            "dataEditModule",
        ]
        return tabulator_definition

    def action_table_data_edit(self, request, modifier):
        current_row_id = json.loads(request.POST.get("currentRowId", ""))
        column_field_name = request.POST.get("columnFieldName", "")
        cell_value = request.POST.get("cellValue", "")
        field_map = self.get_field_map(request)
        field = field_map.get(column_field_name)
        if field:
            messages.add_message(request, messages.INFO, f"Row id: {current_row_id}, New value: {cell_value}")
            messages.add_message(request, messages.WARNING, f"Database works in read-only mode. Changes will not be persistent.")
            return HttpResponse(status=200, content=render_notifications(request))


class PurchaseItemInline(SBAdminTableInline):
    model = PurchaseItem
    fields = ("product", "price")
    extra = 1
    verbose_name = "Items - Table Inline Example"
    verbose_name_plural = "Items - Table Inline Example"


class PurchaseItemInlineStacked(SBAdminStackedInline):
    model = PurchaseItem
    fields = ("product", "price")
    verbose_name = "Items - Stacked Inline Example"
    verbose_name_plural = "Items - Stacked Inline Example"


@admin.register(Purchase, site=sb_admin_site)
class PurchaseSBAdmin(SBAdmin):
    model = Purchase
    filters_version = FilterVersions.FILTERS_VERSION_2
    inlines = [PurchaseItemInline, PurchaseItemInlineStacked]
    sbadmin_list_display = (
        "customer_name",
        SBAdminField(name="total_price", title=_("Price")),
        SBAdminField(name="created_at", title=_("Created At")),
        SBAdminField(name="domain", title="Domain", annotate=F("domain__name")),
    )

    list_filter = ["created_at"]

    ordering = ["-created_at"]
    sbadmin_tabs = {
        "General": [
            None,
            "Meta",
        ],
        "Table inline": [
            PurchaseItemInline,
        ],
        "Stacked inline": [
            PurchaseItemInlineStacked,
        ],
    }
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
            "Meta",
            {
                "classes": [DETAIL_STRUCTURE_RIGHT_CLASS],
                "fields": ["created_at"],
            },
        ),
    ]

    readonly_fields = ["created_at"]


@admin.register(ReorderModel, site=sb_admin_site)
class ReorderModelSBAdmin(SBAdmin):
    model = ReorderModel
    sbadmin_list_reorder_field = "order_by"
    ordering = ["order_by"]
    sbadmin_list_display = ["name"]
    search_fields = ["name"]
    fieldsets = [
        (
            None,
            {
                "fields": ["name"]
            },
        )]
@admin.register(ProductImage, site=sb_admin_site)
class ProductImageSBAdmin(SBAdmin):
    model = ProductImage
    sbadmin_list_display = ["image"]
    fieldsets = [
        (
            None,
            {
                "fields": ["product","image","alt_text"]
            },
        )]


@admin.register(ListActionModel, site=sb_admin_site)
class ListActionModelSBAdmin(SBAdmin):
    def export_action(self, request, modifier) -> HttpResponse:
        data = [{"Demo": "demo"}]

        columns = [{"field": k, "title": k} for k in data[0].keys()] if data else []

        return SBAdminXLSXExportService.create_workbook_http_respone(
            file_name="Demo_export.xlsx",
            data=data,
            columns=columns,
            options={"header_rows_count": 1},
        )

    model = ReorderModel
    sbadmin_list_display = ["name"]
    search_fields = ["name"]
    fieldsets = [
        (
            None,
            {
                "fields": ["name"]
            },
        )]

    def get_sbadmin_list_actions(self, request):
        return [
            SBAdminCustomAction(
                title=_("Single action"),
                view=self,
                action_id="export_action",
            ),
            SBAdminCustomAction(
                title=_("Single action with icon"),
                view=self,
                icon="Lightning",
                action_id="export_action",
            ),
            SBAdminCustomAction(
                title="Dropdown actions",
                icon="Excel-one",
                sub_actions=[
                    SBAdminCustomAction(
                        title=_("Action without icon"),
                        view=self,
                        action_id="export_action",
                    ),
                    SBAdminCustomAction(
                        title=_("Action with icon"),
                        icon="Calendar",
                        view=self,
                        action_id="export_action",
                    ),
                ],
            ),
            SBAdminCustomAction(
                title="Dropdown actions with icon",
                icon="Printer",
                sub_actions=[
                    SBAdminCustomAction(
                        title=_("Action without icon"),
                        view=self,
                        action_id="export_action",
                    ),
                    SBAdminCustomAction(
                        title=_("Action with icon"),
                        icon="Calendar",
                        view=self,
                        action_id="export_action",
                    ),
                ],
            ),
        ]
