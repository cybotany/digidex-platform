from django.db import models
from django.urls import reverse


class NFC(models.Model):
    """
    The NFC (Near Field Communication) model is primarily used to connect physical objects (like plants) that have been digitized
    through an NTAG213 to their digital representations and metadata in the system.

    Attributes:
        serial_number (CharField): The unique serial number associated with the NFC tag.
        counter (IntegerField): The number of times the tag has been scanned.
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

    def increment_counter(self):
        self.counter += 1
        self.save()

    def activate_link(self, user):
        self.user = user
        self.active = True
        self.save()

    def deactivate_link(self):
        self.active = False
        self.save()

    def check_access(self, user):
       """
       Checks if user has access to link.
       """
       return self.active and self.user == user

    def reset_to_default(self):
        """
        Resets the link to its default settings.
        """
        self.active = False
        self.user = None
        self.save()

    def get_absolute_url(self):
        """
        Returns the absolute URL for the NFC instance.
        
        This URL is unique for each NFC link and can be used to access specific resources or views related to it.

        Returns:
            str: The absolute URL for the NFC instance.
        """
        return reverse('link:digit', kwargs={'serial_number': self.serial_number})

    def __str__(self):
        """
        Returns a string representation of the NFC instance.

        This representation is primarily based on the unique serial number of the NTAG213.

        Returns:
            str: The serial number of the NTAG213, representing its unique identification.
        """
        return self.serial_number

    def save(self, *args, **kwargs):
        # Here, you can add logic if you need to generate or modify the slug
        # In your case, it's just directly using the serial number
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "NFC Tag"
        verbose_name_plural = "NFC Tags"
