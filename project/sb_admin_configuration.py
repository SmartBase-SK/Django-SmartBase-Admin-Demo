from django_smartbase_admin.engine.configuration import SBAdminConfigurationBase, SBAdminRoleConfiguration

from project.catalog.models import Purchase

from django import forms
from django.db.models import F, Sum, Count, When
from django.utils.translation import gettext_lazy as _

from django_smartbase_admin.admin.widgets import SBAdminRadioWidget
from django_smartbase_admin.engine import const
from django_smartbase_admin.engine.configuration import (
    SBAdminConfigurationBase,
    SBAdminRoleConfiguration,
)
from django_smartbase_admin.engine.dashboard import (
    SBAdminDashboardLineChartWidgetByDate,
    SBAdminDashboardListWidget,
    SBAdminChartAggregateSubWidget,
)
from django_smartbase_admin.engine.menu_item import SBAdminMenuItem
from django_smartbase_admin.views.dashboard_view import SBAdminDashboardView


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
            title=_("Total turnover"), aggregate=Sum("total_price"), python_formatter=format_total_price
        ),
        SBAdminChartAggregateSubWidget(
            title=_("Purchase count"), aggregate=Count("id"),
        ),
    ]



class SBAdminConfiguration(SBAdminConfigurationBase):
    def get_configuration_for_roles(self, user_roles):
        config = SBAdminRoleConfiguration(
            default_view=SBAdminMenuItem(view_id="dashboard"),
            menu_items=[
                SBAdminMenuItem(view_id="dashboard", icon="All-application"),
                SBAdminMenuItem(view_id="catalog_product", icon="List-checkbox", label="Catalog",
                                sub_items=[SBAdminMenuItem(view_id="catalog_category"),
                                           SBAdminMenuItem(view_id="catalog_manufacturer"),
                                           SBAdminMenuItem(view_id="catalog_product")
                                           ]
                                ),
                SBAdminMenuItem(view_id="catalog_purchase", icon="List-checkbox"),

            ],
            registered_views=[
                SBAdminDashboardView(
                    widgets=[
                        PurchaseChartWidget(settings=[]),
                        PurchaseDashboardListWidget(),
                    ],
                    title="Dashboard"
                ),
            ],
        )
        return config
