from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType


class CEA(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    light_sensor = models.CharField(max_length=255)
    temperature_sensor = models.CharField(max_length=255)
    humidity_sensor = models.CharField(max_length=255)
    air_speed_sensor = models.CharField(max_length=255)
    ndir_co2_sensor = models.CharField(max_length=255)
    voc_sensor = models.CharField(max_length=255)

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


class Greenhouse(CEA):
    floor_area = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name


class GreenhouseSection(CEA):
    greenhouse = models.ForeignKey(Greenhouse, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    bench_area = models.DecimalField(max_digits=6, decimal_places=2)
    eave_height = models.DecimalField(max_digits=4, decimal_places=2)
    ridge_height = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.greenhouse.name} - {self.name}"

