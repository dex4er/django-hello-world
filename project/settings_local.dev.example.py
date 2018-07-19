# Settings for development

from typing import List

DEBUG = True

EXTRA_BASE_APPS: List[str] = [
]

LOCAL_APPS = [
    'debug_toolbar',
]

EXTRA_MIDDLEWARE: List[str] = [
]

LOCAL_MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

DEBUG_TOOLBAR_PATCH_SETTINGS = True

ALLOWED_HOSTS = ['*']
