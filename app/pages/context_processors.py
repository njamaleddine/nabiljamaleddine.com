from django.conf import settings


def profile_info(request):
    return { 'profile_info': settings.PROFILE_INFO }


def default_meta_tags(request):
    return {
        "default_meta_tags": settings.META_TAGS,
    }


def site_url(request):
    return {
        "site_url": settings.SITE_URL,
    }
