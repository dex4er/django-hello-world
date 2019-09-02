import os
import sys

import environ

env = environ.Env()

# Read env from the file
READ_ENV = env.str("READ_ENV", default="")
if READ_ENV:
    env.read_env(READ_ENV)

# Debug mode
DEBUG = env.bool("DEBUG", default=False)
DEBUG_TOOLBAR_PATCH_SETTINGS = env.bool("DEBUG_TOOLBAR_PATCH_SETTINGS", default=False)
INTERNAL_IPS = env.list("INTERNAL_IPS", default=["localhost", "127.0.0.1", "::1"])
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=INTERNAL_IPS)

# Application definition
PROJECT_NAME = env.str(
    "PROJECT_NAME", default=os.path.basename(os.path.dirname(os.path.abspath(__file__)))
)
ROOT_URLCONF = PROJECT_NAME + ".urls"
WSGI_APPLICATION = PROJECT_NAME + ".wsgi.application"

PROJECT_APPS = [PROJECT_NAME, PROJECT_NAME + ".blog"]

BASE_APPS = [
    "werkzeug_debugger_runserver",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "model_utils",
    "tz_detect",
    "adminsortable2",
    "django_createuser",
    "django_migrations_ignore_attrs",
    "django_prometheus",
    "django_pyc",
]

EXTRA_BASE_APPS = env.list("EXTRA_BASE_APPS", default=[])
LOCAL_APPS = env.list("LOCAL_APPS", default=[])

INSTALLED_APPS = EXTRA_BASE_APPS + BASE_APPS + PROJECT_APPS + LOCAL_APPS

# Middleware definition
BASE_MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "tz_detect.middleware.TimezoneMiddleware",
]

EXTRA_BASE_MIDDLEWARE = env.list("EXTRA_BASE_MIDDLEWARE", default=[])
LOCAL_MIDDLEWARE = env.list("LOCAL_MIDDLEWARE", default=[])

MIDDLEWARE = (
    ["django_prometheus.middleware.PrometheusBeforeMiddleware"]
    + EXTRA_BASE_MIDDLEWARE
    + BASE_MIDDLEWARE
    + LOCAL_MIDDLEWARE
    + ["django_prometheus.middleware.PrometheusAfterMiddleware"]
)

# Internationalization
LANGUAGE_CODE = env.str("LANGUAGE_CODE", default="en-us")
TIME_ZONE = env.str("TIME_ZONE", "GMT")
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Default directories

# /opt/django-hello-world
SITE_DIR = env.str(
    "SITE_DIR",
    default=os.path.realpath(
        os.path.dirname(
            os.environ.get("VIRTUAL_ENV", os.path.dirname(os.path.abspath(__file__)))
        )
    ),
)

# /opt/django-hello-world/lib/python*/site-packages/django_hello_world
PROJECT_DIR = env.str("PROJECT_DIR", default=os.path.dirname(os.path.abspath(__file__)))

# /opt/django-hello-world/run
RUN_DIR = env.str("RUN_DIR", default=os.path.join(SITE_DIR, "run"))

# Static files (CSS, JavaScript, Images)
STATIC_URL = env.str("STATIC_URL", default="/static/")

# /opt/django-hello-world/run/static
STATIC_ROOT = env.str("STATIC_ROOT", default=os.path.join(RUN_DIR, "static"))

STATICFILES_DIRS = []

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    "django.contrib.staticfiles.finders.FileSystemFinder",
]

STATICFILES_STORAGE = env.str(
    "STATICFILES_STORAGE", default="whitenoise.storage.CompressedStaticFilesStorage"
)

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "APP_DIRS": True,
        "DIRS": [os.path.join(PROJECT_DIR, "templates")],
        "OPTIONS": {
            "context_processors": [
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.request",
            ],
            "debug": DEBUG,
        },
    }
]

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
MEDIA_URL = env.str("MEDIA_URL", default="/media/")

# /opt/django-hello-world/run/media
MEDIA_ROOT = os.path.join(RUN_DIR, "media")

# Revproxy
USE_X_FORWARDED_HOST = env.bool("USE_X_FORWARDED_HOST", default=True)

# SuspiciousOperation (TooManyFields)
DATA_UPLOAD_MAX_NUMBER_FIELDS = None

# Django Jet
JET_CHANGE_FORM_SIBLING_LINKS = False

# REST API settings
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        # 'rest_framework.authentication.BasicAuthentication',
        "rest_framework.authentication.TokenAuthentication",
        "rest_framework.authentication.SessionAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": [
        # 'rest_framework.permissions.AllowAny',
        "rest_framework.permissions.IsAuthenticated"
    ],
}

