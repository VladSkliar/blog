"""
Django settings for minisite project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""
from django.core.urlresolvers import reverse_lazy
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import sys
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = 'd6%)2hin&dzkai1ycfqd(4q^cx*t(rj7tr+otzl^5g7!g54&@j'

DEBUG = False

TEMPLATE_DEBUG = True

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
    )

ALLOWED_HOSTS = []


TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
)
# Application definition
sys.path.append(os.path.join(BASE_DIR, 'apps'))

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    'info',
    'blog',

    'sorl.thumbnail',
    'disqus',
    'ckeditor',
    'rosetta',
    'djrill',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'solid_i18n.middleware.SolidLocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'info.middleware.HttpRequestSaver',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)


MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

MEDIA_URL = '/media/'

ROOT_URLCONF = 'minisite.urls'

WSGI_APPLICATION = 'minisite.wsgi.application'

LOGIN_URL = reverse_lazy('login')

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGES = (
    ('en', (u'English')),
    ('uk', (u'Ukrainian')),
)
LANGUAGE_CODE = 'en'

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'collect_static/')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),

)

CKEDITOR_UPLOAD_PATH = "uploads/"

CKEDITOR_UPLOAD_SLUGIFY_FILENAME = False

CKEDITOR_RESTRICT_BY_USER = True

SITE_ID = 1

SOLID_I18N_USE_REDIRECTS = False

DEFAULT_FROM_EMAIL = 'admin@skliarblog.com'
