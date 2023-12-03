from django.db import models
from django.contrib.auth import get_user_model
from apps.inventory.models import Link, Group
from apps.taxonomy.models import Unit

class Digit(models.Model):
    """
    Represents a digitized version of a plant, linking it to both the inventory system and taxonomic data.

    The Digit model serves as a bridge between physical plant specimens and their digital representations. 
    It directly associates a plant specimen with a unique identifier (NFC tag), its grouping, and its corresponding taxonomic classification.

    Attributes:
        name (CharField): A human-readable name for the digitized plant.
        description (CharField): A brief description of the digitized plant.
        group (ForeignKey): A relationship to the Group model, representing the grouping of the digitized plant.
        link (OneToOneField): A relationship to the Link model, representing the NFC tag associated with the plant.
        taxonomic_unit (ForeignKey): A relationship to the Unit model, representing the plant's taxonomic classification.
        user (ForeignKey): The user who created the digitized plant record.
        created_at (DateTimeField): The date and time when the digitized plant record was created.
    """
    name = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        help_text="A human-readable name for the digitized plant."
    )
    description = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        help_text="A brief description of the digitized plant."
    )
    group = models.ForeignKey(
        Group,
        null=True,
        on_delete=models.CASCADE,
        related_name='digits',
        help_text="The group to which the digitized plant belongs."
    )
    link = models.OneToOneField(
        Link,
        on_delete=models.CASCADE,
        related_name='digit',
        help_text="The NFC tag link associated with the digitized plant."
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
        verbose_name="User",
        help_text="The user who created the digitized plant record."
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Created At",
        help_text="The date and time when the digitized plant record was created."
    )

    def __str__(self):
        """
        Returns a string representation of the Digit instance.

        The string representation includes the name of the digitized plant.

        Returns:
            str: String representation of the Digit instance.
        """
        return self.name

    class Meta:
        verbose_name = "Digit"
        verbose_name_plural = "Digits"
