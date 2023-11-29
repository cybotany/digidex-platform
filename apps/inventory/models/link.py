from django.db import models
from django.urls import reverse

class Link(models.Model):
    """
    Represents a link between a digitized object and the inventory system within the CyBotany application.

    The Link model is primarily used to connect physical objects (like plants) that have been digitized
    (through an NFC tag or similar technology) to their digital representations and metadata in the system.
    Each link is uniquely identified by a serial number and is associated with a secret hash for secure
    identification and access.

    Attributes:
        serial_number (CharField): The unique serial number of the Link, typically associated with
                                   the physical NFC tag or other identification mechanism.
        active (BooleanField): A flag indicating whether the Link is active and mapped to a digital object. Inactive
                               links may represent unused or deactivated tags.
        secret_hash (CharField): The hash of a secret key associated with the Link. This is used for
                                 secure verification and is not the actual secret key itself.

    Methods:
        get_absolute_url: Returns the absolute URL for the Link instance, typically used for redirecting
                          users to the appropriate view based on the link's status and associated data.
    """

    serial_number = models.CharField(
        max_length=255,
        unique=True,
        verbose_name="Tag Serial Number",
        help_text="The unique serial number associated with the NFC tag or identification mechanism."
    )
    active = models.BooleanField(
        default=False,
        verbose_name="Active",
        help_text="Indicates whether the link is currently active and mapped to a digital object."
    )
    secret_hash = models.CharField(
        max_length=64,
        editable=False,
        verbose_name="Secret Hash",
        help_text="The hash of a secret key for secure identification and access."
    )

    def get_absolute_url(self):
        """
        Generates the absolute URL for the Link instance.

        This method constructs a URL that can be used to handle requests related to this particular Link.
        The URL depends on whether the Link is active and whether it has an associated secret hash.

        Returns:
            str: The absolute URL for handling this Link instance, or None if the link is inactive or lacks a secret hash.
        """
        if self.active and self.secret_hash:
            return reverse('inventory:link-handling', kwargs={'secret_hash': self.secret_hash})
        return None

    def __str__(self):
        """
        Returns a string representation of the Link instance.

        This representation is primarily based on the unique serial number of the Link.

        Returns:
            str: The serial number of the Link, representing its unique identification.
        """
        return self.serial_number

    class Meta:
        verbose_name = "Link"
        verbose_name_plural = "Links"
        help_text = "Represents connections between physical objects and their digital representations in the inventory system."
