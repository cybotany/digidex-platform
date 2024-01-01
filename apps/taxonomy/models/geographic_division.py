from django.db import models


class GeographicDivision(models.Model):
    """
    Represents the geographic division of a taxonomic unit.

    Attributes:
        tsn (IntegerField): The taxonomic serial number.
        geographic_value (str): The geographic value.
        update_date (datetime): The date and time when the geographic value was added.
    """
    tsn = models.IntegerField(
        null=True,
        blank=True
    )
    geographic_value = models.CharField(
        max_length=200,
        null=True,
        blank=True
    )
    update_date = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        """
        Returns a string representation of the division, using its geographic value.
        """
        return self.geographic_value
