from django_smartbase_admin.admin.widgets import SBAdminTreeWidget

from .models import Category


class CategoryTreeWidget(SBAdminTreeWidget):
    order_by = ["path"]
    model = Category

    @classmethod
    def get_tree_base_values(cls):
        return ["id", cls.path_field, "name"]

    @classmethod
    def get_tree_title(cls, request, item):
        return item.get("name")
