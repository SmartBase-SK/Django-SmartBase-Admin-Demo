from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path
from django_smartbase_admin.admin.site import sb_admin_site

from project.catalog.views import home_redirect

urlpatterns = [
    path("", home_redirect, name="home_redirect"),
    path("admin/", admin.site.urls),
    path("sb-admin/", sb_admin_site.urls),
]

if settings.ENVIRONMENT == "dev":
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    ) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
