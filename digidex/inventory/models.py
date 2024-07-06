import uuid

from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from wagtail.models import (
    WorkflowMixin,
    PreviewableMixin,
    DraftStateMixin,
    LockableMixin,
    RevisionMixin,
    TranslatableMixin,
    SpecificMixin,
    Collection
)
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel

from nearfieldcommunication.models import NearFieldCommunicationTag


class BaseInventory(
    WorkflowMixin,
    PreviewableMixin,
    DraftStateMixin,
    LockableMixin,
    RevisionMixin,
    TranslatableMixin,
    SpecificMixin,
    Collection
):
    """
    Base class for all inventory items, categories, and notes.
    """
    uuid = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False,
        db_index=True
    )
    body = RichTextField( 
        blank=True,
        null=True,
        verbose_name=_("body")
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    last_modified = models.DateTimeField(
        auto_now=True
    )

    content_panels = [
        FieldPanel('name'),
        FieldPanel('body'),
    ]

    class Meta:
        abstract = True
    

class Inventory(BaseInventory):
    """
    Acts as the index for all user-specific inventory members.
    """
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=('translation_key', 'locale'),
                name='unique_translation_key_locale_inventory_inventory'
            )
        ]
        verbose_name = _("inventory")
        verbose_name_plural = _("inventories")


class Category(Inventory):
    class Meta:
        verbose_name = _("category")
        verbose_name_plural = _("catagories")


class Item(Inventory):
    class Meta:
        verbose_name = _("item")
        verbose_name_plural = _("items")


class Link(NearFieldCommunicationTag):
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
        verbose_name = _("link")
        verbose_name_plural = _("links")
