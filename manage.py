#!/usr/bin/env python
import os
import sys

from dotenv import load_dotenv

if __name__ == "__main__":

    dot_env = os.path.join(os.path.dirname(__file__), '.env')
    if os.path.isfile(dot_env):
        load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.development")

    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django  # noqa
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
    execute_from_command_line(sys.argv)
