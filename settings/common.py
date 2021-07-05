# -*- coding: utf-8 -*-
from email.utils import getaddresses

import environ

from django.utils.translation import ugettext_lazy as _
from app.base.logging import CustomJSONFormatter as JSONFormatter

ROOT_DIR = environ.Path(__file__) - 2  # (/a/b/myfile.py - 2 = /a/)
APPS_DIR = ROOT_DIR.path("app")

env = environ.Env()


# MANAGER CONFIGURATION
ADMINS = getaddresses(
    [env("DJANGO_ADMINS", default="Nabil Jamaleddine <me@nabiljamaleddine.com>")]
)

MANAGERS = ADMINS

DJANGO_ADMIN_ENABLED = env("DJANGO_ADMIN_ENABLED", default=False)

INSTALLED_APPS = (
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "versatileimagefield",
    "storages",
    "app.pages",
    "app.users",
)

if DJANGO_ADMIN_ENABLED:
    INSTALLED_APPS = ("django.contrib.admin",) + INSTALLED_APPS

AUTH_USER_MODEL = "users.User"
AUTHENTICATION_BACKENDS = ("django.contrib.auth.backends.ModelBackend",)

SITE_NAME = env("SITE_NAME", default="Nabil Jamaleddine's Site")
SITE_URL = env("SITE_URL", default="http://www.nabiljamaleddine.com")

MIDDLEWARE = (
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
)

DEBUG = env.bool("DJANGO_DEBUG", False)

TIME_ZONE = "UTC"

USE_TZ = True

LANGUAGE_CODE = "en-us"

LANGUAGES = (("en", _("English")),)

USE_I18N = True

USE_L10N = True

WSGI_APPLICATION = "wsgi.application"

# URL CONFIGURATION
# ------------------------------------------------------------------------------
ROOT_URLCONF = "app.urls"

# EMAIL CONFIGURATION
# ------------------------------------------------------------------------------
EMAIL_BACKEND = env(
    "DJANGO_EMAIL_BACKEND", default="django.core.mail.backends.smtp.EmailBackend"
)

# DATABASE CONFIGURATION
# ------------------------------------------------------------------------------
DATABASES = {
    "default": env.db("DATABASE_URL", default="postgres://localhost/nabiljamaleddine"),
}
DATABASES["default"]["ATOMIC_REQUESTS"] = True
DATABASES["default"]["CONN_MAX_AGE"] = 0

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            str(APPS_DIR.path("templates")),
        ],
        "OPTIONS": {
            "debug": DEBUG,
            "loaders": [
                "django.template.loaders.filesystem.Loader",
                "django.template.loaders.app_directories.Loader",
            ],
            "context_processors": [
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.request",
                "app.pages.context_processors.canonical_url",
                "app.pages.context_processors.site_settings",
            ],
        },
    },
]

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# STATIC FILE CONFIGURATION
# -----------------------------------------------------------------------------
# Absolute path to the directory static files should be collected to.
# Example: "/var/www/example.com/static/"
# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = str(ROOT_DIR.path(".staticfiles"))

# URL that handles the static files served from STATIC_ROOT.
# Example: "http://example.com/static/", "http://static.example.com/"
# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = "/static/"

# A list of locations of additional static files
STATICFILES_DIRS = (str(APPS_DIR.path("static")),)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
)

# MEDIA CONFIGURATION
# ------------------------------------------------------------------------------

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = str(ROOT_DIR.path(".media"))

# URL that handles the media served from MEDIA_ROOT.
# Examples: "http://example.com/media/", "http://media.example.com/"
# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = "/media/"

# SECURITY
# -----------------------------------------------------------------------------
# Allow javascripts to read CSRF token from cookies
CSRF_COOKIE_HTTPONLY = False
# Do not allow Session cookies to be read by javascript
SESSION_COOKIE_HTTPONLY = True

SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = "DENY"

# LOGGING CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#logging
# Default logging for Django. This sends an email to the site admins on every
# HTTP 500 error. Depending on DEBUG, all other log records are either sent to
# the console (DEBUG=True) or discarded by mean of the NullHandler (DEBUG=False)
# See http://docs.djangoproject.com/en/dev/topics/logging
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {"require_debug_false": {"()": "django.utils.log.RequireDebugFalse"}},
    "formatters": {
        "json": {
            "format": "%(asctime)s %(message)s",
            "datefmt": "%Y-%m-%dT%H:%M:%S%z",
            "()": JSONFormatter,
        },
    },
    "handlers": {
        "null": {
            "level": "DEBUG",
            "class": "logging.NullHandler",
        },
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "json",
        },
        "mail_admins": {
            "level": "ERROR",
            "filters": ["require_debug_false"],
            "class": "django.utils.log.AdminEmailHandler",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["null"],
            "propagate": False,
            "level": "INFO",
        },
        "django.request": {
            "handlers": ["mail_admins", "console"],
            "level": "ERROR",
            "propagate": False,
        },
        "gunicorn": {
            "level": "INFO",
            "handlers": ["console"],
            "propagate": False,
        },
        "app": {
            "level": "INFO",
            "handlers": ["console"],
            "propagate": False,
        },
        "raven": {
            "level": "WARNING",
            "handlers": ["console"],
            "propagate": False,
        },
        # Catch All Logger -- Captures any other logging
        "": {
            "handlers": ["console", "mail_admins"],
            "level": "ERROR",
            "propagate": True,
        },
    },
}

PROFILE_INFO = {
    "name": "Nabil Jamaleddine",
    "role": "Software Engineer",
    "github": "https://github.com/njamaleddine",
    "linkedin": "https://www.linkedin.com/in/nabil-jamaleddine-07094240",
    "email": "mailto:me@nabiljamaleddine.com",
}

META_TAGS = {
    "title": env(
        "META_TITLE",
        default=f'{PROFILE_INFO["name"]} | {PROFILE_INFO["role"]}',
    ),
    "keywords": env(
        "META_KEYWORDS",
        default=(
            "Nabil Jamaleddine,Software Engineer,Engineer,Developer,Backend,"
            "Python,Django,JavaScript,PostgreSQL,Microservices,REST,GraphQL,AWS"
        ),
    ),
    "description": env(
        "META_DESCRIPTION",
        default=(
            "Nabil Jamaleddine is a software engineer who specializes in API "
            "development, data modeling, and architecture."
        ),
    ),
    "theme_color": env("META_THEME_COLOR", default="#fcfcfc"),
}
