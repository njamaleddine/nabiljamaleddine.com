from django.conf import settings
from django.urls import include, re_path


urlpatterns = [
    re_path(r"^", include("app.pages.urls", namespace="pages")),
]

if settings.DJANGO_ADMIN_ENABLED:
    from django.contrib import admin

    urlpatterns += [
        re_path(r"^admin/", admin.site.urls),
    ]

    admin.site.site_header = f"{settings.SITE_NAME} Admin"


if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        re_path(r"^__debug__/", include(debug_toolbar.urls)),
    ]
