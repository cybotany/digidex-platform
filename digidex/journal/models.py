import uuid

from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

from wagtail.api import APIField
from wagtail.images import get_image_model
from wagtail.admin.panels import FieldPanel


DigiDexImageModel = get_image_model()

class JournalEntry(models.Model):
    uuid = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False,
        db_index=True
    )
    image = models.ForeignKey(
        DigiDexImageModel,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    entry = models.TextField(
        null=False
    )
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE
    )
    object_id = models.PositiveIntegerField(
        db_index=True
    )
    content_object = GenericForeignKey(
        'content_type',
        'object_id'
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    last_modified = models.DateTimeField(
        auto_now=True
    )

    api_fields = [
        APIField('uuid'),
        APIField('image'),
        APIField('entry'),
        APIField('created_at'),
        APIField('last_modified'),
    ]

    panels = [
        FieldPanel('image'),
        FieldPanel('entry'),
    ]
