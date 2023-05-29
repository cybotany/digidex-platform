from django.db import models
from django.contrib.auth.models import User
from cybotany.utils.constants import MEASUREMENT_CHOICES
from cybotany.utils.helpers import calculate_chamber_volume
from .instrument import Instrument
from .sensor import Sensor


class GrowthChamber(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    measurement_system = models.CharField(max_length=2, choices=MEASUREMENT_CHOICES, default='cm')
    chamber_width = models.DecimalField(max_digits=6, decimal_places=2)
    chamber_height = models.DecimalField(max_digits=6, decimal_places=2)
    chamber_length = models.DecimalField(max_digits=6, decimal_places=2)
    sensors = models.ManyToManyField(Sensor, blank=True)
    instruments = models.ManyToManyField(Instrument, blank=True)

    @property
    def chamber_volume(self):
        return calculate_chamber_volume(self.chamber_width,
                                        self.chamber_height,
                                        self.chamber_length,
                                        self.measurement_system)

    def save(self, *args, **kwargs):
        '''
        If name is empty, count existing Growth Chambers for this user
        and generate a default name to save.
        '''
        if not self.name:
            count = GrowthChamber.objects.filter(user=self.user).count()
            self.name = f'GrowthChamber{count + 1}'
        super().save(*args, **kwargs)
