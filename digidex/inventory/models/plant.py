from django.db import models
from .digit import Digit

class Plant(Digit):
    sunlight_requirement = models.CharField(max_length=100, null=True, blank=True)

    def get_description(self):
        basic_description = super().get_description()
        return f"{basic_description}. Sunlight Requirement: {self.sunlight_requirement}"