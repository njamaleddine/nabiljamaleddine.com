# -*- coding: utf-8 -*-
"""Django settings for NabilJamaleddine project.

see: https://docs.djangoproject.com/en/dev/ref/settings/
"""
from email.utils import getaddresses

import environ

from django.utils.translation import ugettext_lazy as _
from app.base.logging import CustomJSONFormatter as JSONFormatter

ROOT_DIR = environ.Path(__file__) - 2  # (/a/b/myfile.py - 2 = /a/)
APPS_DIR = ROOT_DIR.path('app')

env = environ.Env()


# MANAGER CONFIGURATION
# ------------------------------------------------------------------------------
# Developer Error Notifications
# In the format 'Full Name <email@example.com>, Full Name <anotheremail@example.com>'
ADMINS = getaddresses([
    env('DJANGO_ADMINS', default='Nabil Jamaleddine <me@nabiljamaleddine.com>')
])

# Not-necessarily-technical managers of the site. They get broken link
# notifications and other various emails.
MANAGERS = ADMINS

# INSTALLED APPS
# ==========================================================================
# List of strings representing installed apps.
# See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'django.contrib.humanize',  # Useful template tags
    'versatileimagefield',  # https://github.com/WGBH/django-versatileimagefield
    'storages',
    'app.pages',
    'app.users',
)

# INSTALLED APPS CONFIGURATION
# ==========================================================================

# django.contrib.auth
# ------------------------------------------------------------------------------
AUTH_USER_MODEL = 'users.User'
AUTHENTICATION_BACKENDS = ('django.contrib.auth.backends.ModelBackend',)

SITE_NAME = env('SITE_NAME', default="Nabil Jamaleddine's Site")
SITE_URL = env('SITE_URL', default="http://www.nabiljamaleddine.com")

# MIDDLEWARE CONFIGURATION
# ------------------------------------------------------------------------------
# List of middleware classes to use.  Order is important; in the request phase,
# this middleware classes will be applied in the order given, and in the
# response phase the middleware will be applied in reverse order.
MIDDLEWARE = (
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)


# DJANGO CORE
# ------------------------------------------------------------------------------

# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
# Defaults to false, which is safe, enable them only in development.
DEBUG = env.bool('DJANGO_DEBUG', False)

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'UTC'

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

# Languages we provide translations for
LANGUAGES = (
    ('en', _('English')),
)

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# The Python dotted path to the WSGI application that Django's internal servers
# (runserver, runfcgi) will use. If `None`, the return value of
# 'django.core.wsgi.get_wsgi_application' is used, thus preserving the same
# behavior as previous versions of Django. Otherwise this should point to an
# actual WSGI application object.
# See: https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
WSGI_APPLICATION = 'wsgi.application'

# URL CONFIGURATION
# ------------------------------------------------------------------------------
ROOT_URLCONF = 'app.urls'

# EMAIL CONFIGURATION
# ------------------------------------------------------------------------------
EMAIL_BACKEND = env('DJANGO_EMAIL_BACKEND',
                    default='django.core.mail.backends.smtp.EmailBackend')

# DATABASE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': env.db('DATABASE_URL', default='postgres://localhost/nabiljamaleddine'),
}
DATABASES['default']['ATOMIC_REQUESTS'] = True
DATABASES['default']['CONN_MAX_AGE'] = 0


# TEMPLATE CONFIGURATION
# -----------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            str(APPS_DIR.path('templates')),
        ],
        'OPTIONS': {
            'debug': DEBUG,
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ],
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
                'app.pages.context_processors.profile_info',
                'app.pages.context_processors.default_meta_tags',
                'app.pages.context_processors.site_url',
            ],
        },
    },
]

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# STATIC FILE CONFIGURATION
# -----------------------------------------------------------------------------
# Absolute path to the directory static files should be collected to.
# Example: "/var/www/example.com/static/"
# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = str(ROOT_DIR.path('.staticfiles'))

# URL that handles the static files served from STATIC_ROOT.
# Example: "http://example.com/static/", "http://static.example.com/"
# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = '/static/'

# A list of locations of additional static files
STATICFILES_DIRS = (
    str(APPS_DIR.path('static')),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# MEDIA CONFIGURATION
# ------------------------------------------------------------------------------

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = str(ROOT_DIR.path('.media'))

# URL that handles the media served from MEDIA_ROOT.
# Examples: "http://example.com/media/", "http://media.example.com/"
# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = '/media/'

# SECURITY
# -----------------------------------------------------------------------------
# Allow javascripts to read CSRF token from cookies
CSRF_COOKIE_HTTPONLY = False
# Do not allow Session cookies to be read by javascript
SESSION_COOKIE_HTTPONLY = True

SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'

# LOGGING CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#logging
# Default logging for Django. This sends an email to the site admins on every
# HTTP 500 error. Depending on DEBUG, all other log records are either sent to
# the console (DEBUG=True) or discarded by mean of the NullHandler (DEBUG=False)
# See http://docs.djangoproject.com/en/dev/topics/logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'formatters': {
        'json': {
            'format': '%(asctime)s %(message)s',
            'datefmt': '%Y-%m-%dT%H:%M:%S%z',
            '()': JSONFormatter,
        },
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'json',
        },
        'sentry': {
            'level': 'WARNING',
            'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django': {
            'handlers': ['null'],
            'propagate': False,
            'level': 'INFO',
        },
        'django.request': {
            'handlers': ['mail_admins', 'console', 'sentry'],
            'level': 'ERROR',
            'propagate': False,
        },
        'gunicorn': {
            'level': 'INFO',
            'handlers': ['console', 'sentry'],
            'propagate': False,
        },
        'app': {
            'level': 'INFO',
            'handlers': ['console', 'sentry'],
            'propagate': False,
        },
        'raven': {
            'level': 'WARNING',
            'handlers': ['console'],
            'propagate': False,
        },
        'sentry.errors': {
            'level': 'WARNING',
            'handlers': ['console'],
            'propagate': False,
        },
        # Catch All Logger -- Captures any other logging
        '': {
            'handlers': ['console', 'sentry', 'mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

PROFILE_INFO = {
    'name': 'Nabil Jamaleddine',
    'role': 'Software Engineer',
    'github': 'https://github.com/njamaleddine',
    'linkedin': 'https://www.linkedin.com/in/nabil-jamaleddine-07094240',
    'email': 'mailto:me@nabiljamaleddine.com',
}

META_TAGS = {
    'title': f'{PROFILE_INFO["name"]} | {PROFILE_INFO["role"]}',
    'keywords': (
        'Nabil Jamaleddine,Software Engineer,Engineer,Developer,Backend,'
        'Python,Django,JavaScript,PostgreSQL,Microservices,REST,GraphQL,AWS'
    ),
    'description': (
        'Nabil Jamaleddine, a Software Engineer interested in clean code, schema design, '
        'and API development.'
    ),
}
