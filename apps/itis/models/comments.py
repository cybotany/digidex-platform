from django.db import models
from django.urls import reverse


class Comments(models.Model):
    """
    A mechanism for recording history or detail deemed important for an occurrence(s) of
    Taxonomic Units.

    Attributes:
        comment_id (int): The unique identifier for remarks associated with an occurrence of Taxonomic Units.
        commentator (str): The name of the person associated with the comment being provided with regard 
                           to an occurrence of Taxonomic Units.
        comment_detail (str): Remarks providing additional information regarding an occurrence of Taxonomic Units.
        comment_time_stamp (datetime): The date and time at which a comment associated with an occurrence of 
                                      Taxonomic Units is entered.
        update_date (datetime): The date on which a record is modified. The purpose of this element is to provide 
                                assistance to those downloading data on a periodic basis.
    """

    comment_id = models.IntegerField(
        primary_key=True,
        verbose_name="Comment ID"
    )
    commentator = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name="Commentator"
    )
    comment_detail = models.TextField(
        null=False,
        blank=False,
        verbose_name="Comment Detail"
    )
    comment_time_stamp = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Comment Timestamp"
    )
    update_date = models.DateTimeField(
        auto_now=True,
        verbose_name="Update Date"
    )

    def __str__(self):
        """
        Returns a string representation of the comment, using its detail.

        Returns:
            str: A string representation of the comment.
        """
        return self.comment_detail[:50] + "..."

    def get_absolute_url(self):
        """
        Get the URL to view the details of this comment.

        Returns:
            str: The URL to view the details of this comment.
        """
        return reverse('taxonomy:describe_comment', args=[str(self.comment_id)])
