from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from apps.botany.models import Plant
import uuid


class Tag(models.Model):
    """
    Represents an NFC tag.

    Attributes:
        serial_number (str): The serial number of the NFC tag.
        created_at (datetime): The date and time when the NFC tag was created.
        last_viewed (datetime): The date and time when the NFC tag was last viewed.
        view_count (int): The count of times the NFC tag has been viewed.
        created_by (User): The user who created the NFC tag.
        active (bool): Whether the NFC tag is currently active.
        uuid (UUID): The UUID of the NFC tag.
        plant (Plant): The plant associated with the NFC tag.
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
    last_viewed = models.DateTimeField(
        auto_now=True,
        verbose_name="Last Viewed"
    )
    view_count = models.PositiveIntegerField(
        default=0,
        verbose_name="View Count"
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
    plant = models.OneToOneField(
        Plant,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='nfc_tag',
        verbose_name="Associated Plant"
    )

    def increment_view_count(self):
        """
        Increments the view count of the NFC tag and updates the last viewed timestamp.
        """
        self.view_count += 1
        self.last_viewed = timezone.now()
        self.save()

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
