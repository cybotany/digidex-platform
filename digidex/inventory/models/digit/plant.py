from django.db import models
from .base import BaseDigit

class Plant(BaseDigit):
    sunlight_requirement = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )
