# -*- coding: utf-8 -*-
from django.db import models
from django.urls import reverse
from uuid_upload_path import upload_to

from app.base.models import TimeStampedUUIDModel
from app.users.models import User
from .managers import PostManager


class Tag(TimeStampedUUIDModel):
    """A Tag associated with a Post"""

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Post(TimeStampedUUIDModel):
    """A Blog post"""

    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=100, unique=True)
    published = models.DateTimeField()
    summary = models.TextField(max_length=500)
    markdown_file = models.FileField(upload_to=upload_to)
    tags = models.ManyToManyField(Tag)

    objects = PostManager()

    class Meta:
        ordering = ("-published", "-created")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("pages:blog_post", kwargs={"slug": self.slug})
