from django.conf import settings
from django.db import models

from inventory.models import Digit


class NearFieldCommunicationTag(models.Model):
    """
    Base class for NFC (Near Field Communication) technology, providing common attributes.

    Attributes:
        serial_number (CharField): The unique serial number associated with the NFC tag.
        user (ForeignKey): The user who created the journal entry, linked to the user model.
        active (BooleanField): A flag indicating whether the Link is active and mapped to a digital object.
        created_at (DateTimeField): The date and time when the Link instance was created.
        last_modified (DateTimeField): The date and time when the Link instance was last modified.
    """
    serial_number = models.CharField(
        max_length=32,
        unique=True,
        db_index=True,
        verbose_name="Tag Serial Number",
        help_text="The unique serial number associated with the NFC tag."
    )
    digit = models.ForeignKey(
        Digit,
        on_delete=models.CASCADE,
        related_name="nfc_tags",
        verbose_name="Digital Object",
        help_text="The digital object linked to the NFC tag."
    )
    active = models.BooleanField(
        default=False,
        verbose_name="Active",
        help_text="Indicates whether the link is currently active and mapped to a digital object."
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Created At",
        help_text="The date and time when the link instance was created."
    )
    last_modified = models.DateTimeField(
        auto_now=True,
        verbose_name="Last Modified",
        help_text="The date and time when the link instance was last modified."
    )

    def __str__(self):
        """
        Returns a string representation of the NTAG instance, primarily based on its unique serial number.
        """
        return f"{self.serial_number}"

    def activate_link(self):
        """
        Activates the link, associating it with a user and setting it as active.
        """
        self.active = True
        self.save()

    def deactivate_link(self):
        """
        Deactivates the link, making it inactive.
        """
        self.active = False
        self.save()

    class Meta:
        verbose_name = "NTAG"
        verbose_name_plural = "NTAGs"
