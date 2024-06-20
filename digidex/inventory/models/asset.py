import uuid

from django.db import models

from modelcluster.fields import ParentalKey
from wagtail.models import Collection, Page, Orderable
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, InlinePanel

from .note import Note


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

    content_panels = Page.content_panels + [
        FieldPanel('name'),
        FieldPanel('description'),
        InlinePanel('notes', label="Longitudinal Asset Notes"),
    ]

    parent_page_types = [
        'inventory.TrainerPage',
        'inventory.InventoryPage'
    ]

    subpage_types = []

    def __str__(self):
        return f"Asset: {self.name}"


class AssetPageNote(Orderable, Note):
    page = ParentalKey(
        AssetPage,
        on_delete=models.CASCADE,
        related_name='notes'
    )

    def __str__(self):
        return f"Asset Journal Entry {self.uuid}"
