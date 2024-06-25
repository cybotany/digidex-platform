import uuid
from django.db import models

from modelcluster.fields import ParentalKey
from wagtail.api import APIField
from wagtail.models import Collection, Page, Orderable
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, InlinePanel

from nfc.models import NearFieldCommunicationLink
from journal.models import Note, NoteImageGallery


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
    ]

    parent_page_types = [
        'home.HomePage'
    ]

    subpage_types = [
        'asset.AssetPage'
    ]


class TrainerNote(Note):
    trainer = models.ForeignKey(
        TrainerPage,
        on_delete=models.CASCADE,
        related_name='notes'
    )

    def __str__(self):
        return f"Trainer Note: {self.uuid}"


class TrainerNoteImageGallery(NoteImageGallery):
    note = ParentalKey(
        TrainerNote,
        on_delete=models.CASCADE,
        related_name='gallery_images'
    )

    panels = NoteImageGallery.panels +  [
        InlinePanel('gallery_images', label="Note Image Gallery"),
    ]


class TrainerNearFieldCommunicationLink(NearFieldCommunicationLink):
    trainer = models.OneToOneField(
        TrainerPage,
        on_delete=models.SET_NULL,
        null=True,
        related_name='+'
    )

    def __str__(self):
        return f"Trainer NFC: {self.uuid}"
