from django.db import models
from django.urls import reverse


class Longnames(models.Model):
    """
    A support table that provides a full scientific name without taxon author for Taxonomic
    Units.

    Attributes:
        tsn (int): Taxonomic Serial Number. The unique identifier for an occurrence of Taxonomic Units.
        completename (str): The unit indicators and unit name fields concatenated and trimmed to present entire scientific name, without taxon author. Designed to be helpful when searching for taxa by scientific name.
    """

    tsn = models.IntegerField(
        verbose_name="Taxonomic Serial Number",
        help_text="The unique identifier for an occurrence of Taxonomic Units."
    )
    completename = models.CharField(
        max_length=164,
        verbose_name="Complete Name",
        help_text="The unit indicators and unit name fields concatenated and trimmed to present entire scientific name, without taxon author."
    )

    def __str__(self):
        """
        Returns a string representation of the Longnames.

        Returns:
            str: A string representation of the Longnames.
        """
        return self.completename

    def get_absolute_url(self):
        """
        Get the URL to view the details of this Longnames.

        Returns:
            str: The URL to view the details of this Longnames.
        """
        return reverse('app_name:longname_detail', args=[str(self.id)])
