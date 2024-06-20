import uuid
from django.db import models

from modelcluster.fields import ParentalKey
from wagtail.models import Collection, Page, Orderable
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, InlinePanel

from .note import Note


class TrainerPage(Page):
    uuid = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False,
        db_index=True,
        verbose_name="User Profile UUID"
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
        blank=True,
        help_text="Short Biography about the user."
    )

    content_panels = Page.content_panels + [
        FieldPanel('introduction'),
        InlinePanel('notes', label="Longitudinal Trainer Notes"),
    ]

    parent_page_types = [
        'home.HomePage'
    ]

    subpage_types = [
        'inventory.InventoryPage',
        'inventory.AssetPage'
    ]

    class Meta:
        verbose_name = "User Profile Page"


class TrainerPageNote(Orderable, Note):
    page = ParentalKey(
        TrainerPage,
        on_delete=models.CASCADE,
        related_name='notes'
    )

    def __str__(self):
        return f"Trainer Journal Entry {self.uuid}"
