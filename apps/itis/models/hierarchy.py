from django.db import models
from django.urls import reverse


class Hierarchy(models.Model):
    """
    A support table that provides an accepted or valid Taxonomic Units full TSN hierarchy in
    a single string.

    Attributes:
        hierarchy_string (str): The concatenated TSNs, delimited with a hyphen, which represents the hierarchy from Kingdom to TSN of concern.
        tsn (int): Taxonomic Serial Number. The unique identifier for an occurrence of Taxonomic Units.
        parent_tsn (int): The direct parent TSN of hierarchy.TSN.
        level (int): The distance down the hierarchy from Kingdom to TSN of concern for the hierarchy entry. For example, TSN 51, Schizomycetes, a Bacteria Class, has a level of 2.
        children_count (int): The number of total children a particular TSN has, from its direct children to the bottom of the hierarchy.
    """

    hierarchy_string = models.CharField(
        max_length=300,
        unique=True,
        verbose_name="Hierarchy String",
        help_text="The concatenated TSNs, delimited with a hyphen, which represents the hierarchy from Kingdom to TSN of concern."
    )
    tsn = models.IntegerField(
        verbose_name="Taxonomic Serial Number",
        help_text="The TSN for the hierarchy entry. The unique identifier for an occurrence of Taxonomic Units."
    )
    parent_tsn = models.IntegerField(
        null=True,
        blank=True,
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
