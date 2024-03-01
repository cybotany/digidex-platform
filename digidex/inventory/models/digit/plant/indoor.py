from django.db import models

from digidex.inventory.models.digit.plant import base as base_plant

class IndoorPlant(base_plant.Plant):
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