from sbcore.settings import *

INSTALLED_APPS = (
    [
        "project",
        "catalog.apps.CatalogConfig",
    ]
    + COMMON_INSTALLED_APPS
)
SB_ADMIN_CONFIGURATION = "project.sb_admin_configuration.SBAdminConfiguration"

ROOT_URLCONF = "project.urls"
