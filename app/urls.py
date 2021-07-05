from django.conf import settings
from django.conf.urls import include, url


urlpatterns = [
    url(r"^", include("app.pages.urls", namespace="pages")),
]

if settings.DJANGO_ADMIN_ENABLED:
    from django.contrib import admin

    urlpatterns += [
        url(r"^admin/", admin.site.urls),
    ]

    admin.site.site_header = f"{settings.SITE_NAME} Admin"


if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        url(r"^__debug__/", include(debug_toolbar.urls)),
    ]
