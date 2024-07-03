from django.db.models import F, Count
from django_smartbase_admin.engine.configuration import SBAdminConfigurationBase, SBAdminRoleConfiguration
from django_smartbase_admin.engine.dashboard import SBAdminDashboardListWidget, SBAdminDashboardChartWidget
from django_smartbase_admin.engine.menu_item import SBAdminMenuItem
from django_smartbase_admin.views.dashboard_view import SBAdminDashboardView
from blog.models import Post, Author

class AuthorPostsChartWidget(SBAdminDashboardListWidget):
    name = "Author Posts"
    model = Post
    date_annotate_field = "published_date"
    sub_widgets = []

config = SBAdminRoleConfiguration(
    default_view=SBAdminMenuItem(view_id="dashboard"),
    menu_items=[
        SBAdminMenuItem(view_id="dashboard", icon="All-application"),
        SBAdminMenuItem(view_id="blog_post",
                        sub_items=[],
                        icon="Search"),
        SBAdminMenuItem(view_id="blog_author", icon="People-top-card"),
        SBAdminMenuItem(view_id="blog_category", icon="Star", label="Categories")
        ],
    registered_views=[
        SBAdminDashboardView(
            widgets=[
                SBAdminDashboardListWidget(
                    name="Posts",
                    model=Post,
                    list_display=["title", "published_date"],
                    list_per_page=10
                ),
                SBAdminDashboardChartWidget(
                    name="Author posts",
                    model=Author,
                    x_axis_annotate=F("name"),
                    y_axis_annotate=Count("post__id"),

                )
            ],
            title="Dashboard",
        ),
    ],
)


class SBAdminConfiguration(SBAdminConfigurationBase):
    def get_configuration_for_roles(self, user_roles):
        return config
