import uuid

from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from wagtail.models import Page, Collection
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel

from notes.models import Note
from nearfieldcommunication.models import NearFieldCommunicationTag


class BaseInventory(Page):
    """
    Base class for all inventory items, categories, and notes.
    """
    uuid = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False,
        db_index=True
    )
    name = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        verbose_name=_("name")
    )
    body = RichTextField( 
        blank=True,
        null=True,
        verbose_name=_("body")
    )
    collection = models.OneToOneField(
        Collection,
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    last_modified = models.DateTimeField(
        auto_now=True
    )

    content_panels = Page.content_panels + [
        FieldPanel('name'),
        FieldPanel('body'),
    ]

    class Meta:
        abstract = True
    

class Inventory(BaseInventory):
    """
    Acts as the index for all user-specific inventory members.
    """
    subpage_types = [
        'inventory.InventoryCategory',
        'inventory.InventoryItem',
    ]

    class Meta:
        verbose_name = _("inventory")
        verbose_name_plural = _("inventories")


class InventoryCategory(Inventory):
    parent_page_types = [
        'inventory.Inventory',
    ]

    subpage_types = [
        'inventory.InventoryItem',
    ]


    class Meta:
        verbose_name = _("inventory category")
        verbose_name_plural = _("inventory catagories")


class InventoryItem(Inventory):
    parent_page_types = [
        'inventory.Inventory',
        'inventory.InventoryCategory',
    ]

    subpage_types = []

    class Meta:
        verbose_name = _("inventory item")
        verbose_name_plural = _("inventory items")


class InventoryLink(NearFieldCommunicationTag):
    inventory = models.OneToOneField(
        Inventory,
        on_delete=models.SET_NULL,
        related_name='+',
        null=True
    )

    def __str__(self):
        if self.inventory:
            return f"{self} for {self.inventory}"
        return f"{self} available for mapping"

    def get_url(self):
        """
        Constructs the absolute URL to view this specific NFC tag.

        Returns:
            A URL path as a string.
        """
        return reverse('nfc:route_nfc', kwargs={'link_uuid': self.uuid})

    class Meta:
        verbose_name = _("inventory nfc mapping")
        verbose_name_plural = _("inventory nfc mappings")


class InventoryNote(Note):
    inventory = models.ForeignKey(
        Inventory,
        on_delete=models.CASCADE,
        related_name='notes',
        null=False
    )

    def __str__(self):
        return f"Notes for {self.inventory}"

    class Meta:
        verbose_name = _("inventory notes")
        verbose_name_plural = _("inventory notes")
