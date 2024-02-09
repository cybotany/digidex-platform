from django.db import models


class Hierarchy(models.Model):
    """
    Represents the hierarchy of a taxonomic unit as per ITIS data model documentation.

    Attributes:
        hierarchy_string (TextField): A string representation of the complete hierarchy path.
        tsn (ForeignKey): The Taxonomic Serial Number (TSN) of the taxonomic unit. Links to a 'Unit' model.
        parent_tsn (ForeignKey): The TSN of the parent taxonomic unit.
        level (IntegerField): The hierarchical level of the taxonomic unit.
        children_count (IntegerField): The count of direct children under this taxonomic unit.
    """
    hierarchy_string = models.TextField(
        unique=True,
        verbose_name="Hierarchy String",
        help_text="A string representation of the complete hierarchy path."
    )
    tsn = models.ForeignKey(
        'taxonomy.Unit',
        on_delete=models.CASCADE,
        verbose_name="Taxonomic Serial Number",
        db_column="tsn",
        help_text="Taxonomic Serial Number (TSN) for the Taxonomic Unit."
    )
    parent_tsn = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        related_name='children',
        null=True,
        blank=True,
        verbose_name="Parent TSN",
        help_text="The TSN of the parent taxonomic unit."
    )
    level = models.IntegerField(
        verbose_name="Level",
        help_text="The hierarchical level of the taxonomic unit."
    )
    children_count = models.IntegerField(
        verbose_name="Children Count",
        help_text="The count of direct children under this taxonomic unit."
    )

    def __str__(self):
        return self.hierarchy_string

    class Meta:
        verbose_name = "Hierarchy"
        verbose_name_plural = "Hierarchies"
