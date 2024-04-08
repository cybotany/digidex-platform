import os
import random
import string
import dj_database_url

from .base import *

SECRET_KEY = os.environ["SECRET_KEY"]

DEBUG = False

DATABASES = {
    "default": dj_database_url.config(
        conn_max_age=600,
        conn_health_checks=True
    )
}

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

EMAIL_HOST = os.environ["EMAIL_HOST"]
EMAIL_HOST_USER = os.environ["EMAIL_HOST_USER"]
EMAIL_HOST_PASSWORD = os.environ["EMAIL_HOST_PASSWORD"]
EMAIL_PORT = os.environ["EMAIL_PORT"]
EMAIL_USE_TLS = os.environ["EMAIL_USE_TLS"]

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

SECURE_SSL_REDIRECT = True

ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOSTS", "").split(",")

CSRF_TRUSTED_ORIGINS = os.getenv("DJANGO_CSRF_TRUSTED_ORIGINS", "").split(",")

STORAGES["staticfiles"]["BACKEND"] = "whitenoise.storage.CompressedManifestStaticFilesStorage"

if "SPACES_BUCKET_NAME" in os.environ:
    INSTALLED_APPS.append("storages")

    AWS_STORAGE_BUCKET_NAME = os.getenv("SPACES_BUCKET_NAME")
    AWS_S3_REGION_NAME = os.getenv("AWS_S3_REGION_NAME")
    AWS_S3_ENDPOINT_URL = os.getenv("SPACES_ENDPOINT_URL")
    AWS_S3_CUSTOM_DOMAIN = os.environ.get('SPACES_CUSTOM_DOMAIN')
    AWS_S3_ACCESS_KEY_ID = os.getenv("SPACES_ACCESS_KEY")
    AWS_S3_SECRET_ACCESS_KEY = os.getenv("SPACES_SECRET_KEY")

    STORAGES["default"]["BACKEND"] = "storages.backends.s3boto3.S3Boto3Storage"

    AWS_S3_OBJECT_PARAMETERS = {
        'CacheControl': 'max-age=86400',
    }

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["console"],
            "level": os.getenv("DJANGO_LOG_LEVEL", "INFO"),
        },
    },
}

AWS_LOCATION = 'static'

STATIC_URL = '{}/{}/'.format(AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
STATIC_ROOT = 'static/'
MEDIA_ROOT = 'media/'

WAGTAILADMIN_BASE_URL = "https://digidex.app"
WAGTAIL_SITE_NAME = "DigiDex"
WAGTAIL_REDIRECTS_FILE_STORAGE = "cache"
