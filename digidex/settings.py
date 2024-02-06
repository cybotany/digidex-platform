"""
Django settings for digidex project.
"""
import os
from pathlib import Path
from datetime import timedelta

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Fetch the environment variable indicating the environment.
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', '')
DJANGO_ENV = os.environ.get('DJANGO_ENV', 'production')

GOOGLE_CLOUD_PROJECT_ID = os.environ.get('GOOGLE_CLOUD_PROJECT_ID', '')
RECAPTCHA_SITE_KEY = os.environ.get('RECAPTCHA_SITE_KEY', '')
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = os.environ.get('SERVICE_ACCOUNT_KEY', '')
RECAPTCHA_REQUIRED_SCORE = os.environ.get('RECAPTCHA_REQUIRED_SCORE', '')

# Environment specific settings
if DJANGO_ENV == 'production':
    DEBUG = False
    ALLOWED_HOSTS = ["digidex.app", "www.digidex.app"]

    AWS_LOCATION = 'static'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID', '')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY', '')
    AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME', '')
    AWS_S3_ENDPOINT_URL = os.environ.get('SPACES_ENDPOINT_URL', '')
    AWS_S3_CUSTOM_DOMAIN = os.environ.get('SPACES_EDGE_ENDPOINT_URL', '')
    AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}

    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_SSL_REDIRECT = True

    SECURE_HSTS_SECONDS = 31536000
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True

    STATIC_URL = '{}/{}/'.format(AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
    MEDIA_URL = f'https://{AWS_S3_ENDPOINT_URL}/'

    DEFAULT_FILE_STORAGE = 'digidex.utils.custom_storage.PublicMediaStorage'
    STATICFILES_STORAGE = 'digidex.utils.custom_storage.PublicStaticStorage'   
    STATICFILES_DIRS = [
        BASE_DIR / "static",
    ]

    CORS_ALLOWED_ORIGINS = [
        "https://digidex.app",
        "https://www.digidex.app",
        "https://cdn.digidex.app",
    ]
    CORS_ALLOW_CREDENTIALS = True
    CORS_ALLOW_HEADERS = [
        'access-control-allow-origin',
        "content-type",
        "authorization",
        'x-requested-with'
    ]
    CORS_ALLOW_METHODS = [
        "GET",
        "POST",
    ]

elif DJANGO_ENV == 'staging':
    DEBUG = True
    ALLOWED_HOSTS = ["staging.digidex.app", "www.staging.digidex.app"]

    AWS_LOCATION = 'static'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID', '')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY', '')
    AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME', '')
    AWS_S3_ENDPOINT_URL = os.environ.get('SPACES_ENDPOINT_URL', '')
    AWS_S3_CUSTOM_DOMAIN = os.environ.get('SPACES_EDGE_ENDPOINT_URL', '')
    AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}
    
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_SSL_REDIRECT = True

    SECURE_HSTS_SECONDS = 31536000
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True

    STATIC_URL = '{}/{}/'.format(AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
    MEDIA_URL = f'https://{AWS_S3_ENDPOINT_URL}/'

    DEFAULT_FILE_STORAGE = 'digidex.utils.custom_storage.PublicMediaStorage'
    STATICFILES_STORAGE = 'digidex.utils.custom_storage.PublicStaticStorage'   
    STATICFILES_DIRS = [
        BASE_DIR / "static",
    ]

    CORS_ALLOWED_ORIGINS = [
        "https://staging.digidex.app",
        "https://www.staging.digidex.app",
        "https://cdn.staging.digidex.app",
    ]
    CORS_ALLOW_CREDENTIALS = True
    CORS_ALLOW_HEADERS = [
        'access-control-allow-origin',
        "content-type",
        "authorization",
        'x-requested-with'
    ]
    CORS_ALLOW_METHODS = [
        "GET",
        "POST",
    ]

else:
    DEBUG = True
    ALLOWED_HOSTS = ["localhost", "10.0.0.218"]

    SECURE_PROXY_SSL_HEADER = None
    SESSION_COOKIE_SECURE = False
    CSRF_COOKIE_SECURE = False
    SECURE_SSL_REDIRECT = False

    STATIC_URL = '/static/'
    MEDIA_URL = '/media/'

    DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'
    STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'static'),
    ]
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    

PRIVATE_FILE_STORAGE = 'digidex.utils.custom_storage.PrivateMediaStorage'

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'storages',
    'rest_framework',
    'corsheaders',
    'bootstrap5',
    'digidex.accounts.apps.AccountConfig',
    'digidex.api',
    'digidex.inventory',
    'digidex.journal',
    'digidex.link',
    'digidex.main',
    'digidex.taxonomy',
    'digidex.utils',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'digidex.accounts.middleware.UserActivityMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'digidex.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'digidex.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('DATABASE_NAME'),
        'USER': os.environ.get('DATABASE_USER'),
        'PASSWORD': os.environ.get('DATABASE_PASSWORD'),
        'HOST': os.environ.get('DATABASE_HOST'),
        'PORT': os.environ.get('DATABASE_PORT'),
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

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

AUTH_USER_MODEL = "accounts.User"

SITE_HOST = 'www.digidex.app'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.office365.com'
EMAIL_HOST_USER = 'support@digidex.app'
DEFAULT_FROM_EMAIL = 'no-reply@digidex.app'
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
EMAIL_PORT = 587
EMAIL_USE_SSL = False
EMAIL_USE_TLS = True

LOGIN_REDIRECT_URL = 'inventory:digit-storage'
LOGIN_URL = 'accounts:login'

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
