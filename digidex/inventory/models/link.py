import uuid
from django.db import models
from django.urls import reverse


class Link(models.Model):
    """
    The Link model is primarily used to connect physical objects (like plants) that have been digitized
    (through an NFC tag or similar technology) to their digital representations and metadata in the system.

    Attributes:
        serial_number (CharField): The unique serial number associated with the NFC tag.
        counter (IntegerField): The number of times the tag has been scanned.
        user (ForeignKey): The user who created the journal entry, linked to the user model.
        active (BooleanField): A flag indicating whether the Link is active and mapped to a digital object. Inactive
                               links may represent unused or deactivated tags.
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
    counter = models.IntegerField(
        default=0,
        verbose_name="Counter",
        help_text="The number of times the tag has been scanned."
    )
    user = models.ForeignKey(
        'accounts.User',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
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

    def reset_to_default(self):
        """
        Resets the link to its default settings.
        """
        self.active = False
        self.user = None
        self.save()

    def get_absolute_url(self):
        """
        Returns the absolute URL for the Link instance.
        
        This URL is unique for each Link and can be used to access specific resources or views related to the Link.

        Returns:
            str: The absolute URL for the Link instance.
        """
        return reverse('inventory:linking', kwargs={'serial_number': self.serial_number})

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
