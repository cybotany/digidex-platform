import uuid

from django.db import models

from wagtail.fields import RichTextField


class DigitizedObject(models.Model):
    """
    Base class for digitized objects, providing common attributes.

    Attributes:
        name (CharField): The name of the digitized object.
        uuid (UUIDField): The unique identifier for the digitized object.
        description (RichTextField): A detailed description of the digitized object.
        created_at (DateTimeField): The date and time the digitized object was created.
        last_modified (DateTimeField): The date and time the digitized object was last modified.
    """
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
        blank=False
    )
    description = RichTextField(
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    last_modified = models.DateTimeField(
        auto_now=True
    )
