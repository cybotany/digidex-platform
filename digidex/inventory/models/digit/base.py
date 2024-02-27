import uuid
from urllib.parse import urlencode
from django.urls import reverse
from django.db import models, transaction
from ..grouping import Grouping

class BaseDigit(models.Model):
    """
    Abstract base model for digitized entities, serving as a bridge between physical specimens and their digital representations.

    Attributes:
        uuid (UUIDField): The unique identifier associated with each Digit.
        name (CharField): A human-readable name for the digitized entity.
        description (TextField): A short description of the digitized entity.
        grouping (ForeignKey): The grouping this digit belongs to.
        taxon (ForeignKey): A relationship to the Unit model, representing the entity's taxonomic classification.
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
    grouping = models.ForeignKey(
        'inventory.Grouping',
        on_delete=models.CASCADE,
        related_name="%(class)ss", # The second "s" at the end is intentional
        help_text="The grouping this digit belongs to."
    )
    taxon = models.ForeignKey(
        'taxonomy.Unit',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="%(class)ss", # The second "s" at the end is intentional
        help_text="The taxonomic classification of the digitized entity."
    )
    ntag = models.OneToOneField(
        'link.NTAG',
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

        super(BaseDigit, self).delete(*args, **kwargs)

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
        if not self.grouping_id:
            default_grouping, _ = Grouping.objects.get_or_create(
                user=self.ntag.user,
                is_default=True,
                defaults={
                    'name': 'Default Grouping',
                    'description': 'This is an automatically created default grouping.'
                }
            )
            self.grouping = default_grouping
        
        if not self.name and self.ntag:
            user_digit_count = BaseDigit.objects.filter(
                ntag__user=self.ntag.user,
                ntag__use=self.ntag.use_category()
            ).count()

            default_name_prefix = self.ntag.use_category()
            self.name = f"{default_name_prefix} {user_digit_count + 1}"

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """
        Get the URL to view the details of this digitized entity, using query parameters.
        """
        digit_type = self.ntag.use_category()
        return reverse('inventory:detail-digit', kwargs={'type': digit_type, 'uuid': self.uuid})

    class Meta:
        abstract = True
        ordering = ['-created_at']
        