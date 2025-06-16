from sbcore.settings import *

INSTALLED_APPS = (
        [
            "project",
            "project.catalog.apps.CatalogConfig",
            "ckeditor_uploader"
        ]
        + COMMON_INSTALLED_APPS
)
SB_ADMIN_CONFIGURATION = "project.sb_admin_configuration.SBAdminConfiguration"

ROOT_URLCONF = "project.urls"
MIDDLEWARE = MIDDLEWARE + [
    'project.middleware.read_only_middleware.ReadOnlyModeMiddleware',
]
if CONTAINER_TYPE != 'celery' and ENVIRONMENT != 'dev':
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": os.environ.get("POSTGRES_DB"),
            "USER": os.environ.get("READ_ONLY_POSTGRES_USER"),
            "PASSWORD": os.environ.get("READ_ONLY_POSTGRES_PASSWORD"),
            "HOST": "pgbouncer-redonly",
            "PORT": os.environ.get("POSTGRES_PORT"),
            "CONN_MAX_AGE": None,
            "DISABLE_SERVER_SIDE_CURSORS": True,
            "TEST": {
                "NAME": os.environ.get("POSTGRES_DB"),
            },
        }
    }

CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_BASEPATH = STATIC_URL+"ckeditor/ckeditor/"
