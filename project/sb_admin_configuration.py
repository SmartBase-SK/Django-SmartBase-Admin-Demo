from django import forms
from django.db.models import Sum, Count
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.translation import gettext_lazy as _
from django_smartbase_admin.admin.admin_base import SBAdminBaseFormInit
from django_smartbase_admin.admin.widgets import SBAdminRadioDropdownWidget
from django_smartbase_admin.engine.configuration import (
    SBAdminRoleConfiguration,
    SBAdminConfigurationBase,
)
from django_smartbase_admin.engine.const import GLOBAL_FILTER_DATA_KEY
from django_smartbase_admin.engine.dashboard import (
    SBAdminDashboardLineChartWidgetByDate,
    SBAdminDashboardListWidget,
    SBAdminChartAggregateSubWidget,
)
from django_smartbase_admin.engine.field import SBAdminField
from django_smartbase_admin.engine.menu_item import SBAdminMenuItem
from django_smartbase_admin.views.dashboard_view import SBAdminDashboardView

from project.catalog.models import Purchase, Domain, BaseDomainModel

EDITOR_ROLE = "Editors"


class GlobalFilterForm(SBAdminBaseFormInit, forms.Form):
    include_all_values_for_empty_fields = ["domain"]
    domain = forms.ModelChoiceField(
        queryset=Domain.objects.all(),
        required=False,
        blank=True,
        widget=SBAdminRadioDropdownWidget(attrs={"id": "DOMAIN_FILTER"}),
        label=_("Choose domain"),
        empty_label="All domains",
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["domain"].label_from_instance = self.label

    @staticmethod
    def label(obj):
        return obj.name


class PurchaseDashboardListWidget(SBAdminDashboardListWidget):
    ordering = ["-created_at"]
    name = _("Latest Purchases")
    model = Purchase
    list_per_page = 10

    list_display = [
        "created_at",
        SBAdminField(name="customer_name", title=_("Customer")),
        SBAdminField(name="total_price", title=_("Total Price")),
    ]


def format_total_price(sub_widget, request, value):
    return f"{value} €"


class PurchaseChartWidget(SBAdminDashboardLineChartWidgetByDate):
    def get_default_shortcut_index(self):
        return 2

    name = _("Turnover")
    model = Purchase
    date_annotate_field = "created_at"
    date_resolutions = SBAdminDashboardLineChartWidgetByDate.DateResolutionsOptions
    sub_widgets = [
        SBAdminChartAggregateSubWidget(
            title=_("Total turnover"),
            aggregate=Sum("total_price"),
            python_formatter=format_total_price,
        ),
        SBAdminChartAggregateSubWidget(
            title=_("Purchase count"),
            aggregate=Count("id"),
        ),
    ]


admin_menu_items = [
    SBAdminMenuItem(view_id="dashboard", icon="All-application"),
    SBAdminMenuItem(
        label="Catalog",
        icon="Box",
        sub_items=[
            SBAdminMenuItem(view_id="catalog_product", label="Products"),
            SBAdminMenuItem(view_id="catalog_category", label="Categories"),
            SBAdminMenuItem(view_id="catalog_manufacturer", label="Manufacturers"),
        ],
    ),

    SBAdminMenuItem(view_id="catalog_product", label="List View", icon="List-checkbox"),
    SBAdminMenuItem(view_id="catalog_editablelistmodel", label="Editable List View", icon="Edit"),
    SBAdminMenuItem(view_id="catalog_reordermodel", url='/sb-admin/catalog_reordermodel/action_enter_reorder/template', label="Reorder List View", icon="Sort-amount-down"),
    SBAdminMenuItem(view_id="catalog_purchase", label="Advanced filters", icon="Filter"),
    SBAdminMenuItem(view_id="catalog_listactionmodel", label="List actions", icon="Lightning"),
    SBAdminMenuItem(view_id="catalog_category", label="Tree Widget", icon="Sort-amount-down"),
    SBAdminMenuItem(view_id="catalog_quicksearchmodel", label="Quick search", icon="Find"),
    SBAdminMenuItem(url=f'{reverse("redirect_to_last_product_tab")}?{urlencode({"tab": ""})}', label="Tabs", icon="Minus-the-top"),
    SBAdminMenuItem(url=f'{reverse("redirect_to_last_product_tab")}?{urlencode({"tab": "tree-widget"})}', label="Tree Widget Field", icon="Triangle-round-rectangle"),
    SBAdminMenuItem(url=f'{reverse("redirect_to_last_purchase")}?{urlencode({"tab": "table-inline"})}', label="Table Inline", icon="Id-card-h"),
    SBAdminMenuItem(url=f'{reverse("redirect_to_last_purchase")}?{urlencode({"tab": "stacked-inline"})}', label="Stacked Inline", icon="Table-report"),
    SBAdminMenuItem(url=f'{reverse("redirect_to_last_product_tab")}?{urlencode({"tab": "fake-inline"})}', label="Fake inline", icon="Magic"),

]

editor_menu_items = [
    SBAdminMenuItem(view_id="catalog_product", icon="List-checkbox", label="List View"),
    SBAdminMenuItem(view_id="catalog_category", icon="List-checkbox", label="Tree View"),
    SBAdminMenuItem(view_id="catalog_manufacturer", icon="Box"),
]


class BaseConfiguration(SBAdminRoleConfiguration):
    global_filter_form = GlobalFilterForm
    default_view = SBAdminMenuItem(view_id="dashboard")
    registered_views = [
        SBAdminDashboardView(
            widgets=[
                PurchaseChartWidget(settings=[]),
                PurchaseDashboardListWidget()
            ],
            title="Dashboard",
        ),
    ]

    def restrict_queryset(
            self,
            qs,
            model,
            request,
            request_data,
            global_filter=True,
            global_filter_data_map=None,
    ):
        qs = super().restrict_queryset(
            qs, model, request, request_data, global_filter, global_filter_data_map
        )
        global_filter_map = request.session.get(GLOBAL_FILTER_DATA_KEY)

        if global_filter_map:
            domain = global_filter_map.get("domain")
            if issubclass(model, BaseDomainModel) and domain:
                qs = qs.filter(domain_id=domain)
        return qs


class AdminConfiguration(BaseConfiguration):
    default_view = SBAdminMenuItem(view_id="dashboard")
    menu_items = admin_menu_items


class EditorConfiguration(BaseConfiguration):
    menu_items = editor_menu_items
    default_view = SBAdminMenuItem(view_id="catalog_product")


class SBAdminConfiguration(SBAdminConfigurationBase):
    def get_configuration_for_roles(self, user_roles):
        user_roles = list(user_roles)
        if EDITOR_ROLE in user_roles:
            return EditorConfiguration()
        return AdminConfiguration()
