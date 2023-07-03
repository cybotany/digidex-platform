from django.db import models

from .growing_method import GrowingMethod


class GrowingMedium(models.Model):
    """
    Growing medium model for storing additional user information.

    Fields:
        name (CharField): A char field for growing medium, maximum length 100 characters.
        growing_methods (ManyToManyField): A many to many field for growing method this medium is used in.
    """
    name = models.CharField(
        max_length=100,
        blank=True,
        help_text='Growing mediums for plants.'
    )
    growing_methods = models.ManyToManyField(
        GrowingMethod,
        related_name="growing_mediums"
    )
