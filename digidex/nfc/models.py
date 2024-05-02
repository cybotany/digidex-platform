import uuid

from django.db import models
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
    digit = models.OneToOneField(
        'inventory.UserDigitizedObject',
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

    def get_serial_number(self):
        return self.serial_number

    def get_digit(self):
        if not self.digit:
            raise ValidationError(_("No associated digit found for this tag."))
        return self.digit

    def get_digit_page_url(self):
        digit = self.get_digit()
        if not hasattr(digit, 'page'):
            raise ValidationError(_("DigitPage does not exist for the associated digit."))
        return digit.page.url

    class Meta:
        verbose_name = "NTAG"
        verbose_name_plural = "NTAGs"
