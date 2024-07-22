from .base import *

DEBUG = True

BASE_URL = '127.0.0.1'

API_URL = f"api.{BASE_URL}"
ACCOUNT_URL = f"account.{BASE_URL}"
ADMIN_URL = f"admin.{BASE_URL}"
CMS_URL = f"cms.{BASE_URL}"
LINK_URL = f"link.{BASE_URL}"
WWW_URL = f"www.{BASE_URL}"

ALLOWED_HOSTS = [
    BASE_URL,
    ACCOUNT_URL,
    API_URL,
    ADMIN_URL,
    CMS_URL,
    LINK_URL,
    WWW_URL,
]

WAGTAILADMIN_BASE_URL = f"http://{ADMIN_URL}"

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

SECURE_PROXY_SSL_HEADER = None

SESSION_COOKIE_SECURE = False

CSRF_COOKIE_SECURE = False

SECURE_SSL_REDIRECT = False

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'inventory': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
    },
}

try:
    from .local import *  # noqa
except ImportError:
    pass
