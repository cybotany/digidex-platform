from django.db import models

from digidex.inventory.models.digit.animal import base as base_animal

class Pet(base_animal.Animal):
    """
    A class representing a pet digit.
    """
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
