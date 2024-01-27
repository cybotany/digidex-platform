import uuid
from django.db import models
from django.urls import reverse


class Digit(models.Model):
    """
    Represents a digitized version of a plant, linking it to both the inventory system and taxonomic data.

    The Digit model serves as a bridge between physical plant specimens and their digital representations. 
    It directly associates a plant specimen with its corresponding taxonomic classification.

    Attributes:
        name (CharField): A human-readable name for the digitized plant.
        description (TextField): A short description of the digitized plant.
        taxonomic_unit (ForeignKey): A relationship to the Unit model, representing the plant's taxonomic classification.
        nfc_link (OneToOneField): A relationship to the Link model, representing the NFC link for the digitized plant.
        journal_collection (OneToOneField): A relationship to the Link model, representing the NFC link for the digitized plant.
        uuid (UUIDField): The unique identifier associated with the NFC tag or identification mechanism.
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
        'taxonomy.Unit',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='digits',
        help_text="The taxonomic classification of the digitized plant."
    )
    nfc_link = models.OneToOneField(
        'Link',
        on_delete=models.CASCADE,
        related_name='digit',
        help_text="NFC link for the digitized plant."
    )
    journal_collection = models.OneToOneField(
        'journal.Collection',
        on_delete=models.CASCADE,
        related_name='digit',
        help_text="The journal for the digitized plant."
    )
    uuid = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        db_index=True,
        verbose_name="Digit UUID",
        help_text="The unique identifier associated with the NFC tag or identification mechanism."
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

    def save(self, *args, **kwargs):
        """
        Overrides the save method of the model. If name is not provided, it sets a default name 
        based on the count of Digits the user has.
        """
        if not self.name:
            user_digit_count = Digit.objects.filter(nfc_link__user=self.nfc_link.user).count()
            self.name = f'Digit {user_digit_count + 1}'

        super().save(*args, **kwargs)

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
        return reverse('inventory:details', kwargs={'digit_uuid': self.uuid})

    class Meta:
        verbose_name = "Digit"
        verbose_name_plural = "Digits"
