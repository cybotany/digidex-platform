from django.db import models
from django.urls import reverse


class ReferenceLinks(models.Model):
    """
    An intersection table that provides a link between occurrences of Taxonomic Units and
    occurrences of publications, experts, or other_sources.

    Attributes:
        tsn (int): Taxonomic Serial Number. The unique identifier for an occurrence of Taxonomic Units.
        doc_id_prefix (str): A designation affixed to the documentation_id identifying the reference as a publication, expert or other source.
        documentation_id (int): The serial portion of the identifier created for either the Publications table, the Experts table or the Other_Sources table used with the documentation_id_prefix to provide the reference link with an instance from the Taxonomic_units table.
        original_desc_ind (str): Indicator used to identify that this occurrence represents the reference of the original description, when available.
        init_itis_desc_ind (str): Indicator used to identify the reference(s) that serve as the reason for an occurrence of Taxonomic Units being recognized where the original reference is unavailable.
        change_track_id (int): The unique identifier assigned to a change made to an occurrence of Taxonomic Units.
        vernacular_name (str): NOT IN USE.
        update_date (datetime): The date on which a record is modified. The purpose of this element is to provide assistance to those downloading data on a periodic basis.
    """

    tsn = models.IntegerField(
        verbose_name="Taxonomic Serial Number",
        help_text="The unique identifier for an occurrence of Taxonomic Units."
    )
    doc_id_prefix = models.CharField(
        max_length=3,
        choices=[('EXP', 'Expert'), ('PUB', 'Publication'), ('SRC', 'Source')],
        verbose_name="Document ID Prefix",
        help_text="A designation affixed to the documentation_id identifying the reference as a publication, expert or other source."
    )
    documentation_id = models.IntegerField(
        verbose_name="Documentation ID",
        help_text="The serial portion of the identifier created for either the Publications table, the Experts table or the Other_Sources table."
    )
    original_desc_ind = models.CharField(
        max_length=1,
        choices=[('T', 'True'), ('F', 'False')],
        null=True,
        blank=True,
        verbose_name="Original Description Indicator",
        help_text="Indicator used to identify that this occurrence represents the reference of the original description, when available."
    )
    init_itis_desc_ind = models.CharField(
        max_length=1,
        choices=[('T', 'True'), ('F', 'False')],
        null=True,
        blank=True,
        verbose_name="Initial ITIS Description Indicator",
        help_text="Indicator used to identify the reference(s) that serve as the reason for an occurrence of Taxonomic Units being recognized where the original reference is unavailable."
    )
    change_track_id = models.IntegerField(
        null=True,
        blank=True,
        verbose_name="Change Track ID",
        help_text="The unique identifier assigned to a change made to an occurrence of Taxonomic Units."
    )
    vernacular_name = models.CharField(
        max_length=80,
        null=True,
        blank=True,
        verbose_name="Vernacular Name"
    )
    update_date = models.DateTimeField(
        auto_now=True,
        verbose_name="Update Date",
        help_text="The date on which a record is modified."
    )

    def __str__(self):
        """
        Returns a string representation of the ReferenceLinks.

        Returns:
            str: A string representation of the ReferenceLinks.
        """
        return f"TSN: {self.tsn}, Documentation ID: {self.documentation_id}"

    def get_absolute_url(self):
        """
        Get the URL to view the details of this ReferenceLinks.

        Returns:
            str: The URL to view the details of this ReferenceLinks.
        """
        return reverse('app_name:reference_link_detail', args=[str(self.id)])
