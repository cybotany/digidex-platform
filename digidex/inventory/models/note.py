import uuid

from django.db import models

from modelcluster.models import ClusterableModel
from modelcluster.fields import ParentalKey
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
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    last_modified = models.DateTimeField(
        auto_now=True
    )

    panels = [
        FieldPanel('entry'),
        InlinePanel('gallery_images', label="Note Image Gallery"),
    ]

    class Meta:
        abstract = True


class NoteGalleryImage(Orderable):
    image = models.ForeignKey(
        DigiDexImageModel,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    panels = [
        FieldPanel('image'),
    ]

    class Meta:
        abstract = True
