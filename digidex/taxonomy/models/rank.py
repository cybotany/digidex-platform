from django.db import models


class Rank(models.Model):
    """
    Defines the levels associated with the taxonomic hierarchical structure and establishes the
    rank order for an occurrence of the Taxonomic Units.

    Attributes:
        kingdom (ForeignKey): A reference to the Kingdom model.
        rank (int): A unique identifier for a specific rank within the taxonomic kingdom hierarchy.
        rank_name (str): The label associated with the specific rank of a taxonomic kingdom hierarchy.
        direct_parent_rank (ForeignKey): A reference to another Rank which is the direct parent rank.
        required_parent_rank (ForeignKey): A reference to another Rank which is the required parent rank.
        last_modified (datetime): The date on which a record was last modified.
    """
    kingdom = models.ForeignKey(
        'taxonomy.Kingdom',
        on_delete=models.CASCADE,
        verbose_name="Kingdom ID",
        help_text="The kingdom to which the rank belongs."
    )
    rank = models.SmallIntegerField(
        verbose_name="Rank ID",
        help_text="A unique identifier for a specific rank within the taxonomic kingdom hierarchy."
    )
    rank_name = models.CharField(
        max_length=15,
        verbose_name="Rank Name",
        help_text="The label associated with the specific rank of a taxonomic kingdom hierarchy."
    )
    direct_parent_rank = models.IntegerField(
        verbose_name="Direct Parent Rank",
        help_text="The rank of the direct parent of the current rank."
    )
    required_parent_rank = models.IntegerField(
        verbose_name="Required Parent Rank",
        help_text="The rank of the required parent of the current rank."
    )
    last_modified = models.DateTimeField(
        verbose_name="Update Date",
        help_text="The date on which a record was last modified."
    )

    class Meta:
        unique_together = (('kingdom', 'rank'))
        verbose_name = "Rank"
        verbose_name_plural = "Ranks"

    def __str__(self):
        """
        Returns a string representation of the taxon unit type, using its rank name.

        Returns:
            str: A string representation of the taxon unit type.
        """
        return self.rank_name
