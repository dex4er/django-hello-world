# pylint: disable=unused-import

import os

from project.settings_local import ALLOWED_HOSTS, DEBUG, DEBUG_TOOLBAR_PATCH_SETTINGS, EXTRA_BASE_APPS, EXTRA_MIDDLEWARE, LOCAL_APPS, LOCAL_MIDDLEWARE  # NOQA
from project.settings_dirs import BASE_DIR, PROJECT_DIR, PROJECT_DIRNAME, SITE_DIR  # NOQA
from project.settings_db import DATABASES  # NOQA
from project.settings_email import EMAIL_BACKEND, EMAIL_HOST, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD, EMAIL_PORT, EMAIL_USE_TLS  # NOQA
from project.settings_log import LOGGING  # NOQA
from project.settings_secret import SECRET_FILE, SECRET_KEY  # NOQA

ROOT_URLCONF = 'project.urls'

WSGI_APPLICATION = 'project.wsgi.application'


# Application definition

PROJECT_APPS = [
    'hello_world'
]

BASE_APPS = [
    'werkzeug_debugger_runserver',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'model_utils',
]

INSTALLED_APPS = EXTRA_BASE_APPS + BASE_APPS + PROJECT_APPS + LOCAL_APPS


# Middleware definition

BASE_MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

MIDDLEWARE = EXTRA_MIDDLEWARE + BASE_MIDDLEWARE + LOCAL_MIDDLEWARE


# Internationalization

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)

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

MEDIA_URL = '/media/'

# /home/app/site/media
MEDIA_ROOT = os.path.join(SITE_DIR, 'media')


# Internal IP addresses for DEBUG mode
INTERNAL_IPS = ['127.0.0.1', '::1']

# Revproxy
USE_X_FORWARDED_HOST = True
