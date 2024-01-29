import uuid
from django.db import models, transaction
from django.urls import reverse
from digidex.journal.models import Collection


class Digit(models.Model):
    """
    Represents a digitized version of a plant, linking it to both the inventory system and taxonomic data.

    The Digit model serves as a bridge between physical plant specimens and their digital representations. 
    It directly associates a plant specimen with its corresponding taxonomic classification.

    Attributes:
        uuid (UUIDField): The unique identifier associated with the NFC tag.
        name (CharField): A human-readable name for the digitized plant.
        description (TextField): A short description of the digitized plant.
        taxonomic_unit (ForeignKey): A relationship to the Unit model, representing the plant's taxonomic classification.
        nfc_link (OneToOneField): A relationship to the Link model, representing the NFC link for the digitized plant.
        journal_collection (OneToOneField): A relationship to the Collection model, representing the entire journal collection link for the digitized plant.
        created_at (DateTimeField): The date and time when the Digit instance was created.
        last_modified (DateTimeField): The date and time when the Digit instance was last modified.
    """

    uuid = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False,
        db_index=True,
        verbose_name="Digit UUID",
        help_text="The unique identifier associated with the NFC tag or identification mechanism."
    )
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
        'link.NFC',
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
    is_archived = models.BooleanField(
        default=False,
        verbose_name="Archived",
        help_text="Indicates whether the digit is archived."
    )

    @classmethod
    def create_digit(cls, form_data, link, user):
        with transaction.atomic():
            digit = cls.objects.create(
                nfc_link=link,
                journal_collection=Collection.objects.create(),
                **form_data
            )
            link.user = user
            link.active = True
            link.save()

            return digit

    def archive(self):
        """
        Archives the digit instance. This involves marking it as archived and dissociating
        its NFC link so that the link can be reused for a new digit.
        """
        self.nfc_link = None
        self.is_archived = True
        self.save()

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
        return reverse('inventory:details', kwargs={'uuid': self.nfc_link.uuid})

    class Meta:
        verbose_name = "Digit"
        verbose_name_plural = "Digits"
