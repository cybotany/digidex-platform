from django.db import models
from .kingdom import Kingdom
from .rank import Rank


class KingdomRank(models.Model):
    """
    Represents a unique combination of a kingdom and a rank in the taxonomic hierarchy.

    This model is used as an intermediate table to establish a unique relationship 
    between the Kingdom and Rank models. It ensures that each kingdom is associated 
    with a specific rank in a unique way.

    Attributes:
        kingdom (ForeignKey): A reference to the Kingdom model. Represents the highest level 
                              in the taxonomic hierarchical structure.
        rank (ForeignKey): A reference to the Rank model. Defines a specific level within the 
                           taxonomic hierarchical structure.
    """

    kingdom = models.ForeignKey(
        Kingdom,
        on_delete=models.CASCADE,
        verbose_name="Kingdom",
        related_name='ranks'
    )
    rank = models.ForeignKey(
        Rank,
        on_delete=models.CASCADE,
        verbose_name="Rank",
        related_name='kingdoms'
    )

    class Meta:
        unique_together = ('kingdom', 'rank')
        verbose_name = "Kingdom and Rank Combination"
        verbose_name_plural = "Kingdom and Rank Combinations"
        ordering = ['kingdom', 'rank']

    def __str__(self):
        """
        Returns a string representation of the KingdomRank, using the names of the kingdom and rank.
        """
        return f"{self.kingdom.kingdom_name} - {self.rank.rank_name}"
