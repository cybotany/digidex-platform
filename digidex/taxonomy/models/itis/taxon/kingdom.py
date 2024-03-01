from django.db import models

class ItisTaxonKingdom(models.Model):
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

    class Meta:
        verbose_name = "Kingdom"
        verbose_name_plural = "Kingdoms"
