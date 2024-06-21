import uuid

from django.db import models

from modelcluster.fields import ParentalKey
from wagtail.api import APIField
from wagtail.models import Collection, Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, InlinePanel

from .note import Note, NoteGalleryImage
from .nfc import NearFieldCommunicationLink


class AssetPage(Page):
    uuid = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False,
        db_index=True,
        verbose_name="Inventory Category UUID"
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

    api_fields = [
        APIField('uuid'),
        APIField('name'),
        APIField('description'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('name'),
        FieldPanel('description'),
        InlinePanel('notes', label="Longitudinal Asset Notes"),
    ]

    parent_page_types = [
        'inventory.TrainerPage',
        'inventory.CategoryPage'
    ]

    subpage_types = []

    def __str__(self):
        return f"Asset: {self.name}"


class AssetNote(Note):
    page = models.ForeignKey(
        AssetPage,
        on_delete=models.CASCADE,
        related_name='notes'
    )

    api_fields = [
        APIField('uuid'),
        APIField('entry'),
        APIField('created_at'),
        APIField('last_modified'),
    ]

    def __str__(self):
        return f"Asset Note: {self.uuid}"


class AssetNoteGalleryImage(NoteGalleryImage):
    note = ParentalKey(
        AssetNote,
        on_delete=models.CASCADE,
        related_name='gallery_images'
    )

    api_fields = [
        APIField('image'),
    ]


class AssetNearFieldCommunicationLink(NearFieldCommunicationLink):
    page = models.OneToOneField(
        AssetPage,
        on_delete=models.SET_NULL,
        null=True,
        related_name='nfc'
    )

    def __str__(self):
        return f"Asset NFC: {self.uuid}"