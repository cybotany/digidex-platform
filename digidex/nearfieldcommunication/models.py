import uuid
import re

from django.urls import reverse
from django.core.exceptions import ValidationError
from django.db import models


def validate_ntag_serial(value):
    pattern = re.compile(r'^([A-Za-z0-9]{2}:){6}[A-Za-z0-9]{2}$')
    if not pattern.match(value):
        raise ValidationError(
            '%(value)s is not a valid NTAG serial number',
            params={'value': value},
        )

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

    def get_url(self):
        return reverse('nfc:route_nfc_link', kwargs={'nfc_uuid': self.uuid})

    class Meta:
        verbose_name = "nfc tag"
        verbose_name_plural = "nfc tags"
