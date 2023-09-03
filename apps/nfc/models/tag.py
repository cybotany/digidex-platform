from django.db import models
from django.contrib.auth import get_user_model


class NFCTag(models.Model):
    """
    Represents an NFC tag.

    Attributes:
        tag_id (str): The ID of the NFC tag.
        description (str): The description of the NFC tag.
        created_at (datetime): The date and time when the NFC tag was created.
        updated_at (datetime): The date and time when the NFC tag was last updated.
        created_by (User): The user who created the NFC tag.
    """

    tag_id = models.CharField(
        max_length=255,
        unique=True,
        verbose_name="Tag ID"
    )
    description = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Description"
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

    def __str__(self):
        """
        Returns a string representation of the NFC tag, using its tag ID.

        Returns:
            str: A string representation of the NFC tag.
        """
        return self.tag_id

    class Meta:
        verbose_name = "NFC Tag"
        verbose_name_plural = "NFC Tags"