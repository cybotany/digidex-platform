from django.db import models
from .base import BaseDigit

class Plant(BaseDigit):
    sunlight_requirement = models.CharField(max_length=100, null=True, blank=True)

    def get_description(self):
        basic_description = super().get_description()
        return f"{basic_description}. Sunlight Requirement: {self.sunlight_requirement}"
