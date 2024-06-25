import uuid

from django.db import models

from modelcluster.fields import ParentalKey
from wagtail.api import APIField
from wagtail.models import Collection, Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, InlinePanel

from nfc.models import NearFieldCommunicationLink
from journal.models import Note, NoteImageGallery


class AssetPage(Page):
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
        InlinePanel('notes', label="Longitudinal Asset Notes"),
    ]

    parent_page_types = [
        'trainer.TrainerPage',
    ]

    subpage_types = []

    def __str__(self):
        return f"Asset: {self.name}"


class AssetNote(Note):
    asset = models.ForeignKey(
        AssetPage,
        on_delete=models.CASCADE,
        related_name='notes'
    )

    def __str__(self):
        return f"Asset Note: {self.uuid}"


class AssetNoteImageGallery(NoteImageGallery):
    note = ParentalKey(
        AssetNote,
        on_delete=models.CASCADE,
        related_name='gallery_images'
    )

    panels = NoteImageGallery.panels +  [
        InlinePanel('gallery_images', label="Note Image Gallery"),
    ]


class AssetNearFieldCommunicationLink(NearFieldCommunicationLink):
    asset = models.OneToOneField(
        AssetPage,
        on_delete=models.SET_NULL,
        null=True,
        related_name='+'
    )

    def __str__(self):
        return f"Asset NFC: {self.uuid}"
