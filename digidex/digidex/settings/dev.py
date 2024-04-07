from .base import *

DEBUG = True

SECRET_KEY = "django-insecure-@u8i(hsjlxkjbn)x97pn#lypz#)^0&%viyw4f$^e#vgn2pen+@"

ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

STATICFILES_DIRS = [
    os.path.join(PROJECT_DIR, "static"),
]

STATIC_ROOT = os.path.join(BASE_DIR, "static")

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
