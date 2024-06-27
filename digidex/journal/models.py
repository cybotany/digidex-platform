import uuid

from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

from modelcluster.models import ClusterableModel
from modelcluster.fields import ParentalKey

from wagtail.api import APIField
from wagtail.images import get_image_model
from wagtail.fields import RichTextField
from wagtail.models import Orderable
from wagtail.admin.panels import FieldPanel, InlinePanel


DigiDexImageModel = get_image_model()

class Note(ClusterableModel):
    uuid = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False,
        db_index=True
    )
    entry = RichTextField(
        blank=True,
        null=True
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
        APIField('entry'),
        APIField('created_at'),
        APIField('last_modified'),
    ]

    panels = [
        FieldPanel('entry'),
        InlinePanel('images', label="Image Gallery"),
    ]


class NoteImageGallery(Orderable):
    image = models.ForeignKey(
        DigiDexImageModel,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    note = ParentalKey(
        Note,
        related_name='images'
    )

    api_fields = [
        APIField('image'),
    ]

    panels = [
        FieldPanel('image'),
    ]
