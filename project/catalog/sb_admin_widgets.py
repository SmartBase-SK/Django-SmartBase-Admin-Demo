from django_smartbase_admin.admin.widgets import SBAdminTreeWidget
from django_smartbase_admin.engine.dashboard import SBAdminDashboardListWidget
from django_smartbase_admin.engine.filter_widgets import SBAdminTreeFilterWidget, AutocompleteFilterWidget
from django.db.models import (
    F,
    Q,
)
from .models import Category


class CategoryTreeWidget(SBAdminTreeWidget):
    order_by = ["path"]
    model = Category

    @classmethod
    def get_tree_base_values(cls):
        return ["id", "path", "name"]

    @classmethod
    def get_tree_title(cls, request, item):
        return item.get("name")

    @classmethod
    def get_label(cls, request, item):
        return item.name


class CategoryTreeFilterWidget(CategoryTreeWidget, SBAdminTreeFilterWidget):
    template_name = "sb_admin/filter_widgets/tree_select_filter.html"
