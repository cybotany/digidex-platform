import uuid

from django.db import models
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class NearFieldCommunicationTag(models.Model):
    """
    Base class for NFC (Near Field Communication) technology, providing common attributes.

    Attributes:
        uuid (UUIDField): The unique identifier for the Link instance.
        serial_number (CharField): The unique serial number associated with the NFC tag.
        digit (OneToOneField): The digital object associated with the NFC tag.
        active (BooleanField): A flag indicating whether the Link is active and mapped to a digital object.
        created_at (DateTimeField): The date and time when the Link instance was created.
        last_modified (DateTimeField): The date and time when the Link instance was last modified.
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
        blank=True,
        null=True,
        on_delete=models.CASCADE,
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
        return f"{self.serial_number}"

    def activate_link(self):
        self.active = True
        self.save()

    def deactivate_link(self):
        self.active = False
        self.save()

    def get_digitized_object(self):
        if not self.digitized_object:
            raise ValidationError(_("No associated digit found for this tag."))
        return self.digitized_object

    def get_absolute_url(self):
        """
        Returns the URL for the 'view-ntag' view for this specific NFC tag.
        """
        return reverse('view-ntag', kwargs={'_uuid': self.uuid})

    def get_digitized_object_url(self):
        """
        Fetch the URL for the UserDigitizedObjectPage associated with the digitized object linked to this NFC tag.
        """
        if not self.digitized_object:
            raise ValidationError(_("No associated digit found for this tag."))

        try:
            return self.digitized_object.get_associated_page_url()
        except AttributeError:
            raise ValidationError(_("The digitized object is not correctly configured to find its page."))

    class Meta:
        verbose_name = "NTAG"
        verbose_name_plural = "NTAGs"
