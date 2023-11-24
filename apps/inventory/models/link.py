from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model


class Link(models.Model):
    """
    Represents a link connecting a taxonomic unit with the inventory system.

    Attributes:
        serial_number (str): The serial number of the Link.
        created_at (datetime): The date and time when the Link was created.
        created_by (User): The user who created the Link.
        active (bool): Whether the Link is currently active.
        secret (str): A secret string used for generating the hash stored on the Link.
        secret_hash (str): The hash of the secret, stored on the Link.
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
    secret = models.CharField(
        max_length=64,
        editable=False,
        verbose_name="Secret"
    )
    secret_hash = models.CharField(
        max_length=64,
        editable=False,
        verbose_name="Secret Hash"
    )

    def get_absolute_url(self):
        """
        Generates the absolute URL for the Link instance.
        """
        if self.active and self.secret_hash:
            return reverse('inventory:link-handling', kwargs={'secret_hash': self.secret_hash})
        return None  # or some default URL if the link is not active or doesn't have a secret_hash


    def __str__(self):
        """
        Returns a string representation of the link, using its serial_number.
        """
        return self.serial_number

    class Meta:
        verbose_name = "Link"
        verbose_name_plural = "Links"
