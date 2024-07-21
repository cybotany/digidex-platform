from .base import *

DEBUG = True

ACCOUNT_URL = f"{ACCOUNT_URL}.dev"
ADMIN_URL = f"{ADMIN_URL}.dev"
API_URL = f"{API_URL}.dev"
APP_URL = f"{APP_URL}.dev"

ALLOWED_HOSTS = [
    ACCOUNT_URL,
    ADMIN_URL,
    API_URL,
    APP_URL
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
