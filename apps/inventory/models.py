from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from apps.taxonomy.models import Unit
from apps.nfc.models import Link


class Digit(models.Model):
    """
    Represents a digitized version of a plant, linking it to both the inventory system and taxonomic data.

    The Digit model serves as a bridge between physical plant specimens and their digital representations. 
    It directly associates a plant specimen with its corresponding taxonomic classification.

    Attributes:
        name (CharField): A human-readable name for the digitized plant.
        description (TextField): A short description of the digitized plant.
        taxonomic_unit (ForeignKey): A relationship to the Unit model, representing the plant's taxonomic classification.
        user (ForeignKey): The user who created the journal entry, linked to the user model.
        nfc_link (OneToOneField): A relationship to the Link model, representing the NFC link for the digitized plant.
        created_at (DateTimeField): The date and time when the Digit instance was created.
        last_modified (DateTimeField): The date and time when the Digit instance was last modified.
    """

    name = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        help_text="A human-readable name for the digitized plant."
    )
    description = models.TextField(
        max_length=500,
        null=True,
        blank=True,
        help_text="A short description of the digitized plant."
    )
    taxonomic_unit = models.ForeignKey(
        Unit,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='digits',
        help_text="The taxonomic classification of the digitized plant."
    )
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="User",
        help_text="The owner of the digitized plant."
    )
    nfc_link = models.OneToOneField(
        Link,
        on_delete=models.CASCADE,
        related_name='digit',
        null=True,
        blank=True,
        help_text="NFC link for the digitized plant."
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Created At",
        help_text="The date and time when the digit instance was created."
    )
    last_modified = models.DateTimeField(
        auto_now=True,
        verbose_name="Last Modified",
        help_text="The date and time when the digit instance was last modified."
    )

    def __str__(self):
        """
        Returns a string representation of the Digit instance.

        The string representation includes the name of the digitized plant.

        Returns:
            str: String representation of the Digit instance.
        """
        return self.name

    def get_absolute_url(self):
        """
        Get the URL to view the details of this digit.

        Returns:
            str: The URL to view the details of this digit.
        """
        return reverse('inventory:details', args=[str(self.id)])

    class Meta:
        verbose_name = "Digit"
        verbose_name_plural = "Digits"
