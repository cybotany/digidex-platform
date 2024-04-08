from .base import *

DEBUG = False

ALLOWED_HOSTS = ['localhost', 'digidex.app']

AWS_ACCESS_KEY_ID = os.environ.get('SPACES_ACCESS_KEY', '')
AWS_SECRET_ACCESS_KEY = os.environ.get('SPACES_SECRET_KEY', '')

AWS_STORAGE_BUCKET_NAME = os.environ.get('SPACES_BUCKET_NAME', '')
AWS_S3_ENDPOINT_URL = os.environ.get('SPACES_ENDPOINT_URL', '')
AWS_S3_CUSTOM_DOMAIN = os.environ.get('SPACES_CUSTOM_DOMAIN', '')

AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
AWS_LOCATION = 'static'
AWS_DEFAULT_ACL = 'public-read'

STATIC_URL = '{}/{}/'.format(AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)

STATIC_ROOT = 'static/'
MEDIA_ROOT = 'media/'

WAGTAILADMIN_BASE_URL = "https://digidex.app"
WAGTAIL_SITE_NAME = "DigiDex"
