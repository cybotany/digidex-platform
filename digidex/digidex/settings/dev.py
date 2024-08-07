from .base import *

DEBUG = True

HOST_SCHEME = 'http'

HOSTNAME = "localhost"

ALLOWED_HOSTS = [
    HOSTNAME,
    f'www.{HOSTNAME}',
]

WAGTAILADMIN_BASE_URL = f"{HOST_SCHEME}://{HOSTNAME}"

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
        'inventorytags': {
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
