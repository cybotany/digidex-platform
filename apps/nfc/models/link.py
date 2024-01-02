from django.db import models


class Link(models.Model):
    """
    The Link model is primarily used to connect physical objects (like plants) that have been digitized
    (through an NFC tag or similar technology) to their digital representations and metadata in the system.
    Each link is uniquely identified by a uid for easy access.

    Attributes:
        uid (CharField): The unique identifier or serial number of the Link, typically associated with
                                   the physical NFC tag or other identification mechanism.
        active (BooleanField): A flag indicating whether the Link is active and mapped to a digital object. Inactive
                               links may represent unused or deactivated tags.
        counter (IntegerField): The numerical counter value associated with the NFC tag. This value is
                                automatically triggered at each read command.

    """

    uid = models.CharField(
        max_length=255,
        unique=True,
        db_index=True,
        verbose_name="Tag UID",
        help_text="The unique identifier associated with the NFC tag or identification mechanism."
    )
    active = models.BooleanField(
        default=False,
        verbose_name="Active",
        help_text="Indicates whether the link is currently active and mapped to a digital object."
    )
    counter = models.IntegerField(
        default=0,
        verbose_name="Counter Value",
        help_text="The numerical counter value associated with the NFC tag."
    )

    def __str__(self):
        """
        Returns a string representation of the Link instance.

        This representation is primarily based on the unique serial number of the Link.

        Returns:
            str: The serial number of the Link, representing its unique identification.
        """
        return self.uid

    class Meta:
        verbose_name = "Link"
        verbose_name_plural = "Links"
