import uuid
from django.db import models, transaction
from django.urls import reverse


class Digit(models.Model):
    """
    Represents a digitized version of a plant, linking it to both the inventory system and taxonomic data.

    The Digit model serves as a bridge between physical plant specimens and their digital representations. 
    It directly associates a plant specimen with its corresponding taxonomic classification.

    Attributes:
        uuid (UUIDField): The unique identifier associated with each Digit.
        name (CharField): A human-readable name for the digitized plant.
        description (TextField): A short description of the digitized plant.
        taxon (ForeignKey): A relationship to the Unit model, representing the plant's taxonomic classification.
        ntag (OneToOneField): A relationship to the Link model, representing the NTAG link for the digitized plant.
        created_at (DateTimeField): The date and time when the Digit instance was created.
        last_modified (DateTimeField): The date and time when the Digit instance was last modified.
        is_archived (BooleanField): Indicates whether the digit is archived.
    """

    uuid = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False,
        db_index=True,
        verbose_name="Digit UUID",
        help_text="The unique identifier associated with the Digit."
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
    taxon = models.ForeignKey(
        'taxonomy.Unit',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='digits',
        help_text="The taxonomic classification of the digitized plant."
    )
    ntag = models.OneToOneField(
        'link.NTAG',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='digit',
        help_text="NTAG link for the digitized plant."
    )
    is_archived = models.BooleanField(
        default=False,
        verbose_name="Archived",
        help_text="Indicates whether the digit is archived."
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

    @classmethod
    def create_digit(cls, form_data, link, user):
        with transaction.atomic():
            digit = cls.objects.create(
                ntag=link,
                **form_data
            )
            link.user = user
            link.active = True
            link.save()

            return digit

    def delete(self, *args, **kwargs):
        """
        Overrides the delete method of the model to include custom deletion logic.
        """
        # Reset the NTAG link to default and save it
        if self.ntag:
            self.ntag.reset_to_default()
            self.ntag.save()

        super(Digit, self).delete(*args, **kwargs)

    def archive(self):
        """
        Archives the digit instance. This involves marking it as archived and dissociating
        its NTAG link so that the link can be reused for a new digit.
        """
        self.ntag = None
        self.is_archived = True
        self.save()

    def save(self, *args, **kwargs):
        """
        Overrides the save method of the model. If name is not provided, it sets a default name 
        based on the count of Digits the user has.
        """
        if not self.name:
            user_digit_count = Digit.objects.filter(ntag__user=self.ntag.user).count()
            self.name = f'Digit {user_digit_count + 1}'

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """
        Get the URL to view the details of this digit.

        Returns:
            str: The URL to view the details of this digit.
        """
        return reverse('inventory:digit-details', kwargs={'uuid': self.uuid})

    class Meta:
        verbose_name = "Digit"
        verbose_name_plural = "Digits"
