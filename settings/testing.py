from __future__ import absolute_import, unicode_literals

from .development import *  # noqa

MEDIA_ROOT = "/tmp"

SECRET_KEY = "fake"

EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"
INSTALLED_APPS += ("tests",)
