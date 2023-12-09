from django.db import models
from django.contrib.auth import get_user_model
from apps.core.models import Digit
from apps.inventory.models import Group
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
        user (ForeignKey): A relationship to the User model, representing the user who created or is managing the link.
        digit (OneToOneField): A relationship to the Digit model, representing the digitized plant associated with this link.
        group (ForeignKey): A relationship to the Group model.
    """

    serial_number = models.CharField(
        max_length=255,
        unique=True,
        db_index=True,
        verbose_name="Tag Serial Number",
        help_text="The unique serial number associated with the NFC tag or identification mechanism."
    )
    active = models.BooleanField(
        default=False,
        verbose_name="Active",
        help_text="Indicates whether the link is currently active and mapped to a digital object."
    )
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        help_text='The user who created and owns the link.',
        related_name='links'
    )
    digit = models.OneToOneField(
        Digit,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='link',
        help_text="The digitized plant associated with this NFC tag."
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='links',
        help_text="The group to which this link belongs."
    )

    def get_digit_url(self):
        """
        Returns the URL for the digit view of the associated.

        Returns:
            str: URL for the digit view of the associated Digit.
        """
        return reverse('core:digit', kwargs={'pk': self.digit.pk})

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
