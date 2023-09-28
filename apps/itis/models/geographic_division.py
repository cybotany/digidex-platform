from django.db import models
from django.urls import reverse


class GeographicDivision(models.Model):
    """
    Geographic association for the referenced occurrence in Taxonomic Units.

    Attributes:
        tsn (int): Taxonomic Serial Number. The unique identifier for an occurrence of Taxonomic Units.
        geographic_value (str): Label given to a geographic division as identified by the Taxonomic Work Group.
        update_date (datetime): The date on which a record is modified. The purpose of this element is to provide assistance to those downloading data on a periodic basis.
    """

    tsn = models.IntegerField(
        primary_key=True,
        verbose_name="Taxonomic Serial Number"
    )
    geographic_value = models.CharField(
        max_length=45,
        null=False,
        blank=False,
        verbose_name="Geographic Value"
    )
    update_date = models.DateTimeField(
        auto_now=True,
        verbose_name="Update Date"
    )

    def __str__(self):
        """
        Returns a string representation of the geographic division, using its value.

        Returns:
            str: A string representation of the geographic division.
        """
        return self.geographic_value

    def get_absolute_url(self):
        """
        Get the URL to view the details of this geographic division.

        Returns:
            str: The URL to view the details of this geographic division.
        """
        return reverse('taxonomy:describe_geographic_div', args=[str(self.tsn)])
