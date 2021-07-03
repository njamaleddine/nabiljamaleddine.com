# -*- coding: utf-8 -*-
from django.http import Http404
from django.shortcuts import render
from django.views.decorators.cache import cache_page
from markdown import Markdown

from .models import Post, Tag


@cache_page(60 * 60)
def index(request):
    """Homepage"""
    context = {"page": "index"}
    return render(request, "index.html", context)


@cache_page(60 * 15)
def blog(request):
    """Display all blog posts"""
    context = {"page": "blog"}
    tag_params = request.GET.get("tags")
    if tag_params:
        tags = tag_params.split(",")
        for tag in tags:
            posts = (
                Post.objects.filter(
                    tags__in=Tag.objects.filter(name__icontains=tag).values_list(
                        "id", flat=True
                    )
                )
                .order_by("-published")
                .distinct()
            )
    else:
        posts = Post.objects.all().order_by("-published")
    context["posts"] = posts
    return render(request, "blog.html", context)


@cache_page(60 * 15)
def blog_post(request, slug):
    """
    Return a single blog post and read the content from a markdown file

    Blog post slugs are unique
    """
    context = {"page": "blog_post"}
    post = Post.objects.filter(slug=slug).first()
    if post:
        context["post"] = post
        context["tags"] = [tag.name for tag in post.tags.all()]
        with open(post.markdown_file.path, encoding="utf-8") as post_content:
            # convert blog post markdown into html
            context["content"] = Markdown(
                extensions=[
                    "markdown.extensions.fenced_code",
                    "markdown.extensions.codehilite",
                ]
            ).convert(post_content.read())
        return render(request, "blog_post.html", context)
    raise Http404("Page Not Found")
