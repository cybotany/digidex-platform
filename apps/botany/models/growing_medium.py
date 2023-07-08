from django.db import models
from django.contrib.auth import get_user_model


class GrowingMedium(models.Model):
    """
    Growing medium model for storing additional user information.

    Fields:
        user (ForeignKey): Reference to the user who added this growing medium.
        name (CharField): A char field for growing medium, maximum length 100 characters.
        description (TextField): A text field used for describing the growing medium.
    """
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        null=True
    )
    name = models.CharField(
        max_length=100,
        blank=True,
        help_text='Name of the growing medium for plants.'
    )
    description = models.TextField(
        blank=True,
        help_text='Description for the growing medium.'
    )

    def __str__(self):
        return self.name
