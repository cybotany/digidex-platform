import uuid

from django.db import models

from modelcluster.fields import ParentalKey
from wagtail.models import Collection, Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, InlinePanel

from .note import Note, NoteGalleryImage
from .nfc import NearFieldCommunicationLink


class InventoryPage(Page):
    uuid = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False,
        db_index=True,
        verbose_name="Inventory UUID"
    )
    collection = models.ForeignKey(
        Collection,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    name = models.CharField(
        max_length=50
    )
    description = RichTextField(
        blank=True,
        null=True
    )

    content_panels = Page.content_panels + [
        FieldPanel('name'),
        FieldPanel('description'),
        InlinePanel('notes', label="Longitudinal Inventory Notes"),
    ]

    parent_page_types = [
        'inventory.TrainerPage'
    ]

    subpage_types = [
        'inventory.AssetPage'
    ]

    def __str__(self):
        return f"Inventory: {self.name}"


class InventoryNote(Note):
    inventory = models.ForeignKey(
        InventoryPage,
        on_delete=models.CASCADE,
        related_name='notes'
    )

    def __str__(self):
        return f"Inventory Note: {self.uuid}"


class InventoryNoteGalleryImage(NoteGalleryImage):
    note = ParentalKey(
        InventoryNote,
        on_delete=models.CASCADE,
        related_name='gallery_images'
    )


class InventoryNearFieldCommunicationLink(NearFieldCommunicationLink):
    inventory = models.OneToOneField(
        InventoryPage,
        on_delete=models.SET_NULL,
        null=True,
        related_name='nfc'
    )

    def __str__(self):
        return f"Inventory NFC: {self.uuid}"
