import uuid

from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from modelcluster.models import ClusterableModel

from wagtail.models import (
    WorkflowMixin,
    PreviewableMixin,
    DraftStateMixin,
    LockableMixin,
    RevisionMixin,
    TranslatableMixin,
    SpecificMixin,
    Collection,
)
from wagtail.documents import get_document_model
from wagtail.images import get_image_model
from wagtail.search import index

from .note import Note
from .nfc import NearFieldCommunicationTag


DigiDexImageModel = get_image_model()
DigiDexDocumentModel = get_document_model()


class AbstractInventory(
    WorkflowMixin,
    PreviewableMixin,
    DraftStateMixin,
    LockableMixin,
    RevisionMixin,
    TranslatableMixin,
    SpecificMixin,
    Collection,
):
    class Meta:
        abstract = True


class Inventory(AbstractInventory, index.Indexed, ClusterableModel):
    """
    Represents a collection of inventory items in the system.
    """
    uuid = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False,
        db_index=True
    )
    slug = models.SlugField(
        max_length=100,
        blank=True,
        null=True
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name='owner',
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    last_modified = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"{self.name} - Inventory"

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=('translation_key', 'locale'),
                name='unique_translation_key_locale'
            )
        ]


class InventoryProfile(Inventory):
    def __str__(self):
        return f"{self.name} - Profile"

    class Meta:
        verbose_name = "Inventory Profile"
        verbose_name_plural = "Inventory Profiles"


class InventoryCategory(Inventory):
    def __str__(self):
        return f"{self.name} - Category"

    class Meta:
        verbose_name = "Inventory Category"
        verbose_name_plural = "Inventory Categories"


class InventoryItem(Inventory):
    def __str__(self):
        return f"{self.name} - Item"

    class Meta:
        verbose_name = "Inventory Item"
        verbose_name_plural = "Inventory Items"


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
    body = models.ForeignKey(
        Note,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    def __str__(self):
        return f"{self.name} - Note"

    class Meta:
        verbose_name = "Inventory Note"
        verbose_name_plural = "Inventory Notes"


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
        verbose_name = "Inventory NFC Mapping"
        verbose_name_plural = "Inventory NFC Mappings"
