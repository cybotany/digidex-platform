from django.db import models
from .base import BaseDigit

class Pet(BaseDigit):
    breed = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

    def get_kingdom_id(self):
        """
        Return the kingdom ID for animals.
        """
        return 5
