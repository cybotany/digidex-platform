from django.db import models

class NFC(models.Model):
    """
    Abstract base class for NFC (Near Field Communication) technology, providing common attributes.

    Attributes:
        serial_number (CharField): The unique serial number associated with the NFC tag.
        manufacturer (CharField): The manufacturer of the NFC tag.
        version (CharField): The version of the NFC tag.
        counter (PositiveIntegerField): The counter value associated with the NFC tag.
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
    manufacturer = models.CharField(
        max_length=2,
        blank=True,
        verbose_name="Manufacturer",
        db_column="manufacturer_id",
        help_text="The manufacturer of the NFC tag."
    )
    version = models.CharField(
        max_length=4,
        blank=True,
        verbose_name="Version",
        help_text="The version of the NFC tag."
    )
    counter = models.PositiveIntegerField(
        default=0,
        verbose_name="Counter",
        help_text="The counter value associated with the NFC tag."
    )
    user = models.ForeignKey(
        'accounts.User',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name="User",
        help_text="The user associated with this link."
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

    class Meta:
        abstract = True
