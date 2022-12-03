# -*- coding: utf-8 -*-

import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _
from uuid_upload_path import upload_to
from versatileimagefield.fields import PPOIField, VersatileImageField


class UUIDModel(models.Model):
    """
    An abstract base class model that makes primary key `id` as UUID
    instead of default auto incremented number.
    """

    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)

    class Meta:
        abstract = True


class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides self-updating
    ``created`` and ``modified`` fields
    """

    created = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        abstract = True


class TimeStampedUUIDModel(TimeStampedModel, UUIDModel):
    """
    An abstract base class model that provides self-updating
    ``created`` and ``modified`` fields with UUID as primary_key field.
    """

    class Meta:
        abstract = True


class ImageMixin(models.Model):
    """
    An abstract base class model that provides a VersatileImageField Image
    with POI
    """

    image = VersatileImageField(
        upload_to=upload_to,
        blank=True,
        null=True,
        ppoi_field="image_poi",
    )
    image_poi = PPOIField(
        blank=True, null=True, verbose_name=_("Image's Point of Interest")
    )

    class Meta:
        abstract = True
