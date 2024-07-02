import uuid

from django.conf import settings
from django.db import models
from wagtail.models import Collection


class Organism(models.Model):
    uuid = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False,
        db_index=True
    )
    slug = models.SlugField(
        max_length=100,
        blank=False,
        null=False
    )
    collection = models.ForeignKey(
        Collection,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    name = models.CharField(
        max_length=100,
        blank=False,
        null=False
    )
    description = models.TextField(
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    last_modified = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"Organism: {self.name}"


class Inventory(models.Model):
    uuid = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False,
        db_index=True
    )
    slug = models.SlugField(
        max_length=100,
        blank=False,
        null=False
    )
    collection = models.ForeignKey(
        Collection,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    name = models.CharField(
        max_length=100,
        blank=False,
        null=False
    )
    description = models.TextField(
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    last_modified = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"Inventory: {self.name}"


class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="inventory_userprofile",
    )
    uuid = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False,
        db_index=True
    )
    slug = models.SlugField(
        max_length=100,
        blank=False,
        null=False
    )
    collection = models.ForeignKey(
        Collection,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )


import uuid

from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

from wagtail.api import APIField
from wagtail.images import get_image_model
from wagtail.admin.panels import FieldPanel


DigiDexImageModel = get_image_model()

class JournalEntry(models.Model):
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
    entry = models.TextField(
        null=False
    )
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE
    )
    object_id = models.PositiveIntegerField(
        db_index=True
    )
    content_object = GenericForeignKey(
        'content_type',
        'object_id'
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    last_modified = models.DateTimeField(
        auto_now=True
    )

    api_fields = [
        APIField('uuid'),
        APIField('image'),
        APIField('entry'),
        APIField('created_at'),
        APIField('last_modified'),
    ]

    panels = [
        FieldPanel('image'),
        FieldPanel('entry'),
    ]

    def get_formatted_date(self):
        return self.created_at.strftime('%B %d, %Y')

    def get_card(self):
        return {
            'uuid': self.uuid,
            'image': self.image,
            'entry': self.entry,
            'date': self.get_formatted_date(),
        }


import uuid

from django.db import models
from django.urls import reverse

from .validators import validate_ntag_serial


class NearFieldCommunicationTag(models.Model):
    """
    Represents an NFC (Near Field Communication) tag in the system, associated with a digitized object.

    This model stores information about NFC tags, which are used to link real-world objects with digital records.

    Attributes:
        uuid (UUIDField): Auto-generated unique identifier for each NFC tag.
        serial_number (CharField): Unique serial number of the NFC tag. Used for physical identification.
        active (BooleanField): Status flag indicating whether the NFC tag is active (in use).
        created_at (DateTimeField): Timestamp indicating when the record was first created.
        last_modified (DateTimeField): Timestamp indicating when the record was last updated.
    """
    PLANT_LABEL = 'PL'
    DOG_TAG = 'DT'
    CAT_TAG = 'CT'
    BUBBLE_STICKER = 'BS'
    REGULAR_STICKER = 'RS'
    WET_INLAY = 'WI'
    DRY_INLAY = 'DI'
    NTAG_FORM_CHOICES = {
        PLANT_LABEL: 'Plant Label',
        DOG_TAG: 'Dog Tag',
        CAT_TAG: 'Cat Tag',
        BUBBLE_STICKER: 'Bubble Sticker',
        REGULAR_STICKER: 'Regular Sticker',
        WET_INLAY: 'Wet Inlay',
        DRY_INLAY: 'Dry Inlay',
    }
    uuid = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
        db_index=True
    )
    serial_number = models.CharField(
        max_length=32,
        editable=False,
        unique=True,
        db_index=True,
        validators=[validate_ntag_serial]
    )
    tag_form = models.CharField(
        max_length=2,
        choices=NTAG_FORM_CHOICES,
        default=REGULAR_STICKER
    )
    active = models.BooleanField(
        default=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    last_modified = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        """Return the serial number as the string representation of the NFC tag."""
        return f"{self.NTAG_FORM_CHOICES[self.tag_form]} {self.id}"

    def activate_link(self):
        """
        Activates the NFC tag, indicating it is in use and linked to an object.

        This sets the 'active' field to True and saves the instance.
        """
        self.active = True
        self.save()

    def deactivate_link(self):
        """
        Deactivates the NFC tag, indicating it is not currently in use.

        This sets the 'active' field to False and saves the instance.
        """
        self.active = False
        self.save()

    class Meta:
        verbose_name = "nfc tag"
        verbose_name_plural = "nfc tags"


class NearFieldCommunicationLink(models.Model):
    uuid = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False,
        db_index=True
    )
    tag = models.OneToOneField(
        NearFieldCommunicationTag,
        on_delete=models.CASCADE,
        related_name='nfc_link'
    )
    organism = models.OneToOneField(
        'inventory.Organism',
        on_delete=models.CASCADE,
        related_name='+',
        null=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    last_modified = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"{self.tag} - {self.asset}"

    def get_url(self):
        """
        Constructs the absolute URL to view this specific NFC tag.

        Returns:
            A URL path as a string.
        """
        return reverse('nfc:route_nfc', kwargs={'link_uuid': self.uuid})

    class Meta:
        verbose_name = "nfc mapping"
        verbose_name_plural = "nfc mappings"
