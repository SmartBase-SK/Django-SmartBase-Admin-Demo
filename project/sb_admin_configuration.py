from django import forms
from django_smartbase_admin.admin.widgets import SBAdminRadioWidget
from django_smartbase_admin.engine.field import SBAdminField

from project.catalog.models import Purchase, Domain, BaseDomainModel

from django.db.models import Sum, Count, F
from django.utils.translation import gettext_lazy as _
from django_smartbase_admin.engine.configuration import (
    SBAdminRoleConfiguration,
    SBAdminConfigurationBase,
)
from django_smartbase_admin.engine.const import FilterVersions, GLOBAL_FILTER_DATA_KEY
from django_smartbase_admin.engine.menu_item import SBAdminMenuItem
from django_smartbase_admin.views.dashboard_view import SBAdminDashboardView
from django_smartbase_admin.engine.dashboard import (
    SBAdminDashboardLineChartWidgetByDate,
    SBAdminDashboardListWidget,
    SBAdminChartAggregateSubWidget,
)

EDITOR_ROLE = "Editors"


class GlobalFilterForm(forms.Form):
    include_all_values_for_empty_fields = ["domain"]
    domain = forms.ModelChoiceField(
        queryset=Domain.objects.all(),
        required=False,
        blank=True,
        widget=SBAdminRadioWidget(attrs={"id": "DOMAIN_FILTER"}),
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
    name = "Latest Purchases"
    model = Purchase
    list_display = ["created_at", "customer_name", "total_price", SBAdminField(name="domain", title="Domain", annotate=F("domain__name"))]
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


class BaseConfiguration(SBAdminRoleConfiguration):
    global_filter_form = GlobalFilterForm
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
    menu_items = admin_menu_items
    default_view = SBAdminMenuItem(view_id="dashboard")


class EditorConfiguration(BaseConfiguration):
    menu_items = editor_menu_items
    default_view = SBAdminMenuItem(view_id="catalog_product")


class SBAdminConfiguration(SBAdminConfigurationBase):
    def get_configuration_for_roles(self, user_roles):
        user_roles = list(user_roles)
        if EDITOR_ROLE in user_roles:
            return EditorConfiguration()
        return AdminConfiguration()
