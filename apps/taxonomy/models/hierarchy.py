from django.db import models


class Hierarchy(models.Model):
    """
    Represents the hierarchy of a taxonomic unit as per ITIS data model.
    """
    hierarchy_string = models.TextField(
        verbose_name="Hierarchy String",
        null=True,
        blank=True
    )
    tsn = models.ForeignKey(
        'Units',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Taxonomic Serial Number",
        db_column='tsn'
    )
    parent_tsn = models.IntegerField(
        null=True,
        blank=True,
        verbose_name="Parent Taxonomic Serial Number",
        db_column='parent_tsn'
    )
    level = models.IntegerField(
        null=True,
        blank=True,
        verbose_name="Taxonomic Rank"
    )
    children_count = models.IntegerField(
        null=True,
        blank=True,
        verbose_name="Taxonomic Rank"
    )

    class Meta:
        verbose_name_plural = "Hierarchies"

    def __str__(self):
        return self.hierarchy_string
