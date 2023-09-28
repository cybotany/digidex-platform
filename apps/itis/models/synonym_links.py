from django.db import models
from django.urls import reverse


class SynonymLinks(models.Model):
    """
    A mechanism to provide the link between an accepted taxonomic name and alternates or
    predecessors to it.

    Attributes:
        tsn (int): Taxonomic Serial Number. The unique identifier for an occurrence of Taxonomic Units.
        tsn_accepted (int): The taxonomic serial number assigned to the accepted occurrence of Taxonomic Units to which a synonym is associated.
        update_date (datetime): The date on which a record is modified. The purpose of this element is to provide assistance to those downloading data on a periodic basis.
    """

    tsn = models.IntegerField(
        verbose_name="Taxonomic Serial Number",
        help_text="The unique identifier for an occurrence of Taxonomic Units."
    )
    tsn_accepted = models.IntegerField(
        verbose_name="Accepted Taxonomic Serial Number",
        help_text="The taxonomic serial number assigned to the accepted occurrence of Taxonomic Units to which a synonym is associated."
    )
    update_date = models.DateTimeField(
        verbose_name="Update Date",
        auto_now=True,
        help_text="The date on which a record is modified."
    )

    def __str__(self):
        """
        Returns a string representation of the SynonymLinks.

        Returns:
            str: A string representation of the SynonymLinks.
        """
        return f"TSN: {self.tsn}, Accepted TSN: {self.tsn_accepted}"

    def get_absolute_url(self):
        """
        Get the URL to view the details of this SynonymLinks.

        Returns:
            str: The URL to view the details of this SynonymLinks.
        """
        return reverse('app_name:synonym_link_detail', args=[str(self.id)])
