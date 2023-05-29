from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=255)
    avatar = models.ImageField(upload_to='avatars/', blank=True)
    bio = models.TextField(blank=True)
    facebook_url = models.URLField(max_length=200, blank=True)
    twitter_url = models.URLField(max_length=200, blank=True)
    linkedin_url = models.URLField(max_length=200, blank=True)
    tiktok_url = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Sensor(models.Model):
    SENSOR_TYPE_CHOICES = [
        ('temp', 'Temperature'),
        ('humidity', 'Humidity'),
        ('light', 'Light'),
        ('voc', 'Air Quality'),
    ]
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=10, choices=SENSOR_TYPE_CHOICES)
    description = models.TextField()
    min_value = models.DecimalField(max_digits=6, decimal_places=2)
    max_value = models.DecimalField(max_digits=6, decimal_places=2)
    value_unit = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Instrument(models.Model):
    INSTRUMENT_TYPE_CHOICES = [
        ('camera', 'Camera'),
        ('light', 'Light'),
        ('fan', 'Fan'),
    ]
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=10, choices=INSTRUMENT_TYPE_CHOICES)
    description = models.TextField()

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
