from django.conf import settings


def profile_info(request):
    return { 'profile_info': settings.PROFILE_INFO }


def default_meta_tags(request):
    return {
        "default_meta_tags": settings.META_TAGS,
    }


def canonical_url(request):
    if request.path == '/':
        url = f'{settings.SITE_URL}'
    else:

        url = f'{settings.SITE_URL}{request.path}'

    return {
        "get_canonical_url": url,
    }
