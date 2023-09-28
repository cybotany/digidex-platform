from django.db import models
from django.urls import reverse


class Publications(models.Model):
    """
    Printed references that are taxonomically significant for additions or changes to
    occurrences of the Taxonomic_units table and/or associated data, or that provide
    credibility for approved vernacular names.

    Attributes:
        publication_id_prefix (str): A prefix attached to a serial number to associate the record with the Publications table.
        publication_id (int): The unique identifier of a printed reference.
        reference_author (str): Author(s) of a printed reference.
        title (str): The identifying name given an article contained in a printed reference.
        publication_name (str): The identifying title of the printed reference, including volume and number, if applicable.
        listed_pub_date (datetime): The date printed on a journal or other printed reference.
        actual_pub_date (datetime): The true date on which a journal or other written reference was published. It may or may not correspond with the publication's listed date.
        publisher (str): Producer of a printed reference.
        pub_place (str): Location of the publisher of a printed reference.
        isbn (str): The ISBN number of a book cited; older publications and some alternatively published books do not have assigned ISBN numbers.
        issn (str): The ISSN number of a journal cited; older journals and some alternatively published publications do not have assigned ISSN numbers.
        pages (str): Page numbers within a printed reference to which the specific citation refers.
        pub_comment (str): Remarks associated with the printed reference cited.
        update_date (datetime): The date on which a record is modified. The purpose of this element is to provide assistance to those downloading data on a periodic basis.
    """

    publication_id_prefix = models.CharField(
        max_length=3,
        default="PUB",
        editable=False,
        verbose_name="Publication ID Prefix"
    )
    publication_id = models.AutoField(
        primary_key=True,
        verbose_name="Publication ID"
    )
    reference_author = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name="Reference Author"
    )
    title = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name="Title"
    )
    publication_name = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name="Publication Name"
    )
    listed_pub_date = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name="Listed Publication Date"
    )
    actual_pub_date = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name="Actual Publication Date"
    )
    publisher = models.CharField(
        max_length=80,
        null=True,
        blank=True,
        verbose_name="Publisher"
    )
    pub_place = models.CharField(
        max_length=40,
        null=True,
        blank=True,
        verbose_name="Publication Place"
    )
    isbn = models.CharField(
        max_length=16,
        null=True,
        blank=True,
        verbose_name="ISBN"
    )
    issn = models.CharField(
        max_length=16,
        null=True,
        blank=True,
        verbose_name="ISSN"
    )
    pages = models.CharField(
        max_length=15,
        null=True,
        blank=True,
        verbose_name="Pages"
    )
    pub_comment = models.CharField(
        max_length=500,
        null=True,
        blank=True,
        verbose_name="Publication Comment"
    )
    update_date = models.DateTimeField(
        auto_now=True,
        verbose_name="Update Date"
    )

    def __str__(self):
        """
        Returns a string representation of the publication, using its title.

        Returns:
            str: A string representation of the publication.
        """
        return self.title

    def get_absolute_url(self):
        """
        Get the URL to view the details of this publication.

        Returns:
            str: The URL to view the details of this publication.
        """
        return reverse('taxonomy:describe_publication', args=[str(self.publication_id)])
