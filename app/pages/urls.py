from django.urls import re_path

from . import views


app_name = "pages"

urlpatterns = [
    re_path(r"^$", views.index, name="index"),
    re_path(r"^blog/?$", views.blog, name="blog"),
    re_path(r"^blog/(?P<slug>[\w-]+)/?$", views.blog_post, name="blog_post"),
]
