import os

from .base import *

DEBUG = False

WAGTAIL_REDIRECTS_FILE_STORAGE = "cache"

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

if "EMAIL_HOST" in os.environ:
    EMAIL_HOST = os.getenv("EMAIL_HOST")
    EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
    EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
    EMAIL_PORT = os.getenv("EMAIL_PORT")
    EMAIL_USE_TLS = os.getenv("EMAIL_USE_TLS")

CSRF_TRUSTED_ORIGINS = os.getenv("DJANGO_CSRF_TRUSTED_ORIGINS", "").split(",")

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

SECURE_SSL_REDIRECT = True

if "SPACES_BUCKET_NAME" in os.environ:
    INSTALLED_APPS.append("storages")
    STORAGES["default"]["BACKEND"] = "storages.backends.s3boto3.S3Boto3Storage"

    AWS_STORAGE_BUCKET_NAME = os.getenv("SPACES_BUCKET_NAME")
    AWS_S3_REGION_NAME = os.getenv("AWS_S3_REGION_NAME")
    
    AWS_S3_ENDPOINT_URL = os.getenv("SPACES_ENDPOINT_URL")
    AWS_S3_CUSTOM_DOMAIN = os.getenv('SPACES_CUSTOM_DOMAIN')
    
    AWS_S3_ACCESS_KEY_ID = os.getenv("SPACES_ACCESS_KEY")
    AWS_S3_SECRET_ACCESS_KEY = os.getenv("SPACES_SECRET_KEY")

    AWS_S3_OBJECT_PARAMETERS = {
        'CacheControl': 'max-age=86400',
    }

    STATIC_URL = '{}/static/'.format(AWS_S3_CUSTOM_DOMAIN)
    MEDIA_URL = '{}/media/'.format(AWS_S3_CUSTOM_DOMAIN)

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

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
