from django.db import models

class ItisAuthor(models.Model):
    """
    Represents the author of a taxonomic unit.

    Attributes:
        id (IntegerField): The unique identifier for the author(s) of a taxonomic name.
        name (str): The author(s) associated with the name of a taxon.
        cleaned_name (CharField): The author(s) associated with the name of a taxon with parenthesis, commas and periods removed.
        last_modified (datetime): The date on the record was last modified.
    """
    id = models.IntegerField(
        primary_key=True,
        editable=False,
        verbose_name="Author ID",
        help_text="The unique identifier for the author(s) of a taxonomic name."
    )
    name = models.CharField(
        max_length=100,
        verbose_name="Author",
        help_text="The author(s) associated with the name of a taxon."
    )
    cleaned_name = models.CharField(
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
        return self.name

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"
