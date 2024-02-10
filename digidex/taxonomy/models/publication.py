from django.db import models

class Publication(models.Model):
    """
    Represents printed references that are taxonomically significant for additions or
    changes to occurrences of the Taxonomic_units table and/or associated data, or that
    provide credibility for approved vernacular names.

    Attributes:
        publication_id (IntegerField): The unique identifier of a printed reference.
        reference_author (CharField): Author(s) of the printed reference.
        title (CharField): The identifying name given an article contained in a printed reference.
        publication_name (CharField): The title of the printed reference, including volume and number, if applicable.
        listed_publication_date (DateTimeField): The date printed on a journal or other printed reference.
        actual_publication_date (DateTimeField): The true date on which the printed reference was published.
        publisher (CharField): Producer of the printed reference.
        publication_place (CharField): Location of the publisher.
        isbn (CharField): The ISBN number of a book cited.
        issn (CharField): The ISSN number of a journal cited.
        pages (CharField): Page numbers within the printed reference to which the specific citation refers.
        publication_comment (TextField): Remarks associated with the printed reference cited.
        last_modified (DateTimeField): The date and time the record was last updated. Automatically set on record update.
    """
    publication_id = models.IntegerField(
        primary_key=True, 
        help_text="The unique identifier of a printed reference."
    )
    reference_author = models.CharField(
        max_length=100, 
        blank=True, 
        null=True, 
        help_text="Author(s) of the printed reference."
    )
    title = models.CharField(
        max_length=255, 
        blank=True, 
        null=True, 
        help_text="The identifying name given an article contained in a printed reference."
    )
    publication_name = models.CharField(
        max_length=255, 
        blank=True, 
        null=True, 
        help_text="The title of the printed reference, including volume and number, if applicable."
    )
    listed_publication_date = models.DateTimeField(
        blank=True, 
        null=True, 
        help_text="The date printed on a journal or other printed reference."
    )
    actual_publication_date = models.DateTimeField(
        blank=True, 
        null=True, 
        help_text="The true date on which the printed reference was published."
    )
    publisher = models.CharField(
        max_length=80, 
        blank=True, 
        null=True, 
        help_text="Producer of the printed reference."
    )
    publication_place = models.CharField(
        max_length=40, 
        blank=True, 
        null=True, 
        help_text="Location of the publisher."
    )
    isbn = models.CharField(
        max_length=16, 
        blank=True, 
        null=True, 
        help_text="The ISBN number of a book cited."
    )
    issn = models.CharField(
        max_length=16, 
        blank=True, 
        null=True, 
        help_text="The ISSN number of a journal cited."
    )
    pages = models.CharField(
        max_length=15, 
        blank=True, 
        null=True, 
        help_text="Page numbers within the printed reference to which the specific citation refers."
    )
    publication_comment = models.TextField(
        max_length=500, 
        blank=True, 
        null=True, 
        help_text="Remarks associated with the printed reference cited."
    )
    last_modified = models.DateTimeField(
        blank=True, 
        null=True,
        help_text="The date and time the record was last updated."
    )

    def __str__(self):
        return f"Publication: {self.publication_id} - {self.title}"

    class Meta:
        verbose_name = "Publication"
        verbose_name_plural = "Publications"
