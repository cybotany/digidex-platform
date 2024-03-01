from django.db import models

class Geography(models.Model):
    """
    Represents the geographic division of a taxonomic unit.

    Attributes:
        tsn (ForeignKey): The taxonomic serial number.
        geography_value (CharField): The geographic value.
        last_modified (DateTimeField): The date and time the record was last updated.
    """
    tsn = models.ForeignKey(
        'taxonomy.Unit',
        on_delete=models.CASCADE,
        verbose_name="Taxonomic Serial Number",
        db_column="tsn",
        help_text="Taxonomic Serial Number (TSN) for the Taxonomic Unit."
    )
    geography_value = models.CharField(
        max_length=200,
        verbose_name="Geographic Value",
        help_text="The geographic value."
    )
    last_modified = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name="Last Modified",
        help_text="The date and time the record was last updated."
    )

    def __str__(self):
        """
        Returns a string representation of the division, using its geographic value.
        """
        return self.geography_value

    class Meta:
        unique_together = ('tsn', 'geography_value')
        verbose_name = "Geographic Division"
        verbose_name_plural = "Geographic Divisions"
