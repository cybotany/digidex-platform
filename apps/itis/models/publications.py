from django.db import models


class Publications(models.Model):
    """
    Printed references that are taxonomically significant for additions or changes to
    occurrences of the Taxonomic_units table and/or associated data, or that provide
    credibility for approved vernacular names.

    pub_id_prefix: A prefix attached to a serial number to associate the record with the Publications table.
    publication_id: : The unique identifier of a printed reference.
    reference_author: Author(s) of a printed reference.
    title: The identifying name given an article contained in a printed reference
    publication_name: : The identifying title of the printed reference, including volume and number, if applicable.
    listed_pub_date: The date printed on a journal or other printed reference.
    actual_pub_date: The true date on which a journal or other written reference was published. It may or may not correspond with the publication’s listed date.
    publisher: Producer of a printed reference.
    pub_place: Location of the publisher of a printed reference.
    isbn: The ISBN number of a book cited; older publications and some alternatively published books do not have assigned ISBN numbers.
    issn: The ISSN number of a journal cited; older journals and some alternatively published publications do not have assigned ISSN numbers.
    pages: Page numbers within a printed reference to which the specific citation refers.
    pub_comment: : Remarks associated with the printed reference cited
    update_date: The date  on which the record was last updated. The purpose of this element is to provide assistance to those downloading data on a periodic basis.
    """
    pub_id_prefix = models.CharField(primary_key=True, max_length=3)
    publication_id = models.IntegerField(primary_key=True)
    reference_author = models.CharField(max_length=100)
    title = models.CharField(max_length=255, blank=True, null=True)
    publication_name = models.CharField(max_length=255)
    listed_pub_date = models.DateField(blank=True, null=True)
    actual_pub_date = models.DateField()
    publisher = models.CharField(max_length=80, blank=True, null=True)
    pub_place = models.CharField(max_length=40, blank=True, null=True)
    isbn = models.CharField(max_length=16, blank=True, null=True)
    issn = models.CharField(max_length=16, blank=True, null=True)
    pages = models.CharField(max_length=15, blank=True, null=True)
    pub_comment = models.CharField(max_length=500, blank=True, null=True)
    update_date = models.DateField()

    class Meta:
        db_table = 'publications'
