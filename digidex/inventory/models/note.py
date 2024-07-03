import uuid

from django.db import models

from wagtail.documents import get_document_model
from wagtail.images import get_image_model


DigiDexImageModel = get_image_model()
DigiDexDocumentModel = get_document_model()

class InventoryNote(models.Model):
    uuid = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False,
        db_index=True
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
