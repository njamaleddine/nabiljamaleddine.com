from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^blog/?$', views.blog, name='blog'),
    url(r'^blog/(?P<slug>\S+)/?$', views.blog_post, name='blog_post'),
]
