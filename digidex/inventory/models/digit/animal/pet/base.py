from django.db import models

from digidex.inventory.models.digit.animal import base as base_animal

class Pet(base_animal.Animal):
    """
    A class representing a pet digit.

    Attributes:
    - age (PositiveIntegerField): The age of the pet in years.
    - breed (CharField): The pet breed.
    - records (JSONField): A list of records for the pet.
    """
    age = models.PositiveIntegerField(
        null=True,
        blank=True,
        help_text="The age of the pet in years."
    )
    breed = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        help_text="The pet breed."
    )
    records = models.JSONField(
        default=list,
        blank=True,
        null=True,
        help_text="A list of records for the pet."
    )

    class Meta:
        abstract = True
