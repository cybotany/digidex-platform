from django.db import models
from django.urls import reverse


class TUCommentsLink(models.Model):
    """
    An intersection table which provides the means for establishing a many to many
    relationship between an occurrence of Taxonomic Units and associated Comments.

    Attributes:
        tsn (int): Taxonomic Serial Number. The unique identifier for an occurrence of Taxonomic Units.
        comment_id (int): The unique identifier for remarks associated with an occurrence of Taxonomic Units.
        update_date (datetime): The date on which a record is modified.
    """

    tsn = models.IntegerField(
        verbose_name="Taxonomic Serial Number",
        help_text="The unique identifier for an occurrence of Taxonomic Units."
    )
    comment_id = models.IntegerField(
        verbose_name="Comment ID",
        help_text="The unique identifier for remarks associated with an occurrence of Taxonomic Units."
    )
    update_date = models.DateTimeField(
        verbose_name="Update Date",
        auto_now=True,
        help_text="The date on which a record is modified."
    )

    def __str__(self):
        """
        Returns a string representation of the TUCommentsLink.

        Returns:
            str: A string representation of the TUCommentsLink.
        """
        return f"TSN: {self.tsn}, Comment ID: {self.comment_id}"

    def get_absolute_url(self):
        """
        Get the URL to view the details of this TUCommentsLink.

        Returns:
            str: The URL to view the details of this TUCommentsLink.
        """
        return reverse('app_name:tu_comments_link_detail', args=[str(self.id)])
