from django.db import models
from digidex.taxonomy.models.itis.taxon import reference as itis_reference

class ItisTaxonVernacularReference(itis_reference.ItisTaxonReference):
    """
    Provides a link between occurrences of Vernaculars and references (Publications, Experts,
    Other_Sources), connecting vernacular names to their evidentiary sources.

    Attributes:
        vernacular (ForeignKey): Unique identifier for the vernacular name entry.
        content_type (ForeignKey): Prefix indicating the type of reference associated with the vernacular.
        object_id (PositiveIntegerField): Identifier for the specific reference providing evidence for the vernacular.
        last_modified (DateTimeField): Date and time when the record was last modified.
    """
    vernacular = models.ForeignKey(
        'taxonomy.ItisTaxonVernacular',
        on_delete=models.CASCADE,
        help_text="Unique identifier for the vernacular name entry."
    )

    def __str__(self):
        return f"Vernacular ID: {self.vernacular}, Doc: {self.content_type}{self.object_id}"

    class Meta:
        unique_together = ('vernacular', 'content_type', 'object_id')
        verbose_name = "Vernacular Reference"
        verbose_name_plural = "Vernacular References"
