# -*- coding: utf-8 -*-
""" Run Tests and Linting for project """
from subprocess import call

from django.core.management.base import BaseCommand

from django.conf import settings


class Command(BaseCommand):
    help = 'Create a django app in the proper directory'

    def add_arguments(self, parser):
        parser.add_argument('app_name', nargs='?')

    def handle(self, *args, **options):
        arguments = ['python', '../manage.py', 'startapp']
        if options.get('app_name'):
            arguments.append(options['app_name'])

        call(arguments, cwd=str(settings.APPS_DIR))
