"""
Django settings for project project.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

from .settings_local import *  # NOQA
from .settings_dirs import *  # NOQA
from .settings_db import *  # NOQA
from .settings_email import *  # NOQA
from .settings_log import *  # NOQA
from .settings_secret import *  # NOQA


ROOT_URLCONF = 'project.urls'

WSGI_APPLICATION = 'project.wsgi.application'


# Application definition
# https://docs.djangoproject.com/en/1.10/ref/applications/

BASE_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'model_utils',
    'django_extensions',
    'hello_world',
]

INSTALLED_APPS = EXTRA_APPS + BASE_APPS + LOCAL_APPS


# Middleware definition
# https://docs.djangoproject.com/en/1.10/topics/http/middleware/

BASE_MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

MIDDLEWARE_CLASSES = EXTRA_MIDDLEWARE + BASE_MIDDLEWARE + LOCAL_MIDDLEWARE


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'

# /home/app/site/static
STATIC_ROOT = os.path.join(SITE_DIR, 'static')

STATICFILES_DIRS = [
    # /home/app/site/base/static
    os.path.join(BASE_DIR, 'static'),
]

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR + '/templates',
            # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
        ],
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
                'apptemplates.Loader',
                # 'django.template.loaders.eggs.Loader',
            ],
            'debug': DEBUG
        },
    },
]


# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# https://docs.djangoproject.com/en/1.10/topics/files/

MEDIA_URL = '/media/'

# /home/app/site/media
MEDIA_ROOT = os.path.join(SITE_DIR, 'media')


# Internal IP addresses for DEBUG mode
INTERNAL_IPS = ['127.0.0.1', '::1']

# Revproxy
USE_X_FORWARDED_HOST = True
