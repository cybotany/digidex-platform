from django.conf import settings
from django.db import models
from django.urls import reverse

class NFC(models.Model):
    """
    Abstract base class for NFC (Near Field Communication) technology, providing common attributes.

    Attributes:
        serial_number (CharField): The unique serial number associated with the NFC tag.
        eeprom (BinaryField): The EEPROM data associated with the NFC tag.
        counter (PositiveIntegerField): The counter value associated with the NFC tag.
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
    eeprom = models.BinaryField(
        null=True,
        blank=True,
        verbose_name="EEPROM",
        help_text="The EEPROM data associated with the NFC tag."
    )
    counter = models.PositiveIntegerField(
        default=0,
        verbose_name="Counter",
        help_text="The counter value associated with the NFC tag."
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
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

    def activate_link(self, user):
        """
        Activates the link, associating it with a user and setting it as active.
        """
        self.user = user
        self.active = True
        self.save()

    def deactivate_link(self):
        """
        Deactivates the link, making it inactive.
        """
        self.active = False
        self.save()

    def check_access(self, user):
        """
        Checks if a user has access to the link.
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

    class Meta:
        abstract = True
