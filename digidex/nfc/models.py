import uuid
from django.db import models
from django.urls import reverse

from nfc.validators import validate_ntag_serial


class NearFieldCommunicationTag(models.Model):
    """
    Represents an NFC (Near Field Communication) tag in the system, associated with a digitized object.

    This model stores information about NFC tags, which are used to link real-world objects with digital records.

    Attributes:
        uuid (UUIDField): Auto-generated unique identifier for each NFC tag.
        serial_number (CharField): Unique serial number of the NFC tag. Used for physical identification.
        digit (OneToOneField): Optional link to the user digit that this NFC tag maps to.
        active (BooleanField): Status flag indicating whether the NFC tag is active (in use).
        created_at (DateTimeField): Timestamp indicating when the record was first created.
        last_modified (DateTimeField): Timestamp indicating when the record was last updated.
    """
    NTAG_TYPES = (
        ('NTAG 213', 'NTAG 213'),
        ('NTAG 215', 'NTAG 215'),
        ('NTAG 216', 'NTAG 216'),
    )

    uuid = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True
    )
    serial_number = models.CharField(
        max_length=32,
        unique=True,
        db_index=True,
        validators=[validate_ntag_serial]
    )
    ntag_type = models.CharField(
        max_length=50,
        choices=NTAG_TYPES,
        default='NTAG 213'
    )
    digital_object = models.OneToOneField(
        'inventory.DigitalObject',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="ntag"
    )
    active = models.BooleanField(
        default=False
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    last_modified = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        """Return the serial number as the string representation of the NFC tag."""
        return self.serial_number

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

    @property
    def url(self):
        """
        Constructs the absolute URL to view this specific NFC tag.

        Returns:
            A URL path as a string.
        """
        if not self.active:
            return None
        return reverse('nfc:route_ntag', kwargs={'ntag_uuid': self.uuid})

    @property
    def digit_page(self):
        """
        Retrieves the URL for the web page associated with the digitized object of this NFC tag.

        Raises:
            ValidationError: If no digitized object is associated, or the digitized object does not support URL retrieval.

        Returns:
            A URL path as a string.
        """
        if hasattr(self, 'digital_object'):
            return self.digital_object.page
        return None

    class Meta:
        verbose_name = "NTAG"
        verbose_name_plural = "NTAGs"

    @classmethod
    def get_queryset(cls):
        return super().get_queryset().select_related('digital_object')