# Database
DATABASES = {
    "default": env.db("DATABASE_DEFAULT_URL"),
    "django": env.db("DATABASE_DJANGO_URL"),
}

DATABASE_TEST_CHARSET = env.str("DATABASE_CHARSET", default="utf8")
DATABASE_TEST_COLLCATION = env.str("DATABASE_COLLCATION", default="utf8_unicode_ci")

for db in DATABASES.values():
    if db["ENGINE"].split(".")[-1] == "mysql":
        db["OPTIONS"] = db.get("OPTIONS") or {}
        if "read_default_file" in db["OPTIONS"]:
            if not os.path.isabs(db["OPTIONS"]["read_default_file"]):
                db["OPTIONS"]["read_default_file"] = os.path.abspath(
                    os.path.join(SITE_DIR, ".my.cnf")
                )
        db["TEST"] = {
            "NAME": "test_" + db["NAME"],
            "CHARSET": DATABASE_TEST_CHARSET,
            "COLLATION": DATABASE_TEST_COLLCATION,
        }

# Hints for DB router
DATABASE_FOR_APPS = env.dict(
    "DATABASE_FOR_APPS",
    default=dict(
        [(k.split(".")[-1], "default") for k in PROJECT_APPS] + [("*", "django")]
    ),
)

DATABASE_ROUTERS = ["django_database_for_apps.Router"]

# Logging
DJANGO_LOG_FORMAT = env.str(
    "DJANGO_LOG_FORMAT", "full" if sys.stdout.isatty() else "verbose"
)
DJANGO_LOG_LEVEL = env.str("DJANGO_LOG_LEVEL", "DEBUG")

LOGGING = {
    "version": 1,
    "disable_existing_loggers": True,
    "formatters": {
        "simple": {"format": "{message}", "style": "{"},
        "verbose": {
            "format": "{levelname:>8} {name} {module} {thread:d} {message}",
            "style": "{",
        },
        "full": {
            "format": "{asctime} {process:d} {levelname:>8} {name} {module} {thread:d} {message}",
            "style": "{",
        },
    },
    "handlers": {
        "full": {
            "level": DJANGO_LOG_LEVEL,
            "class": "logging.StreamHandler",
            "formatter": "full",
        },
        "verbose": {
            "level": DJANGO_LOG_LEVEL,
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
        "simple": {
            "level": DJANGO_LOG_LEVEL,
            "class": "logging.StreamHandler",
            "formatter": "simple",
        },
        "mail_admins": {"class": "logging.NullHandler"},
        "null": {"class": "logging.NullHandler"},
    },
    "loggers": {
        "django": {
            "handlers": [DJANGO_LOG_FORMAT],
            "propagate": True,
            "level": "DEBUG",
        },
        "django.request": {
            "handlers": [DJANGO_LOG_FORMAT],
            "propagate": False,
            "level": "DEBUG",
        },
        "django.server": {
            "handlers": [DJANGO_LOG_FORMAT],
            "propagate": False,
            "level": "DEBUG",
        },
        "django.template": {
            "handlers": [DJANGO_LOG_FORMAT],
            "propagate": False,
            "level": env.str("DJANGO_TEMPLATE_LOG_DEVEL", default="INFO"),
        },
        "django.db.backends": {
            "handlers": [DJANGO_LOG_FORMAT],
            "propagate": False,
            "level": env.str("DJANGO_DB_LOG_DEVEL", default="INFO"),
        },
        "django_python3_ldap": {
            "handlers": [DJANGO_LOG_FORMAT],
            "propagate": True,
            "level": "DEBUG",
        },
        "werkzeug": {"handlers": ["simple"], "propagate": True, "level": "DEBUG"},
        "werkzeug_debugger_runserver": {
            "handlers": ["simple"],
            "propagate": True,
            "level": "DEBUG",
        },
    },
}

# Secret key
SECRET_KEY = env.str("SECRET_KEY", "")
SECRET_FILE = env.str("SECRET_FILE", default=os.path.join(RUN_DIR, "secret", "key.txt"))

if SECRET_FILE and not SECRET_KEY:
    try:
        with open(SECRET_FILE) as f:
            SECRET_KEY = f.read().strip()
    except FileNotFoundError:
        import random

        SECRET_KEY = "".join(
            [
                random.SystemRandom().choice(
                    "abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)"
                )
                for i in range(50)
            ]
        )
        with open(SECRET_FILE, "w") as f:
            f.write(SECRET_KEY)
