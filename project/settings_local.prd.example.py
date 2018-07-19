# Settings for production

from typing import List

DEBUG = False

EXTRA_BASE_APPS: List[str] = [
]

LOCAL_APPS: List[str] = [
]

EXTRA_MIDDLEWARE: List[str] = [
]

LOCAL_MIDDLEWARE: List[str] = [
]

DEBUG_TOOLBAR_PATCH_SETTINGS = True

ALLOWED_HOSTS = ['*']  # change to host name
