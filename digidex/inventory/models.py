import uuid

from django.db import models

from modelcluster.fields import ParentalKey
from wagtail.models import Collection, Page, Orderable
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, InlinePanel

from journal.models import Note


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
        'trainer.TrainerPage'
    ]

    subpage_types = [
        'asset.AssetPage'
    ]

    def __str__(self):
        return f"Inventory: {self.name}"


class InventoryPageNote(Orderable, Note):
    page = ParentalKey(
        InventoryPage,
        on_delete=models.CASCADE,
        related_name='notes'
    )

    def __str__(self):
        return f"Inventory Journal Entry {self.uuid}"
