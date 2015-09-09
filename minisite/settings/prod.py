from dev import *

import dj_database_url

DATABASES['default'] = dj_database_url.config()

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ALLOWED_HOSTS = ['skliar.herokuapp.com']

STATIC_ROOT = 'staticfiles'

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATABASES = {
    'default': {
             'ENGINE': 'django.db.backends.postgresql_psycopg2',
             'NAME': 'd9hot5t75935ag',
             'USER': 'javxneutvfsgve',
             'PASSWORD': 'mDoxBDWreCXVyjLcx58_Djjhn1',
             'HOST': 'ec2-54-235-162-144.compute-1.amazonaws.com',
             'PORT': '5432'}
}
