"""
Django settings for digidex project.
"""
import os
from datetime import timedelta

from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

BASE_DIR = os.path.dirname(PROJECT_DIR)

ROOT_HOSTCONF = 'digidex.hosts'

DEFAULT_HOST = 'default'

PARENT_HOST = os.getenv('PARENT_HOST')

ROOT_URLCONF = "digidex.urls"

API_URL = f"api.{PARENT_HOST}"
ADMIN_URL = f"admin.{PARENT_HOST}"
CMS_URL = f"cms.{PARENT_HOST}"
WWW_URL = f"www.{PARENT_HOST}"

ALLOWED_HOSTS = [
    PARENT_HOST,

    API_URL,
    ADMIN_URL,
    CMS_URL,
    WWW_URL,
]

INSTALLED_APPS = [
    "django_hosts",
    "laces",
    "treebeard",
    "modelcluster",
    "taggit",

    "base",
    "home",
    "blog",
    "contact",
    "company",
    "accounts",
    "inventory",
    "search",
    "api",
    "storages",
    "whitenoise.runserver_nostatic",

    "wagtail.contrib.settings",
    "wagtail.contrib.forms",
    "wagtail.contrib.redirects",
    "wagtail.contrib.routable_page",
    "wagtail.embeds",
    "wagtail.sites",
    "wagtail.users",
    "wagtail.snippets",
    "wagtail.documents",
    "wagtail.images",
    "wagtail.search",
    "wagtail.admin",
    "wagtail",
    'wagtail.api.v2',

    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "rest_framework",
    "rest_framework_simplejwt",
    "allauth",
    "allauth.account",
]

MIDDLEWARE = [
    "django_hosts.middleware.HostsRequestMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "wagtail.contrib.redirects.middleware.RedirectMiddleware",
    "allauth.account.middleware.AccountMiddleware",
    "django_hosts.middleware.HostsResponseMiddleware",
]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(PROJECT_DIR, "templates"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "wagtail.contrib.settings.context_processors.settings",
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

WSGI_APPLICATION = "digidex.wsgi.application"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME', 'defaultdb'),
        'USER': os.getenv('DB_USERNAME'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
        'TEST': {
            'NAME': os.getenv('TEST_DB_NAME', 'test_defaultdb'),
            'SERIALIZE': False,
        },
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Internationalization
LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_L10N = True

USE_I18N = True

USE_TZ = True

WAGTAIL_I18N_ENABLED = True

# Default storage settings
AWS_STORAGE_BUCKET_NAME = os.getenv("SPACES_BUCKET_NAME")
AWS_S3_REGION_NAME = os.getenv("AWS_S3_REGION_NAME")
AWS_S3_ENDPOINT_URL = os.getenv("SPACES_ENDPOINT_URL")
AWS_S3_CUSTOM_DOMAIN = os.getenv('SPACES_CUSTOM_DOMAIN')
AWS_S3_ACCESS_KEY_ID = os.getenv("SPACES_ACCESS_KEY")
AWS_S3_SECRET_ACCESS_KEY = os.getenv("SPACES_SECRET_KEY")
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
AWS_DEFAULT_ACL = 'public-read'
AWS_S3_FILE_OVERWRITE = False

MEDIA_URL = '{}/media/'.format(AWS_S3_CUSTOM_DOMAIN)
STATIC_URL = '{}/static/'.format(AWS_S3_CUSTOM_DOMAIN)

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

STORAGES = {
    "default": {
        "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

# JWT settings
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUTH_HEADER_TYPES': ('Bearer',),
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',
}

# allauth settings
AUTH_USER_MODEL = 'accounts.DigiDexUser'

ACCOUNT_AUTHENTICATION_METHOD = 'username'

ACCOUNT_ADAPTER = 'accounts.adapter.DigidexAccountAdapter'

ACCOUNT_PRESERVE_USERNAME_CASING = False

ACCOUNT_USERNAME_MIN_LENGTH = 3

ACCOUNT_USERNAME_BLACKLIST = [
    'admin', 'administrator', 'root', 'sysadmin', 'webmaster', 'django-admin',
    'support', 'helpdesk', 'moderator', 'superuser', 'guest',
    'anonymous', 'nobody', 'user', 'null', 'undefined', 'localhost',
    'default', 'public', 'system', 'official', 'security', 'info',
    'contact', 'feedback', 'no-reply', 'noreply', 'api', 'static',
    'assets', 'img', 'css', 'js', 'javascript', 'fonts', 'media',
    'login', 'logout', 'signup', 'register', 'account', 'profile',
    'subscribe', 'unsubscribe', 'activate', 'deactivate', 'configuration',
    'settings', 'preferences', 'billing', 'payment', 'dashboard',
    'auth', 'authentication', 'token', 'oauth', 'sitemap', 'robots.txt',
    'postmaster', 'hostmaster', 'usenet', 'news', 'web', 'www', 'ftp',
    'mail', 'email', 'smtp', 'pop3', 'imap', 'cdn', 'network', 'messages',
    'notification', 'alerts', 'blog', 'forum', 'wiki', 'help', 'search',
    'dev', 'developer', 'cors', 'about', 'privacy', 'legal', 'terms',
    'services', 'document', 'documents', 'download', 'downloads', 'error', 'errors', '403', '404', '500',
    'base', 'company', 'inventory'
    'new', 'all', 'any', 'every', 'site', 'api-key', 'reset', 'change',
    'start', 'stop', 'edit', 'delete', 'remove', 'read', 'write', 'list',
    'create', 'update', 'confirm', 'save', 'load', 'logout', 'signin', 'signout',
    'test', 'testing', 'demo', 'example', 'batch', 'status',
    'django-admin',
]

ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 3

ACCOUNT_EMAIL_NOTIFICATIONS = True

ACCOUNT_EMAIL_REQUIRED = True

ACCOUNT_EMAIL_VERIFICATION = 'mandatory'

ACCOUNT_EMAIL_SUBJECT_PREFIX = "[DigiDex] "

LOGIN_URL = '/accounts/login/'

SIGNUP_URL = '/accounts/signup/'

LOGOUT_URL = '/accounts/logout/'

if "EMAIL_HOST" in os.environ:
    EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
    EMAIL_HOST = os.getenv("EMAIL_HOST")
    EMAIL_PORT = os.getenv("EMAIL_PORT")
    EMAIL_USE_TLS = os.getenv("EMAIL_USE_TLS")
    EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
    EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
    DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
else:
    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# Wagtail settings
WAGTAIL_SITE_NAME = "DigiDex"

WAGTAILIMAGES_IMAGE_MODEL = 'base.BaseImage'

WAGTAILIMAGES_EXTENSIONS = ['gif', 'jpg', 'jpeg', 'png', 'webp', 'svg']

WAGTAILSEARCH_BACKENDS = {
    "default": {
        "BACKEND": "wagtail.search.backends.database",
    }
}
