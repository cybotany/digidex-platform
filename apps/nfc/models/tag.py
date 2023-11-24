from django.db import models
from django.contrib.auth import get_user_model
from apps.groups.models import Group
import uuid


class Tag(models.Model):
    """
    Represents an NFC tag.

    Attributes:
        serial_number (str): The serial number of the NFC tag.
        created_at (datetime): The date and time when the NFC tag was created.
        created_by (User): The user who created the NFC tag.
        active (bool): Whether the NFC tag is currently active.
        uuid (UUID): The UUID of the NFC tag.
        group (Group): The group associated with the NFC tag.
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
    created_by = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    active = models.BooleanField(
        default=False,
        verbose_name="Active"
    )
    uuid = models.UUIDField(
        unique=True,
        default=uuid.uuid4,
        editable=False,
        verbose_name="UUID"
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Associated Group"
    )

    def generate_uuid(self):
        """
        Generates a new UUID for the NFC tag.
        """
        self.uuid = uuid.uuid4()
        self.save()

    def __str__(self):
        """
        Returns a string representation of the NFC tag, using its uuid.
        """
        return self.uuid

    class Meta:
        verbose_name = "NFC Tag"
        verbose_name_plural = "NFC Tags"
