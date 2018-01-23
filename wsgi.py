"""
WSGI config for app project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""
import os

from django.core.wsgi import get_wsgi_application
from dotenv import load_dotenv


dot_env = os.path.join(os.path.dirname(__file__), '.env')
if os.path.isfile(dot_env):
    load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.production")

application = get_wsgi_application()
