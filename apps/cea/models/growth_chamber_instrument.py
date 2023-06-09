from django.db import models
from .growth_chamber import GrowthChamber


class GrowthChamberInstrumentData(models.Model):
    growth_chamber = models.ForeignKey(GrowthChamber, on_delete=models.CASCADE, related_name='sensor_data')
    timestamp = models.DateTimeField(auto_now_add=True)
    humidity = models.DecimalField(max_digits=5, decimal_places=2)
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    pressure = models.DecimalField(max_digits=5, decimal_places=2)
    gas = models.DecimalField(max_digits=5, decimal_places=2)
    image_url = models.URLField(blank=True, null=True)

    class Meta:
        ordering = ['timestamp']

    def __str__(self):
        return f'{self.growth_chamber.name} - {self.timestamp}'
