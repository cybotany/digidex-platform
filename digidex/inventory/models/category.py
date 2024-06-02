import uuid
from django.db import models

from modelcluster.fields import ParentalKey
from wagtail.fields import RichTextField
from wagtail.models import Page, Orderable

from .journal import JournalEntry

class InventoryCategoryPage(Page):
    uuid = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False,
        db_index=True,
        verbose_name="Inventory Category UUID"
    )
    name = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        default='Category',
        help_text="Inventory Category Name."
    )
    description = RichTextField(
        blank=True,
        null=True,
        help_text="Inventory Category description."
    )
    is_party = models.BooleanField(
        default=False,
        help_text="Indicates if this is the Party category."
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    last_modified = models.DateTimeField(
        auto_now=True
    )

    parent_page_types = [
        'inventory.UserProfilePage'
    ]

    subpage_types = [
        'inventory.InventoryCategoryPage'
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        return context

    class Meta:
        verbose_name = "Inventory Category Page"

class UserInventoryCategory(Orderable):
    page = ParentalKey(
        'inventory.UserProfilePage',
        on_delete=models.CASCADE,
        related_name='inventory_categories'
    )
    detail_page = models.OneToOneField(
        'inventory.InventoryCategoryPage',
        on_delete=models.CASCADE,
        related_name='+'
    )


class InventoryCategoryJournalEntry(Orderable, JournalEntry):
    page = ParentalKey(
        'inventory.InventoryCategoryPage',
        on_delete=models.CASCADE,
        related_name='journal_entries',
    )
