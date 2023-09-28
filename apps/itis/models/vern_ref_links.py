from django.db import models
from django.urls import reverse


class VernRefLinks(models.Model):
    """
    An intersection table that provides a link between occurrences of Vernaculars and
    occurrences of Publications, Experts, or Other_Sources.

    Attributes:
        tsn (int): Taxonomic Serial Number. The unique identifier for an occurrence of Taxonomic Units.
        doc_id_prefix (str): A designation affixed to the documentation_id identifying the reference as a publication, expert or other source.
        documentation_id (int): The serial portion of the identifier created for either the Publications table, the Experts table or the Other_Sources table used with the documentation_id_prefix to provide the reference link with an instance from the vernaculars table.
        update_date (datetime): The date on which a record is modified. The purpose of this element is to provide assistance to those downloading data on a periodic basis.
        vern_id (int): The serial portion of the identifier created for a vernacular name associated with an occurrence of a Taxonomic Unit.
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
        Returns a string representation of the VernRefLinks.

        Returns:
            str: A string representation of the VernRefLinks.
        """
        return f"TSN: {self.tsn}, Documentation ID: {self.documentation_id}"

    def get_absolute_url(self):
        """
        Get the URL to view the details of this VernRefLinks.

        Returns:
            str: The URL to view the details of this VernRefLinks.
        """
        return reverse('app_name:vern_ref_link_detail', args=[str(self.id)])
