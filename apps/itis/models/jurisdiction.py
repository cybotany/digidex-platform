from django.db import models
from django.urls import reverse
from apps.utils.constants import ORIGIN_CHOICES


class Jurisdiction(models.Model):
    """
    Association of a referenced occurrence of Taxonomic Units with one or more US
    jurisdictional units. Also provides an identification of whether the taxon was native
    and/or introduced to the unit.

    Attributes:
        tsn (int): Taxonomic Serial Number. The unique identifier for an occurrence of Taxonomic Units.
        jurisdiction_value (str): Label signifying a US jurisdictional unit as defined by the TWG, and Canada.
        origin (str): Indication of whether an occurrence of Taxonomic Units is native and/or introduced to a US jurisdictional unit.
        update_date (datetime): The date on which a record is modified. The purpose of this element is to provide assistance to those downloading data on a periodic basis.
    """

    tsn = models.IntegerField(
        verbose_name="Taxonomic Serial Number"
    )
    jurisdiction_value = models.CharField(
        max_length=30,
        null=False,
        blank=False,
        verbose_name="Jurisdiction Value"
    )
    origin = models.CharField(
        max_length=19,
        choices=ORIGIN_CHOICES,
        null=True,
        blank=True,
        verbose_name="Origin"
    )
    update_date = models.DateTimeField(
        auto_now=True,
        verbose_name="Update Date"
    )

    class Meta:
        unique_together = ('tsn', 'jurisdiction_value')

    def __str__(self):
        """
        Returns a string representation of the jurisdiction, using its value.

        Returns:
            str: A string representation of the jurisdiction.
        """
        return self.jurisdiction_value

    def get_absolute_url(self):
        """
        Get the URL to view the details of this jurisdiction.

        Returns:
            str: The URL to view the details of this jurisdiction.
        """
        return reverse('taxonomy:describe_jurisdiction', args=[str(self.tsn)])
