"""
Django settings for cybotany project.
"""
import os
from pathlib import Path
from apps.utils.helpers import get_secret

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Fetch the environment variable indicating the environment.
DJANGO_ENV = os.environ.get('DJANGO_ENV', 'development')

# SECURITY WARNING: don't run with debug turned on in production!
SECRET_KEY = get_secret('DJANGO_SECRET_KEY')
ALLOWED_HOSTS = [get_secret('ALLOWED_HOSTS')]

# API Keys
OPENAI_API_KEY = get_secret('OPENAI_API_KEY')
OPEN_WEATHER_MAP_API_KEY = get_secret('OPEN_WEATHER_MAP_API_KEY')
PLANT_ID_API_KEY = get_secret('PLANT_ID_API_KEY')

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
    'apps.api',
    'apps.accounts',
    'apps.botany',
    'apps.cea',
    'apps.chatbot',
    'apps.utils',
    'apps.nfc',
    'apps.itis',
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
]

ROOT_URLCONF = 'cybotany.urls'

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

WSGI_APPLICATION = 'cybotany.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': get_secret('DATABASE_NAME'),
        'USER': get_secret('DATABASE_USER'),
        'PASSWORD': get_secret('DATABASE_PASSWORD'),
        'HOST': get_secret('DATABASE_HOST'),
        'PORT': get_secret('DATABASE_PORT'),
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

# Static files (CSS, JavaScript, Images)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# Amazon S3 Settings
AWS_ACCESS_KEY_ID = get_secret('AWS_S3_ACCESS_KEY')
AWS_SECRET_ACCESS_KEY = get_secret('AWS_S3_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = get_secret('AWS_STORAGE_BUCKET_NAME')
AWS_S3_REGION_NAME = get_secret('AWS_S3_REGION_NAME')
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
AWS_DEFAULT_ACL = None
MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/'

# Environment specific settings
if DJANGO_ENV == 'production':
    DEBUG = False
    # Use Amazon S3 for static files in production
    STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    STATIC_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/static/"
    # Add any other production-specific static settings here.

else:
    DEBUG = True
    STATIC_URL = '/static/'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
}

LOGIN_REDIRECT_URL = 'home'
LOGIN_URL = '/accounts/login/'