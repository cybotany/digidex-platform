from django.db import models
from django.utils.translation import gettext_lazy as _

from modelcluster.models import ClusterableModel
from modelcluster.fields import ParentalKey

from wagtail.models import Orderable
from wagtail.fields import RichTextField
from wagtail.images import get_image_model
from wagtail.documents import get_document_model
from wagtail.admin.panels import FieldPanel, InlinePanel


class JournalEntry(ClusterableModel):
    page = ParentalKey(
        "InventoryAssetPage",
        on_delete=models.deletion.CASCADE,
        related_name='journal_entries'
    )
    note = RichTextField(
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
        FieldPanel('note'),
        InlinePanel('gallery_documents', label="Document"),
        InlinePanel('gallery_images', label="Image"),
    ]

    def __str__(self):
        return f"Journal entry for {self.page.name}"


class JournalGalleryDocument(Orderable):
    journal_entry = ParentalKey(
        JournalEntry,
        on_delete=models.deletion.CASCADE,
        related_name='gallery_documents'
    )
    document = models.ForeignKey(
        get_document_model(),
        on_delete=models.deletion.CASCADE,
        related_name='+'
    )

    panels = [
        FieldPanel('document'),
    ]


class JournalGalleryImage(Orderable):
    journal_entry = ParentalKey(
        JournalEntry,
        on_delete=models.deletion.CASCADE,
        related_name='gallery_images'
    )
    image = models.ForeignKey(
        get_image_model(),
        on_delete=models.deletion.CASCADE,
        related_name='+'
    )

    panels = [
        FieldPanel('image'),
    ]
