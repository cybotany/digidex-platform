from django.db import models


class Hierarchy(models.Model):
    """
    Represents the hierarchy of a taxonomic unit as per ITIS data model documentation.

    Fields:
        hierarchy_string (TextField): A string representation of the complete hierarchy path.
        tsn (IntegerField): The Taxonomic Serial Number (TSN) of the taxonomic unit. 
                          Links to a 'Unit' model.
        parent_tsn (IntegerField): The TSN of the parent taxonomic unit.
        level (IntegerField): The hierarchical level of the taxonomic unit.
        children_count (IntegerField): The count of direct children under this taxonomic unit.
    """
    hierarchy_string = models.TextField(
        unique=True,
        null=False,
        blank=False,
        verbose_name="Hierarchy String"
    )
    tsn = models.IntegerField(
        null=False,
        blank=False
    )
    parent_tsn = models.IntegerField(
        null=True,
        blank=True,
        verbose_name="Parent Taxonomic Serial Number",
        db_column='parent_tsn'
    )
    level = models.IntegerField(
        null=False,
        blank=False,
        verbose_name="Taxonomic Rank"
    )
    children_count = models.IntegerField(
        null=False,
        blank=False,
        verbose_name="Taxonomic Rank"
    )

    class Meta:
        verbose_name_plural = "Hierarchies"

    def __str__(self):
        return self.hierarchy_string
