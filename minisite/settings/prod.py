from dev import *

import dj_database_url

DATABASES['default'] = dj_database_url.config()

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ALLOWED_HOSTS = ['skliar.herokuapp.com']

STATIC_ROOT = 'staticfiles'

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

