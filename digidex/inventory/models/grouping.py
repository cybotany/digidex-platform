from django.db import models

class Grouping(models.Model):
    """
    Model for organizing digitized entities into groups.

    Attributes:
        name (CharField): A human-readable name for the digitized entity.
        description (TextField): A short description of the digitized entity.
        user (ForeignKey): A relationship to the User model.
        created_at (DateTimeField): The date and time when the Digit instance was created.
        last_modified (DateTimeField): The date and time when the Digit instance was last modified.
    """
    name = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        help_text="The name of the group."
    )
    description = models.TextField(
        blank=True,
        null=True,
        help_text="The description of the group."
    )
    user = models.ForeignKey(
        'auth.User',
        related_name='digit_groups',
        on_delete=models.CASCADE,
        help_text="A relationship to the User model."
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Created At",
        help_text="The date and time when the grouping instance was created."
    )
    last_modified = models.DateTimeField(
        auto_now=True,
        verbose_name="Last Modified",
        help_text="The date and time when the grouping instance was last modified."
    )
    class Meta:
        unique_together = ('user', 'name')

    def __str__(self):
        return self.name
