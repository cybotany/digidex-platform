from django.db import models
from django.urls import reverse
from .base import BaseDigit

class Plant(BaseDigit):
    sunlight_requirement = models.CharField(max_length=100, null=True, blank=True)

    def get_description(self):
        basic_description = super().get_description()
        return f"{basic_description}. Sunlight Requirement: {self.sunlight_requirement}"

    def get_absolute_url(self):
        """
        Get the URL to view the details of this plant.

        Returns:
            str: The URL to view the details of this plant.
        """
        return reverse('inventory:plant-details', kwargs={'uuid': self.uuid})