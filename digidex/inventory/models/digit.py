import uuid
from django.db import models

from modelcluster.fields import ParentalKey
from wagtail.fields import RichTextField
from wagtail.models import Page, Orderable

from .journal import JournalEntry


class DigitalObjectPage(Page):
    uuid = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False,
        db_index=True,
        verbose_name="Digitized Object UUID"
    )
    name = models.CharField(
        max_length=100,
        null=True,
        blank=False,
        help_text="Digitized Object Name."
    )
    description = RichTextField(
        blank=True,
        null=True,
        help_text="Digitized Object Description."
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    last_modified = models.DateTimeField(
        auto_now=True
    )

    parent_page_types = [
        'inventory.InventoryCategoryPage',
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        return context

    def __str__(self):
        return self.name.title()


class DigitalObjectCategory(Orderable):
    page = ParentalKey(
        'inventory.InventoryCategoryPage',
        on_delete=models.CASCADE,
        related_name='itemized_digits'
    )
    detail_page = models.OneToOneField(
        'inventory.DigitalObjectPage',
        on_delete=models.CASCADE,
        related_name='+'
    )


class DigitalObjectJournalEntry(Orderable, JournalEntry):
    page = ParentalKey(
        'inventory.DigitalObjectPage',
        on_delete=models.CASCADE,
        related_name='journal_entries',
    )
