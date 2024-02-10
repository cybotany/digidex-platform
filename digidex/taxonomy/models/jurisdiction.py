from django.db import models


class Jurisdiction(models.Model):
    """
    Represents the association of a of Taxonomic Unit with one or more US
    jurisdictional unit. Also provides an identification of whether the taxon was native
    and/or introduced.

    Attributes:
        tsn (ForeignKey): The taxonomic serial number.
        jurisdiction_value (str): The geographic value.
        origin (str): Indication of whether a Taxonomic Unit is native and/or introduced to a US jurisdictional unit.
        last_modified (datetime): The date and time when the geographic value was added.
    """
    tsn = models.ForeignKey(
        'taxonomy.Unit',
        on_delete=models.CASCADE,
        db_column="tsn",
        help_text="Taxonomic Serial Number (TSN) for the Taxonomic Unit."
    )
    jurisdiction_value = models.CharField(
        max_length=30,
        help_text="Label signifying a US jurisdictional unit as defined by the TWG, and Canada."
    )
    origin = models.CharField(
        max_length=19,
        null=True,
        blank=True,
        help_text="Indication of whether a Taxonomic Unit is native and/or introduced to a US jurisdictional unit."
    )
    last_modified = models.DateTimeField(
        null=True,
        blank=True,
        help_text="The date and time when the geographic value was added."
    )

    def __str__(self):
        """
        Returns a string representation of the division, using its jurisdiction value.
        """
        return self.jurisdiction_value
    
    class Meta:
        unique_together = ('tsn', 'jurisdiction_value')
        verbose_name = "Jurisdiction"
        verbose_name_plural = "Jurisdictions"
