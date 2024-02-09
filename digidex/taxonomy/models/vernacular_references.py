from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from digidex.taxonomy.utils.constants import REFERENCE_CHOICES

class VernacularReferences(models.Model):
    """
    Provides a link between occurrences of Vernaculars and references (Publications, Experts,
    Other_Sources), connecting vernacular names to their evidentiary sources.

    Attributes:
        tsn (ForeignKey): The Taxonomic Serial Number (TSN) of the taxonomic unit. Links to a 'Unit' model.
        vernacular (ForeignKey): Unique identifier for the vernacular name entry.
        reference_prefix (CharField): Prefix indicating the type of reference associated with the vernacular.
        reference_id (IntegerField): Identifier for the specific reference providing evidence for the vernacular.
        last_modified (DateTimeField): Date and time when the record was last modified.
    """
    tsn = models.ForeignKey(
        'taxonomy.Unit',
        on_delete=models.CASCADE,
        db_column="tsn",
        help_text="Taxonomic Serial Number (TSN) for the Taxonomic Unit."
    )
    vernacular = models.ForeignKey(
        'taxonomy.Vernacular',
        on_delete=models.CASCADE,
        help_text="Unique identifier for the vernacular name entry."
    )
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        null=True,
        help_text="Expert, Publication, or Other Source model used as a reference."
    )
    object_id = models.PositiveIntegerField(
        null=True,
        help_text="Primary key of the referenced model."
    )
    content_object = GenericForeignKey(
        'content_type',
        'object_id'
    )
    reference_prefix = models.CharField(
        max_length=3, 
        choices=REFERENCE_CHOICES,
        help_text="Prefix indicating the type of reference associated with the vernacular."
    )
    reference_id = models.IntegerField(
        help_text="Identifier for the specific reference providing evidence for the vernacular."
    )
    last_modified = models.DateTimeField(
        help_text="Date and time when the record was last modified."
    )

    def __str__(self):
        return f"Vernacular ID: {self.vernacular} - TSN: {self.tsn}, Doc: {self.reference_prefix}{self.reference_id}"

    def save(self, *args, **kwargs):
        if not self.content_type:
            model_map = {'EXP': 'Expert', 'PUB': 'Publication', 'SRC': 'Source'}
            model_class = model_map.get(self.reference_prefix)
            if model_class:
                self.content_type = ContentType.objects.get(model=model_class.lower())
        super(VernacularReferences, self).save(*args, **kwargs)

    class Meta:
        unique_together = ('tsn', 'vernacular', 'reference_prefix', 'reference_id')
        verbose_name = "Vernacular Reference"
        verbose_name_plural = "Vernacular References"
