import uuid
from django.db import models

from modelcluster.fields import ParentalKey
from wagtail.api import APIField
from wagtail.models import Collection, Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, InlinePanel

from .note import Note, NoteGalleryImage
from .nfc import NearFieldCommunicationLink


class TrainerPage(Page):
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
    introduction = RichTextField(
        null=True,
        blank=True
    )

    api_fields = [
        APIField('uuid'),
        APIField('introduction'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('introduction'),
        InlinePanel('notes', label="Longitudinal Trainer Notes"),
    ]

    parent_page_types = [
        'home.HomePage'
    ]

    subpage_types = [
        'home.CategoryPage',
        'home.AssetPage'
    ]


class TrainerNote(Note):
    page = ParentalKey(
        TrainerPage,
        on_delete=models.CASCADE,
        related_name='notes'
    )

    def __str__(self):
        return f"Trainer Note: {self.uuid}"


class TrainerNoteGalleryImage(NoteGalleryImage):
    note = ParentalKey(
        TrainerNote,
        on_delete=models.CASCADE,
        related_name='gallery_images'
    )

    panels = NoteGalleryImage.panels +  [
        InlinePanel('gallery_images', label="Note Image Gallery"),
    ]


class TrainerNearFieldCommunicationLink(NearFieldCommunicationLink):
    page = models.OneToOneField(
        TrainerPage,
        on_delete=models.SET_NULL,
        null=True,
        related_name='nfc'
    )

    def __str__(self):
        return f"Trainer NFC: {self.uuid}"
