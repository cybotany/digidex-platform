from .base import *

DEBUG = True

INSTALLED_APPS.append("whitenoise.runserver_nostatic")

HOST_SCHEME = 'http'

HOSTNAME = "localhost"

ALLOWED_HOSTS = [
    HOSTNAME,
    f'www.{HOSTNAME}',
]

WAGTAILADMIN_BASE_URL = f"{HOST_SCHEME}://{HOSTNAME}"

STORAGES = {
    'default': {
        'BACKEND': 'django.core.files.storage.FileSystemStorage'
    },
    'staticfiles': {
        'BACKEND': 'whitenoise.storage.CompressedManifestStaticFilesStorage'
    }
}

MIDDLEWARE.append("whitenoise.middleware.WhiteNoiseMiddleware")

MEDIA_URL = '/media/'

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

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
