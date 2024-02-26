from django.db import models
from django.urls import reverse
from .base import BaseDigit

class Pet(BaseDigit):
    breed = models.CharField(max_length=100, null=True, blank=True)

    def get_description(self):
        basic_description = super().get_description()
        return f"{basic_description}. Breed: {self.breed}"

    def get_absolute_url(self):
        """
        Get the URL to view the details of this Pet.

        Returns:
            str: The URL to view the details of this Pet.
        """
        return reverse('inventory:pet-details', kwargs={'uuid': self.uuid})