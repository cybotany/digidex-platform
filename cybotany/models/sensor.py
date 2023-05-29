from django.db import models
from cybotany.utils.constants import SENSOR_TYPE_CHOICES


class Sensor(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=10, choices=SENSOR_TYPE_CHOICES)
    description = models.TextField()
    min_value = models.DecimalField(max_digits=6, decimal_places=2)
    max_value = models.DecimalField(max_digits=6, decimal_places=2)
    value_unit = models.CharField(max_length=255)

    def __str__(self):
        return self.name
