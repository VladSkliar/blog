from dev import *

import dj_database_url

DATABASES['default'] = dj_database_url.config()

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ALLOWED_HOSTS = ['*']

STATIC_ROOT = 'staticfiles'

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATABASES = {
    'default': {
             'ENGINE': 'django.db.backends.postgresql_psycopg2',
             'NAME': 'd29j9j5j5gqn15',
             'USER': 'hchknkhewtptde',
             'PASSWORD': 'FGyHQP94PNWhZuPb0hEZOcVB90',
             'HOST': 'ec2-107-21-106-196.compute-1.amazonaws.com',
             'PORT': '5432'}
}
