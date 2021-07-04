from django.conf import settings


def canonical_url(request):
    if request.path == "/":
        url = f"{settings.SITE_URL}"
    else:
        url = f"{settings.SITE_URL}{request.path}"

    return {
        "get_canonical_url": url,
    }


def site_settings(request):
    return {
        "default_meta_tags": settings.META_TAGS,
        "profile_info": settings.PROFILE_INFO,
        "site_name": settings.SITE_NAME,
        "site_url": settings.SITE_URL,
    }
