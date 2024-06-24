import uuid

from django.db import models

from modelcluster.fields import ParentalKey
from wagtail.api import APIField
from wagtail.models import Collection, Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, InlinePanel

from .note import Note, NoteGalleryImage
from .nfc import NearFieldCommunicationLink


class CategoryPage(Page):
    uuid = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False,
        db_index=True
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
        InlinePanel('notes', label="Longitudinal Category Notes"),
    ]

    parent_page_types = [
        'inventory.TrainerPage'
    ]

    subpage_types = [
        'inventory.AssetPage'
    ]

    def __str__(self):
        return f"Category: {self.name}"


class CategoryNote(Note):
    page = models.ForeignKey(
        CategoryPage,
        on_delete=models.CASCADE,
        related_name='notes'
    )

    def __str__(self):
        return f"Category Note: {self.uuid}"


class CategoryNoteGalleryImage(NoteGalleryImage):
    note = ParentalKey(
        CategoryNote,
        on_delete=models.CASCADE,
        related_name='gallery_images'
    )

    panels = NoteGalleryImage.panels +  [
        InlinePanel('gallery_images', label="Category Note Image Gallery"),
    ]


class CategoryNearFieldCommunicationLink(NearFieldCommunicationLink):
    page = models.OneToOneField(
        CategoryPage,
        on_delete=models.SET_NULL,
        null=True,
        related_name='nfc'
    )

    def __str__(self):
        return f"Category NFC: {self.uuid}"
