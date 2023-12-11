from django.db import models
from django.urls import reverse
from apps.taxonomy.models import Unit


class Digit(models.Model):
    """
    Represents a digitized version of a plant, linking it to both the inventory system and taxonomic data.

    The Digit model serves as a bridge between physical plant specimens and their digital representations. 
    It directly associates a plant specimen with its corresponding taxonomic classification.

    Attributes:
        name (CharField): A human-readable name for the digitized plant.
        description (TextField): A short description of the digitized plant.
        taxonomic_unit (ForeignKey): A relationship to the Unit model, representing the plant's taxonomic classification.
    """

    name = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        help_text="A human-readable name for the digitized plant."
    )
    description = models.TextField(
        max_length=500,
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
        return reverse('core:digit', args=[str(self.id)])

    class Meta:
        verbose_name = "Digit"
        verbose_name_plural = "Digits"
