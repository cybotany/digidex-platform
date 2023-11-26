from django.db import models
from django.urls import reverse


class Rank(models.Model):
    """
    Defines the levels associated with the taxonomic hierarchical structure and establishes the
    rank order for an occurrence of the Taxonomic Units.

    Attributes:
        kingdom (ForeignKey): A reference to the Kingdom model.
        rank_id (int): A unique identifier for a specific rank within the taxonomic hierarchy.
        rank_name (str): The label associated with the specific rank of a taxonomic hierarchy.
        direct_parent_rank (ForeignKey): A reference to another Rank which is the direct parent rank.
        required_parent_rank (ForeignKey): A reference to another Rank which is the required parent rank.
        update_date (datetime): The date on which a record is modified.
    """

    kingdom = models.ForeignKey(
        'Kingdom',
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        verbose_name="Kingdom",
        db_column='kingdom_id'
    )
    rank_id = models.SmallIntegerField(
        null=False,
        blank=False,
        verbose_name="Rank ID"
    )
    rank_name = models.CharField(
        max_length=15,
        null=False,
        blank=False,
        verbose_name="Rank Name"
    )
    direct_parent_rank_id = models.IntegerField(
        null=True,
        blank=True,
        verbose_name="Direct Parent Rank",
    )
    required_parent_rank_id = models.IntegerField(
        null=True,
        blank=True,
        verbose_name="Required Parent Rank",
    )
    update_date = models.DateTimeField(
        auto_now=True,
        verbose_name="Update Date"
    )

    class Meta:
        unique_together = (('kingdom', 'rank'))

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
