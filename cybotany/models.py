from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType



class Sensor(models.Model):
    SENSOR_TYPE_CHOICES = [
        ('temp', 'Temperature'),
        ('humidity', 'Humidity'),
        ('light', 'Light'),
        ('voc', 'Air Quality'),
    ]
    type = models.CharField(max_length=10, choices=SENSOR_TYPE_CHOICES)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Instrument(models.Model):
    INSTRUMENT_TYPE_CHOICES = [
        ('camera', 'Camera'),
        ('light', 'Light'),
        ('fan', 'Fan'),
    ]
    type = models.CharField(max_length=10, choices=INSTRUMENT_TYPE_CHOICES)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


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
    sensors = models.ManyToManyField(Sensor, blank=True)
    instruments = models.ManyToManyField(Instrument, blank=True)

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
        super().save(*args, **kwargs)
