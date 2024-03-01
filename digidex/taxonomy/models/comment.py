from django.db import models

class Comment(models.Model):
    """
    A mechanism for recording history or detail deemed important for an occurrence(s) of
    Taxonomic Unit.

    Attributes:
        id (IntegerField): The unique identifier for the comment.
        commentator (CharField): The name of the person who made the comment.
        comment (TextField): The comment itself.
        created_at (DateTimeField): The date and time when the comment was made.
        last_modified (DateTimeField): The date and time when the record was last modified.
    """
    id = models.IntegerField(
        primary_key=True,
        verbose_name="Comment ID",
        help_text="The unique identifier for the comment."
    )
    commentator = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name="Commentator",
        help_text="The name of the person who made the comment."
    )
    comment = models.TextField(
        max_length=2000,
        verbose_name="Comment",
        help_text="Remarks providing additional information regarding a Taxonomic Unit."
    )
    created_at = models.DateTimeField(
        verbose_name="Created At",
        help_text="The date and time when the comment was made."
    )
    last_modified = models.DateTimeField(
        verbose_name="Last Modified",
        help_text="The date and time when the record was last modified."
    )

    def __str__(self):
        """
        Returns a string representation of the comment.
        """
        return self.comment

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"