import uuid

from django.db import models

from modelcluster.models import ClusterableModel
from wagtail.api import APIField
from wagtail.images import get_image_model
from wagtail.fields import RichTextField
from wagtail.models import Orderable
from wagtail.admin.panels import FieldPanel


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
    ]


class NoteGalleryImage(Orderable):
    image = models.ForeignKey(
        DigiDexImageModel,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    api_fields = [
        APIField('image'),
    ]

    panels = [
        FieldPanel('image'),
    ]
