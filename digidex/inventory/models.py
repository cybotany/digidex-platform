import uuid
from django.db import models, transaction


class Digit(models.Model):
    """
    Abstract base model for digitized entities, serving as a bridge between physical specimens and their digital representations.

    Attributes:
        uuid (UUIDField): The unique identifier associated with each Digit.
        name (CharField): A human-readable name for the digitized entity.
        description (TextField): A short description of the digitized entity.
        ntag (OneToOneField): A relationship to the Link model, representing the NTAG link for the digitized entity.
        is_public (BooleanField): Indicates if the digit should be publicly visible to the public or private. Digit is private by default.
        is_archived (BooleanField): Indicates whether the digit is archived.
        created_at (DateTimeField): The date and time when the Digit instance was created.
        last_modified (DateTimeField): The date and time when the Digit instance was last modified.
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
        help_text="A human-readable name for the digitized entity."
    )
    description = models.TextField(
        max_length=500,
        null=True,
        blank=True,
        help_text="A short description of the digitized entity."
    )
    ntag = models.OneToOneField(
        'nfc.NearFieldCommunicationTag',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='%(class)s',
        help_text="NTAG link for the digitized entity."
    )
    is_public = models.BooleanField(
        default=False,
        help_text='Indicates if the digit should be publicly visible to the public or private. Digit is private by default.'
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
        if self.ntag:
            self.ntag.reset_to_default()
            self.ntag.save()
        super(Digit, self).delete(*args, **kwargs)

    class Meta:
        abstract = True
        ordering = ['-created_at']
        