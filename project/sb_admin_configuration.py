from project.catalog.models import Purchase

from django.db.models import Sum, Count
from django.utils.translation import gettext_lazy as _
from django_smartbase_admin.engine.configuration import (
    SBAdminRoleConfiguration,
    SBAdminConfigurationBase,
)
from django_smartbase_admin.engine.const import FilterVersions
from django_smartbase_admin.engine.menu_item import SBAdminMenuItem
from django_smartbase_admin.views.dashboard_view import SBAdminDashboardView
from django_smartbase_admin.engine.dashboard import (
    SBAdminDashboardLineChartWidgetByDate,
    SBAdminDashboardListWidget,
    SBAdminChartAggregateSubWidget,
)

EDITOR_ROLE = "Editors"

class PurchaseDashboardListWidget(SBAdminDashboardListWidget):
    ordering = ["-created_at"]
    name = "Latest Purchases"
    model = Purchase
    list_display = ["created_at", "customer_name", "total_price"]
    list_per_page = 10


def format_total_price(sub_widget, request, value):
    return f"{value} €"


class PurchaseChartWidget(SBAdminDashboardLineChartWidgetByDate):
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
        icon="List-checkbox",
        sub_items=[
            SBAdminMenuItem(view_id="catalog_product"),
            SBAdminMenuItem(view_id="catalog_category"),
            SBAdminMenuItem(view_id="catalog_manufacturer"),
        ],
    ),
    SBAdminMenuItem(view_id="catalog_purchase", icon="Table-report"),
]

editor_menu_items = [
    SBAdminMenuItem(view_id="catalog_product", icon="List-checkbox"),
    SBAdminMenuItem(view_id="catalog_category", icon="Tag-one"),
    SBAdminMenuItem(view_id="catalog_manufacturer", icon="Box"),
]


class PurchaseBaseConfiguration(SBAdminRoleConfiguration):
    filters_version = FilterVersions.FILTERS_VERSION_2
    default_view = SBAdminMenuItem(view_id="dashboard")
    registered_views = [
        SBAdminDashboardView(
            widgets=[
                PurchaseChartWidget(settings=[]),
                PurchaseDashboardListWidget(),
            ],
            title="Dashboard",
        ),
    ]


class AdminPurchaseConfiguration(PurchaseBaseConfiguration):
    menu_items = admin_menu_items
    default_view = SBAdminMenuItem(view_id="dashboard")


class EditorPurchaseConfiguration(PurchaseBaseConfiguration):
    menu_items = editor_menu_items
    default_view = SBAdminMenuItem(view_id="catalog_product")


class SBAdminConfiguration(SBAdminConfigurationBase):
    def get_configuration_for_roles(self, user_roles):
        user_roles = list(user_roles)
        if EDITOR_ROLE in user_roles:
            return EditorPurchaseConfiguration()
        return AdminPurchaseConfiguration()
