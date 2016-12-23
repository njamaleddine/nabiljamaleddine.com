from django.db import models


class PostManager(models.Manager):

    def get_queryset(self):
        return super(PostManager, self).get_queryset().select_related(
            'author'
        ).prefetch_related('tags')
