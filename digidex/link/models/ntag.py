from django.db import models
from django.urls import reverse
from .nfc import NFC

class NTAG(NFC):
    """
    Model representing NTAGs, a specific implementation of NFC tags.
    Inherits common attributes from NFC and can include NTAG-specific fields and methods.
    """
    NTAG213 = 213
    NTAG215 = 215
    NTAG216 = 216
    NTAG_TYPES = [
        (NTAG213, 'NTAG213'),
        (NTAG215, 'NTAG215'),
        (NTAG216, 'NTAG216'),
    ]
    ntag_type = models.CharField(
        max_length=8,
        blank=True,
        choices=NTAG_TYPES, 
        verbose_name="NTAG Type",
        help_text="The type of the NTAG."
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
        Returns the absolute URL for the NTAG instance.
        
        This URL is unique for each NTAG link and can be used to access specific resources or views related to it.

        Returns:
            str: The absolute URL for the NTAG instance.
        """
        return reverse('link:digit', kwargs={'serial_number': self.serial_number})

    def __str__(self):
        """
        Returns a string representation of the NTAG instance, primarily based on its unique serial number.
        """
        return f"{self.ntag_type} - {self.serial_number}"

    class Meta:
        verbose_name = "NTAG"
        verbose_name_plural = "NTAGs"
