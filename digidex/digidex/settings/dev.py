from .base import *

DEBUG = True

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

WAGTAILADMIN_BASE_URL = "http://127.0.0.1:8000"

SECURE_PROXY_SSL_HEADER = None

SESSION_COOKIE_SECURE = False

CSRF_COOKIE_SECURE = False

SECURE_SSL_REDIRECT = False

try:
    from .local import *  # noqa
except ImportError:
    pass
