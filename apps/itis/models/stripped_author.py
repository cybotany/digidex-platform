from django.db import models
from django.urls import reverse


class StrippedAuthor(models.Model):
    """
    A support table that provides the author(s) associated with the name of a taxon with
    parenthesis, commas and periods removed. Designed to be helpful when searching for an
    author whose name contains a different punctuation for different taxon names.

    Attributes:
        taxon_author_id (int): A unique identifier for the author(s) of a taxonomic name.
        shortauthor (str): The author(s) associated with the name of a taxon with parenthesis, commas and periods removed.
    """

    taxon_author_id = models.IntegerField(
        verbose_name="Taxon Author ID",
        help_text="A unique identifier for the author(s) of a taxonomic name."
    )
    shortauthor = models.CharField(
        max_length=100,
        verbose_name="Short Author",
        help_text="The author(s) associated with the name of a taxon with parenthesis, commas and periods removed."
    )

    def __str__(self):
        """
        Returns a string representation of the StrippedAuthor.

        Returns:
            str: A string representation of the StrippedAuthor.
        """
        return self.shortauthor

    def get_absolute_url(self):
        """
        Get the URL to view the details of this StrippedAuthor.

        Returns:
            str: The URL to view the details of this StrippedAuthor.
        """
        return reverse('app_name:stripped_author_detail', args=[str(self.id)])
