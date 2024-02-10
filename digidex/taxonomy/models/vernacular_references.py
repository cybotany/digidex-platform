from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class VernacularReferences(models.Model):
    """
    Provides a link between occurrences of Vernaculars and references (Publications, Experts,
    Other_Sources), connecting vernacular names to their evidentiary sources.

    Attributes:
        tsn (ForeignKey): The Taxonomic Serial Number (TSN) of the taxonomic unit. Links to a 'Unit' model.
        vernacular (ForeignKey): Unique identifier for the vernacular name entry.
        content_type (ForeignKey): Prefix indicating the type of reference associated with the vernacular.
        object_id (PositiveIntegerField): Identifier for the specific reference providing evidence for the vernacular.
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
    last_modified = models.DateTimeField(
        help_text="Date and time when the record was last modified."
    )

    def __str__(self):
        return f"Vernacular ID: {self.vernacular} - TSN: {self.tsn}, Doc: {self.content_type}{self.object_id}"

    class Meta:
        unique_together = ('tsn', 'vernacular', 'content_type', 'object_id')
        verbose_name = "Vernacular Reference"
        verbose_name_plural = "Vernacular References"
