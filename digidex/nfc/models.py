import uuid
from django.db import models
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class NearFieldCommunicationTag(models.Model):
    """
    Represents an NFC (Near Field Communication) tag in the system, associated with a digitized object.

    This model stores information about NFC tags, which are used to link real-world objects with digital records.

    Attributes:
        uuid (UUIDField): Auto-generated unique identifier for each NFC tag.
        serial_number (CharField): Unique serial number of the NFC tag. Used for physical identification.
        digitized_object (OneToOneField): Optional link to a digitized object that this NFC tag represents.
        active (BooleanField): Status flag indicating whether the NFC tag is active (in use).
        created_at (DateTimeField): Timestamp indicating when the record was first created.
        last_modified (DateTimeField): Timestamp indicating when the record was last updated.
    """

    uuid = models.UUIDField(
        default=uuid.uuid4, 
        editable=False, 
        unique=True
    )
    serial_number = models.CharField(
        max_length=32,
        unique=True,
        db_index=True
    )
    digitized_object = models.OneToOneField(
        'digitization.DigitizedObject',
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

    def get_absolute_url(self):
        """
        Constructs the absolute URL to view this specific NFC tag.

        Returns:
            A URL path as a string.
        """
        return reverse('nfc:route_ntag', kwargs={'_uuid': self.uuid})

    def get_digitized_object(self):
        """
        Retrieves the digitized object associated with this NFC tag.

        Raises:
            ValidationError: If no digitized object is associated with this tag.

        Returns:
            The associated DigitizedObject instance.
        """
        if not self.digitized_object:
            raise ValidationError(_("No associated digit found for this tag."))
        return self.digitized_object

    def get_digitized_object_url(self):
        """
        Retrieves the URL for the web page associated with the digitized object of this NFC tag.

        Raises:
            ValidationError: If no digitized object is associated, or the digitized object does not support URL retrieval.

        Returns:
            A URL path as a string.
        """
        _mapped_digitized_object = self.get_digitized_object()

        try:
            return _mapped_digitized_object.get_associated_page_url()
        except AttributeError:
            raise ValidationError(_("The digitized object is not correctly configured to find its page."))

    class Meta:
        verbose_name = "NTAG"
        verbose_name_plural = "NTAGs"
