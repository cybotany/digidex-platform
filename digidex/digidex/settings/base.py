"""
Django settings for digidex project.
"""
import os
from datetime import timedelta
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')
ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOSTS", "").split(",")

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)

INSTALLED_APPS = [
    "accounts",
    "api",
    "base",
    "digitization",
    "home",
    "inventory",
    "nfc",
    "profiles",
    "search",
    "storages",

    "wagtail.contrib.settings",
    "wagtail.contrib.forms",
    "wagtail.contrib.redirects",
    "wagtail.embeds",
    "wagtail.sites",
    "wagtail.users",
    "wagtail.snippets",
    "wagtail.documents",
    "wagtail.images",
    "wagtail.search",
    "wagtail.admin",
    "wagtail",
    "modelcluster",
    "taggit",

    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "rest_framework",
    "allauth",
    "allauth.account",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "wagtail.contrib.redirects.middleware.RedirectMiddleware",
    "allauth.account.middleware.AccountMiddleware",
]

ROOT_URLCONF = "digidex.urls"

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

USE_I18N = True

USE_TZ = True

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
AWS_S3_FILE_OVERWRITE = False
MEDIA_URL = '{}/media/'.format(AWS_S3_CUSTOM_DOMAIN)

# Static files (CSS, JavaScript, Images)
STATIC_URL = '{}/static/'.format(AWS_S3_CUSTOM_DOMAIN)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

STORAGES = {
    "default": {
        "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.ManifestStaticFilesStorage",
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
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUTH_HEADER_TYPES': ('Bearer',),
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',
}

# ALLAUTH settings
AUTH_USER_MODEL = 'accounts.User'

ACCOUNT_AUTHENTICATION_METHOD = 'email'

SIGNUP_URL = 'account_signup'

LOGIN_URL = 'account_login'

LOGIN_REDIRECT_URL = 'wagtailadmin_home'

ACCOUNT_ADAPTER = 'accounts.adapters.DigidexAccountAdapter'

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
    'accounts', 'company', 'nfc', 'inventory'
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

ACCOUNT_EMAIL_SUBJECT_PREFIX = "[Digidex] "

# Wagtail settings
WAGTAIL_SITE_NAME = "DigiDex"

WAGTAILIMAGES_EXTENSIONS = ['gif', 'jpg', 'jpeg', 'png', 'webp', 'svg']

WAGTAIL_FRONTEND_LOGIN_URL = LOGIN_URL

WAGTAILSEARCH_BACKENDS = {
    "default": {
        "BACKEND": "wagtail.search.backends.database",
    }
}

LOG_DIR = os.path.join(BASE_DIR, 'logs')
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'file': {
            'level': 'WARNING',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/digidex.log'),
            'formatter': 'verbose',
        },
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
            'filters': ['require_debug_true'],
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'formatter': 'verbose',
        }
    },
    'loggers': {
        'django': {
            'handlers': ['file', 'console', 'mail_admins'],
            'level': 'INFO',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['file', 'mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
    },
}
