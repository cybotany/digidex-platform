from django.db import models
from django.urls import reverse


class Kingdoms(models.Model):
    """
    The highest rank in the taxonomic hierarchical structure.

    Attributes:
        kingdom_id (int): A unique identifier for the highest level of the taxonomic hierarchy structure.
        kingdom_name (str): The label associated with the highest level of the taxonomic hierarchy structure.
        update_date (datetime): The date on which a record is modified. The purpose of this element is to provide assistance to those downloading data on a periodic basis.
    """

    kingdom_id = models.AutoField(
        primary_key=True,
        verbose_name="Kingdom ID"
    )
    kingdom_name = models.CharField(
        max_length=10,
        null=False,
        blank=False,
        verbose_name="Kingdom Name"
    )
    update_date = models.DateTimeField(
        auto_now=True,
        verbose_name="Update Date"
    )

    def __str__(self):
        """
        Returns a string representation of the kingdom, using its name.

        Returns:
            str: A string representation of the kingdom.
        """
        return self.kingdom_name

    def get_absolute_url(self):
        """
        Get the URL to view the details of this kingdom.

        Returns:
            str: The URL to view the details of this kingdom.
        """
        return reverse('taxonomy:describe_kingdom', args=[str(self.kingdom_id)])
