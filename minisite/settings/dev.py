from common import *

EMAIL_BACKEND = "djrill.mail.backends.djrill.DjrillBackend"

MANDRILL_API_KEY = "84r7I2irZA34F-bdxMPsYQ"

DEBUG = True

DATABASES = {
    'default': {
             'ENGINE': 'django.db.backends.postgresql_psycopg2',
             'NAME': 'mydb',
             'USER': 'vladskliar',
             'PASSWORD': 'qlewnfrup12',
             'HOST': '',
             'PORT': '5432'}
}
