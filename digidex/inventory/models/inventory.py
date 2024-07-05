import uuid

from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from wagtail.models import Page, Collection
from wagtail.documents import get_document_model
from wagtail.images import get_image_model
from wagtail.fields import RichTextField

from .nfc import NearFieldCommunicationTag


DigiDexImageModel = get_image_model()
DigiDexDocumentModel = get_document_model()


class Inventory(Page):
    """
    Acts as the index for all inventory items, categories, and notes.
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

    subpage_types = [
        'inventory.InventoryProfile',
    ]


class InventoryProfile(Inventory):

    parent_page_types = [
        'inventory.Inventory',
    ]

    subpage_types = [
        'inventory.InventoryCategory',
        'inventory.InventoryItem',
        'inventory.InventoryNote'
    ]

    class Meta:
        verbose_name = _("inventory profile"),
        verbose_name_plural = _("inventory profiles")


class InventoryCategory(Inventory):
    parent_page_types = [
        'inventory.InventoryProfile',
    ]

    subpage_types = [
        'inventory.InventoryItem',
        'inventory.InventoryNote',
    ]


    class Meta:
        verbose_name = _("inventory category")
        verbose_name_plural = _("inventory catagories")


class InventoryItem(Inventory):
    parent_page_types = [
        'inventory.InventoryProfile',
        'inventory.InventoryCategory',
    ]

    subpage_types = [
        'inventory.InventoryNote'
    ]

    class Meta:
        verbose_name = _("inventory item")
        verbose_name_plural = _("inventory items")


class InventoryNote(Inventory):
    image = models.ForeignKey(
        DigiDexImageModel,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    document = models.ForeignKey(
        DigiDexDocumentModel,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    parent_page_types = [
        'inventory.InventoryProfile',
        'inventory.InventoryCategory',
        'inventory.InventoryItem',
    ]

    subpage_types = []

    class Meta:
        verbose_name = _("inventory note")
        verbose_name_plural = _("inventory notes")


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
