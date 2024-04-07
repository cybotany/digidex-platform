from .base import *
from dotenv import load_dotenv

DEBUG = False

ALLOWED_HOSTS = ['localhost', 'digidex.app', 'www.digidex.app']

AWS_ACCESS_KEY_ID = 'your-access-key'
AWS_SECRET_ACCESS_KEY = 'your-secret-key'

AWS_STORAGE_BUCKET_NAME = 'your-bucket-name'
AWS_S3_ENDPOINT_URL = 'https://nyc3.digitaloceanspaces.com'  # Change to your region
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
AWS_LOCATION = 'static'
AWS_DEFAULT_ACL = 'public-read'

STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATIC_URL = f'https://{AWS_STORAGE_BUCKET_NAME}.nyc3.digitaloceanspaces.com/{AWS_LOCATION}/'
# Media files
DEFAULT_FILE_STORAGE = 'digidex.storage_backends.MediaStorage'