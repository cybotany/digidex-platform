from django.db import models
from .geography import Geography
from .jurisdiction import Jurisdiction
from digidex.taxonomy.utils.constants import VALID_NAME_USAGES

class Kingdom(models.Model):
    """
    The highest rank in the taxonomic hierarchical structure.

    Attributes:
        id (IntegerField): A unique identifier for the highest level of the taxonomic hierarchy structure.
        kingdom_name (CharField): The label associated with the highest level of the taxonomic hierarchy structure.
        last_modified (dateDateTimeFieldtime): The date a record was modified.
    """
    id = models.IntegerField(
        primary_key=True,
        verbose_name="Kingdom ID",
        help_text="A unique identifier for the highest level of the taxonomic hierarchy structure."
    )
    kingdom_name = models.CharField(
        max_length=10,
        verbose_name="Kingdom Name",
        help_text="The label associated with the highest level of the taxonomic hierarchy structure."
    )
    last_modified = models.DateTimeField(
        verbose_name="Update Date",
        help_text="The date a record was last modified."
    )

    def __str__(self):
        """
        Returns a string representation of the kingdom, using its name.

        Returns:
            str: A string representation of the kingdom.
        """
        return self.kingdom_name

    def valid_units_by_rank(self):
        """
        Returns a queryset with counts of units with a valid name usage,
        grouped by kingdom and rank.
        """
        
        return self.unit_set.filter(name_usage__in=VALID_NAME_USAGES).values(
            'rank__rank_name',
        ).annotate(
            valid_units_count=models.Count('id')
        ).order_by('rank')

    def valid_units_by_geography(self):
        """
        Returns a queryset with counts of valid units, grouped by geography value.
        """

        return Geography.objects.filter(
            tsn__kingdom=self,
            tsn__name_usage__in=VALID_NAME_USAGES
        ).values(
            'geography_value'
        ).annotate(
            valid_units_count=models.Count('tsn')
        ).order_by('geography_value')

    def count_units_by_jurisdiction(self):
        """
        Returns a queryset with counts of units, grouped by jurisdiction value,
        and optionally by origin (native/introduced).
        """
        return Jurisdiction.objects.filter(
            tsn__kingdom=self,
            tsn__name_usage__in=VALID_NAME_USAGES
        ).values(
            'jurisdiction_value',
            'origin'
        ).annotate(
            units_count=models.Count('tsn')
        ).order_by('jurisdiction_value', 'origin')

    class Meta:
        verbose_name = "Kingdom"
        verbose_name_plural = "Kingdoms"
