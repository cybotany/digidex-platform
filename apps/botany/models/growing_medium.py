from django.db import models


class GrowingMedium(models.Model):
    """
    Growing medium model for storing additional user information.

    Fields:
        name (CharField): A char field for growing medium, maximum length 100 characters.
        description (TextField): A text field used for describing the growing medium.
    """
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
