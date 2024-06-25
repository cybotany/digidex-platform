import uuid

from django.db import models

from wagtail.images import get_image_model
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel


CustomImageModel = get_image_model()

class Note(models.Model):
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
    image = models.ForeignKey(
        CustomImageModel,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    last_modified = models.DateTimeField(
        auto_now=True
    )

    panels = [
        FieldPanel('entry'),
        FieldPanel('image'),
    ]

    class Meta:
        abstract = True
