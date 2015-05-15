"""
Django settings for project project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

from settings_local import *  # @UnusedWildImport
from settings_dirs import *  # @UnusedWildImport
from settings_db import *  # @UnusedWildImport
from settings_email import *  # @UnusedWildImport
from settings_log import *  # @UnusedWildImport
from settings_secret import *  # @UnusedWildImport
from settings_suit import *  # @UnusedWildImport


# Application definition

BASE_APPS = (
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'model_utils',
    'django_extensions',
    'django_pyc',
    'hello_blog',
)

INSTALLED_APPS = BASE_APPS + EXTRA_BASE_APPS + LOCAL_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'project.urls'

WSGI_APPLICATION = 'project.wsgi.application'


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'pl'

TIME_ZONE = 'Europe/Warsaw'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

# /home/app/site/static
STATIC_ROOT = os.path.join(SITE_DIR, 'static')

STATICFILES_DIRS = (
    # /home/app/site/base/static
    os.path.join(BASE_DIR, 'static'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    # 'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
)

TEMPLATE_DIRS = (
    BASE_DIR + '/templates',
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
)

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.

MEDIA_URL = '/media/'

# /home/app/site/media
MEDIA_ROOT = os.path.join(SITE_DIR, 'media')

# Revproxy
USE_X_FORWARDED_HOST = True
