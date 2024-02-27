from django.db import models
from .base import BaseDigit

class Pet(BaseDigit):
    breed = models.CharField(max_length=100, null=True, blank=True)

    def get_description(self):
        basic_description = super().get_description()
        return f"{basic_description}. Breed: {self.breed}"
