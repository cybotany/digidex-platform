from django.db import models
from plants.utils.constants import INSTRUMENT_TYPE_CHOICES


class Instrument(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=10, choices=INSTRUMENT_TYPE_CHOICES)
    description = models.TextField()

    def __str__(self):
        return self.name
