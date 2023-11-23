"""
Django settings for cybotany project.
"""
import os
from pathlib import Path
from datetime import timedelta
from apps.utils.helpers import get_secret

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Fetch the environment variable indicating the environment.
DJANGO_ENV = os.environ.get('DJANGO_ENV', 'development')
REGION_NAME = os.environ.get('REGION_NAME', 'us-east-1d')

# Fetching grouped secrets
api_secrets = get_secret('cybotany-api', environment=DJANGO_ENV, region_name=REGION_NAME)
db_secrets = get_secret('cybotany-db', environment=DJANGO_ENV, region_name=REGION_NAME)
aws_secrets = get_secret('cybotany-keys', environment=DJANGO_ENV, region_name=REGION_NAME)

# AWS S3 secrets
SECRET_KEY = aws_secrets['DJANGO_SECRET_KEY']  
AWS_ACCESS_KEY_ID = aws_secrets['AWS_S3_ACCESS_KEY']
AWS_SECRET_ACCESS_KEY = aws_secrets['AWS_S3_SECRET_ACCESS_KEY']
AWS_STORAGE_BUCKET_NAME = aws_secrets['AWS_STORAGE_BUCKET_NAME'] 
AWS_S3_REGION_NAME = aws_secrets['AWS_S3_REGION_NAME'] 
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
AWS_DEFAULT_ACL = None

ALLOWED_HOSTS = [
    "10.0.0.218",
    "www.cybotany.io",
    "cybotany.io",
]

# API secrets
OPENAI_API_KEY = api_secrets['OPENAI_API_KEY']
OPEN_WEATHER_MAP_API_KEY = api_secrets['OPEN_WEATHER_MAP_API_KEY']
PLANT_ID_API_KEY = api_secrets['PLANT_ID_API_KEY']

CORS_ALLOW_HEADERS = [
    "content-type",
    "authorization",
]

CORS_ALLOW_METHODS = [
    "GET",
    "POST",
]

# Environment specific settings
if DJANGO_ENV == 'production':
    DEBUG = False
    STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    STATIC_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/static/"
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/'
    CORS_ALLOW_ALL_ORIGINS = False
    CORS_ALLOWED_ORIGINS = [
        "http://127.0.0.1:8080",
        "https://cybotany.com"
    ]
else:
    DEBUG = True
    STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    MEDIA_URL = '/media/'
    CORS_ALLOW_ALL_ORIGINS = True

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
    'apps.api',
    #'apps.accounts',
    'apps.accounts.apps.AccountConfig',
    'apps.botany',
    'apps.chatbot',
    'apps.utils',
    'apps.nfc',
    'apps.itis',
    'apps.core',
    'apps.groups',
    'bootstrap5',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'cybotany.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'cybotany.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': db_secrets['DATABASE_NAME'],
        'USER': db_secrets['DATABASE_USER'],
        'PASSWORD': db_secrets['DATABASE_PASSWORD'],
        'HOST': db_secrets['DATABASE_HOST'],
        'PORT': db_secrets['DATABASE_PORT'],
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
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
        'rest_framework.permissions.AllowAny',],
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

LOGIN_REDIRECT_URL = 'landing-page'
LOGIN_URL = '/accounts/login/'