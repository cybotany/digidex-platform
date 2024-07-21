from os import getenv

from datetime import timedelta

ACCOUNT_URL = "account.digidex"

# JWT settings
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': getenv('SECRET_KEY'),
    'VERIFYING_KEY': None,
    'AUTH_HEADER_TYPES': ('Bearer',),
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',
}

# allauth settings
AUTH_USER_MODEL = 'accounts.DigiDexUser'

ACCOUNT_AUTHENTICATION_METHOD = 'email'

SIGNUP_URL = 'account_signup'

LOGIN_URL = 'account_login'

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
