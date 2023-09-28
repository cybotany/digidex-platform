from django.db import models
from django.urls import reverse


class Vernaculars(models.Model):
    """
    Common names associated with an occurrence in Taxonomic Units.

    Attributes:
        tsn (int): Taxonomic Serial Number. The unique identifier for an occurrence of Taxonomic Units.
        vernacular_name (str): A common name associated with an occurrence of Taxonomic Units.
        language (str): Native language from which the vernacular name originates; e.g. English, French, Spanish, Portuguese, etc.
        approved_ind (str): Designation identifying those vernacular names authorized for use by regulation, statute, etc.
        update_date (datetime): The date on which a record is modified. The purpose of this element is to provide assistance to those downloading data on a periodic basis.
        vern_id (int): The serial portion of the identifier created for a vernacular name associated with an occurrence of a Taxonomic Unit.
    """

    tsn = models.IntegerField(
        verbose_name="Taxonomic Serial Number",
        help_text="The unique identifier for an occurrence of Taxonomic Units."
    )
    vernacular_name = models.CharField(
        max_length=80,
        verbose_name="Vernacular Name",
        help_text="A common name associated with an occurrence of Taxonomic Units."
    )
    language = models.CharField(
        max_length=15,
        verbose_name="Language",
        help_text="Native language from which the vernacular name originates."
    )
    approved_ind = models.CharField(
        max_length=1,
        choices=[('T', 'True'), ('F', 'False')],
        null=True,
        blank=True,
        verbose_name="Approved Indicator",
        help_text="Designation identifying those vernacular names authorized for use by regulation, statute, etc."
    )
    update_date = models.DateTimeField(
        auto_now=True,
        verbose_name="Update Date",
        help_text="The date on which a record is modified."
    )
    vern_id = models.IntegerField(
        verbose_name="Vernacular ID",
        help_text="The serial portion of the identifier created for a vernacular name associated with an occurrence of a Taxonomic Unit."
    )

    def __str__(self):
        """
        Returns a string representation of the Vernaculars.

        Returns:
            str: A string representation of the Vernaculars.
        """
        return self.vernacular_name

    def get_absolute_url(self):
        """
        Get the URL to view the details of this Vernaculars.

        Returns:
            str: The URL to view the details of this Vernaculars.
        """
        return reverse('app_name:vernacular_detail', args=[str(self.id)])
