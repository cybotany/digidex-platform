from django.db import models
from django.urls import reverse
from apps.utils.constants import KINGDOM_CHOICES


class TaxonAuthorsLKUP(models.Model):
    """
    Reference to authors of taxa for all kingdoms.

    Attributes:
        taxon_author_id (int): A unique identifier for the author(s) of a taxonomic name.
        taxon_author (str): The author(s) associated with the name of a taxon.
        update_date (datetime): The date on which a record is modified. The purpose of this element is to provide assistance to those downloading data on a periodic basis.
        kingdom_id (int): A unique identifier for the highest level of the taxonomic hierarchy structure.
        short_author (str): The author(s) associated with the name of a taxon with parenthesis, commas and periods removed. Designed to be helpful when searching for an author whose name contains a different punctuation for different taxon names.
    """

    taxon_author_id = models.AutoField(
        primary_key=True,
        verbose_name="Taxon Author ID"
    )
    taxon_author = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        verbose_name="Taxon Author"
    )
    update_date = models.DateTimeField(
        auto_now=True,
        verbose_name="Update Date"
    )
    kingdom_id = models.IntegerField(
        choices=KINGDOM_CHOICES,
        null=False,
        blank=False,
        verbose_name="Kingdom ID"
    )
    short_author = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name="Short Author"
    )

    def __str__(self):
        """
        Returns a string representation of the taxon author, using its name.

        Returns:
            str: A string representation of the taxon author.
        """
        return self.taxon_author

    def get_absolute_url(self):
        """
        Get the URL to view the details of this taxon author.

        Returns:
            str: The URL to view the details of this taxon author.
        """
        return reverse('taxonomy:describe_taxon_author', args=[str(self.taxon_author_id)])
