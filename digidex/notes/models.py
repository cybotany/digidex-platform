import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _

from wagtail.models import Collection
from wagtail.documents import get_document_model
from wagtail.images import get_image_model
from wagtail.fields import RichTextField


DigiDexImageModel = get_image_model()
DigiDexDocumentModel = get_document_model()

class BaseNote(Collection):
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
    body = RichTextField(
        blank=True,
        null=True,
        verbose_name=_("body")
    )

    class Meta:
        verbose_name = _("inventory note")
        verbose_name_plural = _("inventory notes")
