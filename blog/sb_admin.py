from django.contrib import admin
from django_smartbase_admin.admin.site import sb_admin_site
from .models import Post, Author, Category
from django_smartbase_admin.admin.admin_base import SBAdmin, SBAdminTableInline

class CategoryInline(SBAdminTableInline):
    model = Post.categories.through
    verbose_name = "Post"

class PostInline(SBAdminTableInline):
    model = Post
    verbose_name = "Post"

class AuthorInline(SBAdminTableInline):
    model = Author
    verbose_name = "Author"

@admin.register(Post, site=sb_admin_site)
class PostSBAdmin(SBAdmin):
    list_per_page = 25  # Sets the number of items to display per page
    sbadmin_list_display = ("title", "published_date", "author")
    sbadmin_fieldsets = [
        (None, {
            "fields": ["title", "content", "author", "categories"]
        })
    ]
    inlines = [CategoryInline]
    sbadmin_tabs = {
        "Post": [None, CategoryInline],
    }

@admin.register(Author, site=sb_admin_site)
class AuthorSBAdmin(SBAdmin):
    sbadmin_list_display = ("name",)
    sbadmin_fieldsets = [
        (None, {
            "fields": ["name", "bio"]
        })
    ]
    inlines = [PostInline]
    sbadmin_tabs = {
        "Author": [None, PostInline],
        "Bio": ["bio", None],
    }

@admin.register(Category, site=sb_admin_site)
class CategorySBAdmin(SBAdmin):
    sbadmin_list_display = ("name",)
    sbadmin_fieldsets = [
        (None, {
            "fields": ["name"]
        })
    ]
    inlines = [CategoryInline]


