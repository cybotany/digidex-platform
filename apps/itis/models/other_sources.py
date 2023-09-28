from django.db import models
from django.urls import reverse


class OtherSources(models.Model):
    """
    References, other than persons or publications, that are taxonomically significant for
    additions or changes to occurrences of the Taxonomic_units table and/or associated data,
    or that provide credibility for vernacular names.

    Attributes:
        source_id_prefix (str): A prefix attached to a serial id to identify the record as an Other Source.
        source_id (int): The unique identifier for a supplier of information, other than a person or publication, lending credence to the establishment of or changes to an occurrence of Taxonomic Units.
        source_type (str): The designation of the kind of supplier providing information to the ITIS (other than a person or publication); e.g. database.
        source (str): The name of the supplier of information, other than a person or publication, to the ITIS database.
        version (str): Number, date or other identifying characteristic of the source which indicates the functionality and/or data at a point in time in the life of the system, database, etc.
        acquisition_date (datetime): The date on which ITIS acquired the data it is utilizing from a source other than a publication or expert.
        source_comment (str): Remarks associated with the provider of information to the ITIS (other than a person or publication).
        update_date (datetime): The date on which a record is modified. The purpose of this element is to provide assistance to those downloading data on a periodic basis.
    """

    source_id_prefix = models.CharField(
        max_length=3,
        default="SRC",
        editable=False,
        verbose_name="Source ID Prefix"
    )
    source_id = models.AutoField(
        primary_key=True,
        verbose_name="Source ID"
    )
    source_type = models.CharField(
        max_length=10,
        null=True,
        blank=True,
        verbose_name="Source Type"
    )
    source = models.CharField(
        max_length=64,
        null=True,
        blank=True,
        verbose_name="Source Name"
    )
    version = models.CharField(
        max_length=10,
        null=True,
        blank=True,
        verbose_name="Version"
    )
    acquisition_date = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name="Acquisition Date"
    )
    source_comment = models.CharField(
        max_length=500,
        null=True,
        blank=True,
        verbose_name="Source Comment"
    )
    update_date = models.DateTimeField(
        auto_now=True,
        verbose_name="Update Date"
    )

    def __str__(self):
        """
        Returns a string representation of the other source, using its identifier.

        Returns:
            str: A string representation of the other source.
        """
        return f"{self.source_id_prefix}-{self.source_id}"

    def get_absolute_url(self):
        """
        Get the URL to view the details of this other source.

        Returns:
            str: The URL to view the details of this other source.
        """
        return reverse('taxonomy:describe_other_source', args=[str(self.source_id)])
