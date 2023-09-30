from django.db import models
from django.urls import reverse
from apps.utils.constants import KINGDOM_CHOICES


class TaxonUnitTypes(models.Model):
    """
    Defines the levels associated with the taxonomic hierarchical structure and establishes the
    rank order for an occurrence of the Taxonomic Units.

    Attributes:
        kingdom_id (int): A unique identifier for the highest level of the taxonomic hierarchy structure.
        rank_id (int): A unique identifier for a specific level within the taxonomic hierarchy.
        rank_name (str): The label associated with the specific level of a taxonomic hierarchy.
        direct_parent_rank_id (int): The taxonomic serial number for the direct parent of the subject occurrence of Taxonomic Units.
        required_parent_rank_id (int): A unique identifier for a specific level within the taxonomic hierarchy.
        update_date (datetime): The date on which a record is modified. The purpose of this element is to provide assistance to those downloading data on a periodic basis.
    """

    kingdom_id = models.IntegerField(
        choices=KINGDOM_CHOICES,
        null=False,
        blank=False,
        verbose_name="Kingdom ID"
    )
    rank_id = models.SmallIntegerField(
        verbose_name="Rank ID"
    )
    rank_name = models.CharField(
        max_length=15,
        null=False,
        blank=False,
        verbose_name="Rank Name"
    )
    direct_parent_rank_id = models.SmallIntegerField(
        null=True,
        blank=True,
        verbose_name="Direct Parent Rank ID"
    )
    required_parent_rank_id = models.SmallIntegerField(
        null=True,
        blank=True,
        verbose_name="Required Parent Rank ID"
    )
    update_date = models.DateTimeField(
        auto_now=True,
        verbose_name="Update Date"
    )

    def __str__(self):
        """
        Returns a string representation of the taxon unit type, using its rank name.

        Returns:
            str: A string representation of the taxon unit type.
        """
        return self.rank_name

    def get_absolute_url(self):
        """
        Get the URL to view the details of this taxon unit type.

        Returns:
            str: The URL to view the details of this taxon unit type.
        """
        return reverse('taxonomy:describe_taxon_unit_type', args=[str(self.rank_id)])
