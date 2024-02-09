from django.db import models

class UnitSynonyms(models.Model):
    """
    Represents the linkage between an accepted taxonomic name and its alternates or predecessors.
    
    Attributes:
        - tsn (ForeignKey): Taxonomic Serial Number (TSN) for the Taxonomic Unit.
        - tsn_accepted (ForeignKey): Taxonomic Serial Number (TSN) for the accepted taxonomic unit.
        - last_modified (DateTimeField): The date and time the record was last updated.
    """
    tsn = models.ForeignKey(
        'taxonomy.Unit',
        on_delete=models.CASCADE,
        db_column="tsn",
        related_name='synonyms',
        help_text="Taxonomic Serial Number (TSN) for the Taxonomic Unit."
    )
    tsn_accepted = models.ForeignKey(
        'taxonomy.Unit',
        on_delete=models.CASCADE,
        db_column='tsn_accepted',
        related_name='accepted_for',
        help_text="Taxonomic Serial Number for the accepted Taxonomic Unit."
    )
    last_modified = models.DateTimeField(
        help_text="The date and time the record was last updated."
    )

    def __str__(self):
        return f"Synonym TSN: {self.tsn} -> Accepted TSN: {self.tsn_accepted}"

    class Meta:
        unique_together = ('tsn', 'tsn_accepted')
        verbose_name = "Unit Synonym"
        verbose_name_plural = "Unit Synonyms"
