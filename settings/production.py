# -*- coding: utf-8 -*-
"""Production Settings"""
import logging

from . import __version__
from .common import *  # noqa


# SITE CONFIGURATION
# Hosts/domain names that are valid for this site.
# ------------------------------------------------------------------------------
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')

# DATABASE CONFIGURATION
# ------------------------------------------------------------------------------
# Raises ImproperlyConfigured exception if DATABASE_URL not in os.environ
# Should not override all db settings
DATABASES['default'].update(env.db('DATABASE_URL'))

# DEBUG
# ------------------------------------------------------------------------------
DEBUG = False
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG
TEMPLATES[0]['OPTIONS']['loaders'] = [
    ('django.template.loaders.cached.Loader', [
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    ]),
]
# SECRET CONFIGURATION
# ------------------------------------------------------------------------------
SECRET_KEY = env('DJANGO_SECRET_KEY')

# If your Django app is behind a proxy that sets a header to specify secure
# connections, AND that proxy ensures that user-submitted headers with the
# same name are ignored (so that people can't spoof it), set this value to
# a tuple of (header_name, header_value). For any requests that come in with
# that header/value, request.is_secure() will return True.
# WARNING! Only set this if you fully understand what you're doing. Otherwise,
# you may be opening yourself up to a security risk.

# TODO: Enable when we get an SSL Certificate
# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

SITE_SCHEME = env('SITE_SCHEME', default='http')

if SITE_SCHEME == 'https':
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True

INSTALLED_APPS += ('gunicorn', )


# Email settings
# ------------------------------------------------------------------------------
DEFAULT_FROM_EMAIL = env('DEFAULT_FROM_EMAIL', default='me@nabiljamaleddine.com')
# EMAIL_HOST = env('EMAIL_HOST')
# EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
# EMAIL_HOST_USER = env('EMAIL_HOST_USER')
# EMAIL_PORT = env.int('EMAIL_PORT', default=587)
EMAIL_USE_TLS = True
SERVER_EMAIL = DEFAULT_FROM_EMAIL

# Sentry
# ------------------------------------------------------------------------------
INSTALLED_APPS += ('raven.contrib.django.raven_compat',)
RAVEN_CONFIG = {
    'CELERY_LOGLEVEL': logging.ERROR,
    'dsn': env('SENTRY_DSN'),
    'environment': SITE_ENVIRONMENT,
    'release': __version__,
}
