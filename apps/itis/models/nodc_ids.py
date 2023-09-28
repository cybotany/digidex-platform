from django.db import models
from django.urls import reverse


class NODC_IDs(models.Model):
    """
    A mechanism for maintaining the association between the NODC data applications and
    the ITIS database to support users’ needs.

    Attributes:
        nodc_id (str): An identifier previously assigned to an occurrence of Taxonomic Units by the National Oceanographic Data Center.
        update_date (datetime): The date on which a record is modified. The purpose of this element is to provide assistance to those downloading data on a periodic basis.
        tsn (int): Taxonomic Serial Number. The unique identifier for an occurrence of Taxonomic Units.
    """

    nodc_id = models.CharField(
        max_length=12,
        primary_key=True,
        verbose_name="NODC ID"
    )
    update_date = models.DateTimeField(
        auto_now=True,
        verbose_name="Update Date"
    )
    tsn = models.IntegerField(
        null=False,
        blank=False,
        verbose_name="Taxonomic Serial Number"
    )

    def __str__(self):
        """
        Returns a string representation of the NODC ID, using its identifier.

        Returns:
            str: A string representation of the NODC ID.
        """
        return self.nodc_id

    def get_absolute_url(self):
        """
        Get the URL to view the details of this NODC ID.

        Returns:
            str: The URL to view the details of this NODC ID.
        """
        return reverse('taxonomy:describe_nodc_id', args=[str(self.nodc_id)])
