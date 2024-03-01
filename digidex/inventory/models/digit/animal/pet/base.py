from django.db import models
from digidex.inventory.models.digit.animal import base

class Pet(base.Animal):
    age = models.PositiveIntegerField(
        null=True,
        blank=True
    )
    breed = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )
    records = models.JSONField(
        default=list,
        blank=True,
        null=True
    )

    class Meta:
        abstract = True

    def get_kingdom_id(self):
        """
        Return the kingdom ID for animals.
        """
        return 5
