from django.db import models
from digidex.taxonomy.utils.constants import BINARY_CHOICE

class Vernacular(models.Model):
    """
    Stores common names associated with Taxonomic Units, facilitating the inclusion of
    vernacular names in multiple languages and tracking their approval status.

    Attributes:
        - tsn (ForeignKey): The Taxonomic Serial Number (TSN) of the taxonomic unit. Links to a 'Unit' model.
        - id (IntegerField): Unique identifier for the vernacular name entry.
        - vernacular_name (CharField): Common name associated with the taxonomic unit.
        - language (CharField): Language of the vernacular name.
        - approved_ind (CharField): Indicator of whether the vernacular name is approved.
        - last_modified (DateTimeField): Date and time when the record was last updated.
    """
    tsn = models.ForeignKey(
        'taxonomy.Unit',
        on_delete=models.CASCADE,
        db_column="tsn",
        help_text="Taxonomic Serial Number (TSN) for the Taxonomic Unit."
    )
    id = models.IntegerField(
        primary_key=True,
        help_text="Unique identifier for a vernacular name entry."
    )
    vernacular_name = models.CharField(
        max_length=80, 
        help_text="Common name associated with the taxonomic unit."
    )
    language = models.CharField(
        max_length=15, 
        help_text="Language of the vernacular name."
    )
    approved_ind = models.CharField(
        max_length=1, 
        blank=True, 
        null=True, 
        choices=BINARY_CHOICE,
        help_text="Indicator of whether the vernacular name is approved."
    )
    last_modified = models.DateTimeField(
        help_text="Date and time when the record was last updated."
    )

    def __str__(self):
        return f"{self.vernacular_name} ({self.language}) - TSN: {self.tsn}"

    class Meta:
        unique_together = ('tsn', 'vernacular_id')
        verbose_name = "Vernacular Name"
        verbose_name_plural = "Vernacular Names"
