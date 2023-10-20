from django.db import models
from django.contrib.auth import get_user_model


class Tag(models.Model):
    """
    Represents an NFC tag.

    Attributes:
        serial_number (str): The serial number of the NFC tag.
        created_at (datetime): The date and time when the NFC tag was created.
        updated_at (datetime): The date and time when the NFC tag was last updated.
        created_by (User): The user who created the NFC tag.
        active (bool): Whether the NFC tag is currently active.
    """
    serial_number = models.CharField(
        max_length=255,
        unique=True,
        verbose_name="Tag Serial Number"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Created At"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Updated At"
    )
    created_by = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    active = models.BooleanField(
        default=False,
        verbose_name="Active"
    )

    def __str__(self):
        """
        Returns a string representation of the NFC tag, using its serial number.

        Returns:
            str: A string representation of the NFC tag.
        """
        return self.serial_number

    class Meta:
        verbose_name = "NFC Tag"
        verbose_name_plural = "NFC Tags"