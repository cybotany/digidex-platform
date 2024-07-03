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
    uuid = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False,
        db_index=True
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='owner'
    )
    description = models.TextField(
        blank=True,
        null=True
    )
    slug = models.SlugField(
        max_length=100,
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    last_modified = models.DateTimeField(
        auto_now=True
    )


class InventoryCategory(Inventory):
    pass


class InventoryItem(Inventory):
    pass


class InventoryNote(models.Model):
    uuid = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False,
        db_index=True
    )
    inventory = models.ForeignKey(
        Inventory,
        on_delete=models.CASCADE,
        related_name='notes'
    )
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
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    last_modified = models.DateTimeField(
        auto_now=True
    )


class InventoryLink(NearFieldCommunicationTag):
    inventory = models.OneToOneField(
        Inventory,
        on_delete=models.SET_NULL,
        related_name='nfc_link',
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
        verbose_name = "NFC Mapping"
        verbose_name_plural = "NFC Mappings"
