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
        context['digit_panel'] = self.page_panel
        context['journal_cards'] = self.page_cards
        return context

    @property
    def page_panel(self):
        return self.digital_object.get_panel_details()

    @property
    def page_cards(self):
        card_list = []
        entries = self.digital_object.journal.list_entries()
        for entry in entries:
            card_list.append(entry.get_card_details())
        return card_list


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

    def get_panel_details(self):
        return {
            'name': self.display_name,
            'description': self.display_description,
            'date': self.display_date,
            'image_url': self.image_url,
            'delete_url': self.delete_url,
            'update_url': self.update_url
        }

    def get_card_details(self):
        return {
            'name': self.display_name,
            'description': self.display_description,
            'date': self.display_date,
            'page_url': self.page_url
        } 

    def __str__(self):
        return self.display_name


class DigitalObjectJournalEntry(Orderable, JournalEntry):
    page = ParentalKey(
        'inventory.DigitalObjectPage',
        on_delete=models.CASCADE,
        related_name='journal_entries',
    )
