from django import forms
from django.utils.translation import gettext_lazy as _
from django_smartbase_admin.admin.admin_base import (
    SBAdminBaseForm,
)

from .models import Product, Category
from .sb_admin_widgets import CategoryTreeWidget


class ProductCategoryTreeInlineForm(SBAdminBaseForm):
    category = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        required=False,
        label=_("Category"),
        to_field_name="path",
        widget=CategoryTreeWidget(inline=True, multiselect=True, value_field="path"),
    )

    class Meta:
        model = Product
        fields = ["category"]
