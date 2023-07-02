from django.db import models

from apps.utils.constants import GROWING_METHODS


class GrowingMethod(models.Model):
    """
    Method for growing plants model.

    Fields:
        name (CharField): A char field for growing method, maximum length 30 characters.
    """
    name = models.CharField(
        max_length=100,
        choices=GROWING_METHODS,
        blank=False,
        null=False,
        help_text='Growing methods for plants.'
    )
