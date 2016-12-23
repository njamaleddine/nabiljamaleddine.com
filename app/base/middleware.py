from django.conf import settings
from django.core.exceptions import DisallowedHost

from raven import Client


class GroupDisallowedHostExceptionMiddleware(object):
    def process_response(self, request, response):
        try:
            request.get_host()
        except DisallowedHost:
            client = Client(**settings.RAVEN_CONFIG)
            client.captureException(
                fingerprint=['django.security.DisallowedHost'],
                tags={'http_host': request.META.get('HTTP_HOST', '')},
            )
        return response
