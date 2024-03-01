from django.db import models

from digidex.inventory.models.digit import base as base_digit

class Plant(base_digit.Digit):
    sunlight_requirement = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

    def get_kingdom_id(self):
        """
        Return the kingdom ID for animals.
        """
        return 3