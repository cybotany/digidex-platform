from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType


class Sensors(models.Model):
    SENSOR_TYPES = (
        ('TE', 'Temperature'),
        ('RH', 'Humidity'),
        ('VOC', 'Air Quality'),
        ('PAR', 'Light Intensity'),
    )

    sensor_type = models.CharField(max_length=3, choices=SENSOR_TYPES)
    name = models.CharField(max_length=100)


class CEA(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class GrowthChamber(CEA):
    MEASUREMENT_CHOICES = [
        ('in', 'Inches'),
        ('cm', 'Centimeters'),
    ]

    measurement_system = models.CharField(max_length=2, choices=MEASUREMENT_CHOICES, default='cm')
    chamber_width = models.DecimalField(max_digits=6, decimal_places=2)
    chamber_height = models.DecimalField(max_digits=6, decimal_places=2)
    chamber_length = models.DecimalField(max_digits=6, decimal_places=2)

    temperature_sensor = models.CharField(max_length=2, choices=MEASUREMENT_CHOICES, default='cm')
    humidity_sensor = models.CharField(max_length=2, choices=MEASUREMENT_CHOICES, default='cm')
    air_quality_sensor = models.CharField(max_length=2, choices=MEASUREMENT_CHOICES, default='cm')
    light_sensor = models.CharField(max_length=2, choices=MEASUREMENT_CHOICES, default='cm')

    @property
    def chamber_volume(self):
        volume = self.chamber_width * self.chamber_height * self.chamber_length
        if self.measurement_system == 'in':
            return volume  # return volume in cubic inches
        else:
            return volume / 16.387  # convert cubic inches to cubic centimeters


    def save(self, *args, **kwargs):
        '''
        If name is empty, count existing Growth Chambers for this user
        and generate a default name to save.
        '''
        if not self.name:
            count = GrowthChamber.objects.filter(user=self.user).count()
            self.name = f'GrowthChamber{count + 1}'
        if not self.device_type:
            self.device_type = ContentType.objects.get_for_model(self.__class__)
        super().save(*args, **kwargs)
