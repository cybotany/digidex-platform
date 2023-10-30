from django.db import models
from django.urls import reverse


class Hierarchy(models.Model):
    """
    A support table that provides an accepted or valid Taxonomic Units full TSN hierarchy in
    a single string.

    Attributes:
        hierarchy_string (str): The concatenated TSNs, delimited with a hyphen, which represents the hierarchy from Kingdom to TSN of concern.
        taxonomic_unit (ForeignKey): The Taxonomic Unit associated with this hierarchy.
        parent_taxonomic_unit (ForeignKey): The direct parent Taxonomic Unit of the given Taxonomic Unit.
        level (int): The distance down the hierarchy from Kingdom to TSN of concern for the hierarchy entry.
        children_count (int): The number of total children a particular TSN has, from its direct children to the bottom of the hierarchy.
    """

    hierarchy_string = models.CharField(
        max_length=300,
        unique=True,
        verbose_name="Hierarchy String",
        help_text="The concatenated TSNs, delimited with a hyphen, which represents the hierarchy from Kingdom to TSN of concern."
    )
    taxonomic_unit = models.ForeignKey(
        'TaxonomicUnits',
        on_delete=models.CASCADE,
        verbose_name="Taxonomic Serial Number",
        help_text="The TSN for the hierarchy entry. The unique identifier for an occurrence of Taxonomic Units."
    )
    parent_taxonomic_unit = models.ForeignKey(
        'TaxonomicUnits',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='child_taxonomic_units',
        verbose_name="Parent TSN",
        help_text="The direct parent TSN of hierarchy.TSN."
    )
    level = models.IntegerField(
        verbose_name="Level",
        help_text="The distance down the hierarchy from Kingdom to TSN of concern for the hierarchy entry."
    )
    children_count = models.IntegerField(
        verbose_name="Children Count",
        help_text="The number of total children a particular TSN has, from its direct children to the bottom of the hierarchy."
    )

    def __str__(self):
        """
        Returns a string representation of the Hierarchy.

        Returns:
            str: A string representation of the Hierarchy.
        """
        return self.hierarchy_string

    def get_absolute_url(self):
        """
        Get the URL to view the details of this Hierarchy.

        Returns:
            str: The URL to view the details of this Hierarchy.
        """
        return reverse('app_name:hierarchy_detail', args=[str(self.id)])
