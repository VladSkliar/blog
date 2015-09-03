from common import *

EMAIL_BACKEND = "djrill.mail.backends.djrill.DjrillBackend"

MANDRILL_API_KEY = "84r7I2irZA34F-bdxMPsYQ"

DEBUG = True

DATABASES = {
    'default': {
             'ENGINE': 'django.db.backends.postgresql_psycopg2',
             'NAME': 'd29j9j5j5gqn15',
             'USER': 'hchknkhewtptde',
             'PASSWORD': 'FGyHQP94PNWhZuPb0hEZOcVB90',
             'HOST': 'ec2-107-21-106-196.compute-1.amazonaws.com',
             'PORT': '5432'}
}
