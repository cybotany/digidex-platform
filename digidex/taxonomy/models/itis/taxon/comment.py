from django.db import models

class ItisTaxonComment(models.Model):
    """
    An intersection table for establishing a many-to-many relationship between
    Taxonomic Units and associated Comments. This model links Taxonomic Units
    (via TSN) to Comments, allowing for the association of remarks with specific
    taxonomic occurrences.

    Attributes:
        tsn (ForeignKey): The Taxonomic Serial Number (TSN) of the taxonomic unit.
        comment (ForeignKey): Unique identifier for the associated Comment.
        last_modified (DateTimeField): The date and time the record was last updated.
    """
    tsn = models.ForeignKey(
        'taxonomy.Taxon',
        on_delete=models.CASCADE,
        db_column="tsn",
        help_text="Taxonomic Serial Number (TSN) for the Taxonomic Unit."
    )
    comment = models.ForeignKey(
        'taxonomy.Comment',
        on_delete=models.CASCADE,
        help_text="Unique identifier for the associated Comment."
    )
    last_modified = models.DateTimeField(
        help_text="The date and time the record was last updated."
    )

    class Meta:
        unique_together = ('tsn', 'comment')
        verbose_name = "Taxon Comments"
        verbose_name_plural = "Taxon Comments"

    def __str__(self):
        return f"TSN {self.tsn} - Comment {self.comment}"
