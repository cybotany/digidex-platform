from django.db import models
from digidex.taxonomy.utils.constants import REFERENCE_CHOICES

class VernacularReferences(models.Model):
    """
    Provides a link between occurrences of Vernaculars and references (Publications, Experts,
    Other_Sources), connecting vernacular names to their evidentiary sources.

    Attributes:
        tsn (ForeignKey): The Taxonomic Serial Number (TSN) of the taxonomic unit. Links to a 'Unit' model.
        vernacular_id (IntegerField): Unique identifier for the vernacular name entry.
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
    vernacular_id = models.IntegerField(
        'taxonomy.Vernacular',
        on_delete=models.CASCADE,
        help_text="Unique identifier for the vernacular name entry."
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

    class Meta:
        unique_together = ('tsn', 'vernacular', 'reference_prefix', 'reference_id')
        verbose_name = "Vernacular Reference"
        verbose_name_plural = "Vernacular References"
