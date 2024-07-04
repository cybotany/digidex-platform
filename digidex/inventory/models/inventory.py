import uuid

from django.conf import settings
from django.db import models
from django.urls import reverse

from wagtail.models import Collection
from wagtail.documents import get_document_model
from wagtail.images import get_image_model

from .nfc import NearFieldCommunicationTag


DigiDexImageModel = get_image_model()
DigiDexDocumentModel = get_document_model()

class Inventory(Collection):
    """
    Represents a collection of inventory items in the system.
    
    Root Node
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
        return f"Inventory Collection: {self.name}"


class InventoryProfile(Inventory):

    def get_catagories(self):
        return self.categories.all()

    def get_items(self):
        return self.items.all()

    def __str__(self):
        return f"{self} - Profile"

    class Meta:
        verbose_name = "Inventory Profile"
        verbose_name_plural = "Inventory Profiles"


class InventoryCategory(Inventory):

    def get_items(self):
        return self.items.all()

    def __str__(self):
        return f"{self} - Category"

    class Meta:
        verbose_name = "Inventory Category"
        verbose_name_plural = "Inventory Categories"


class InventoryItem(Inventory):
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
    entry = models.TextField(
        null=False
    )

    def __str__(self):
        return f"{self} - Journal"

    class Meta:
        verbose_name = "Inventory Journal Entry"
        verbose_name_plural = "Inventory Journal Entries"


class InventoryLink(NearFieldCommunicationTag):
    inventory = models.OneToOneField(
        Inventory,
        on_delete=models.SET_NULL,
        related_name='+',
        null=True
    )

    def __str__(self):
        return f"Link for {self.inventory}"

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
