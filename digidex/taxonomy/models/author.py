from django.db import models

class Author(models.Model):
    """
    Represents the author of a taxonomic unit.

    Attributes:
        id (IntegerField): The unique identifier for the author(s) of a taxonomic name.
        author (str): The author(s) associated with the name of a taxon.
        kingdom (ForeignKey): A unique identifier for the highest level of the taxonomic hierarchy structure.
        short_author (CharField): The author(s) associated with the name of a taxon with parenthesis, commas and periods removed.
        last_modified (datetime): The date on the record was last modified.
    """
    id = models.IntegerField(
        primary_key=True,
        editable=False,
        verbose_name="Author ID",
        help_text="The unique identifier for the author(s) of a taxonomic name."
    )
    author = models.CharField(
        max_length=100,
        verbose_name="Author",
        help_text="The author(s) associated with the name of a taxon."
    )
    kingdom = models.ForeignKey(
        'taxonomy.Kingdom',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Kingdom",
        help_text="A unique identifier for the highest level of the taxonomic hierarchy structure."
    )
    short_author = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name="Short Author",
        help_text="The author(s) associated with the name of a taxon with parenthesis, commas and periods removed."
    )
    last_modified = models.DateTimeField(
        verbose_name="Last Modified",
        help_text="The date on the record was last modified."
    )

    def __str__(self):
        return self.author

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"
