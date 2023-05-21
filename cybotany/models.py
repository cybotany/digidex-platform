from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


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
    ridge_orientation = models.CharField(max_length=2, choices=[("NS", "North-South"), ("EW", "East-West")])

    def __str__(self):
        return self.name
    

class GreenhouseSection(CEA):
    greenhouse = models.ForeignKey(Greenhouse, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    floor_area = models.DecimalField(max_digits=6, decimal_places=2)
    bench_area = models.DecimalField(max_digits=6, decimal_places=2)
    eave_height = models.DecimalField(max_digits=4, decimal_places=2)
    ridge_height = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.greenhouse.name} - {self.name}"


class GrowingMedium(models.Model):
    TRADITIONAL_CHOICES = [
        ('soil', 'Soil'),
        ('compost', 'Compost'),
        ('peat moss', 'Peat Moss'),
        ('coco coir', 'Coco Coir'),
        ('perlite', 'Perlite'),
        ('vermiculite', 'Vermiculite'),
        ('sand', 'Sand'),
        ('bark', 'Bark'),
        ('other', 'Other'),
    ]
    HYDROPONIC_CHOICES = [
        ('coco coir', 'Coco Coir'),
        ('perlite', 'Perlite'),
        ('vermiculite', 'Vermiculite'),
        ('rockwool', 'Rockwool'),
        ('leca', 'LECA'),
        ('other', 'Other'),
    ]
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    composite_material = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class PropogationMethod(models.Model):
    PROPAGATION_CHOICES = [
        ('cutting', 'Cutting'),
        ('division', 'Division'),
        ('grafting', 'Grafting'),
        ('layering', 'Layering'),
        ('seed', 'Seed'),
        ('storage organs', 'Storage Organs'),
        ('offsets', 'Offsets'),
        ('micropropogation', 'Micropropogation'),
    ]

    propagation_method = models.CharField(max_length=50, choices=PROPAGATION_CHOICES)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Organism(models.Model):
    common_name = models.CharField(max_length=255)
    scientific_name = models.CharField(max_length=255)
    kingdom = models.CharField(max_length=255)
    phylum = models.CharField(max_length=255, blank=True, null=True)
    class_name = models.CharField('class', max_length=255, blank=True, null=True)
    order = models.CharField(max_length=255, blank=True, null=True)
    family = models.CharField(max_length=255, blank=True, null=True)
    genus = models.CharField(max_length=255, blank=True, null=True)
    species = models.CharField(max_length=255, blank=True, null=True)
    itis_tsn = models.IntegerField('ITIS TSN', blank=True, null=True)

    class Meta:
        abstract = True


class Plant(Organism):
    propogation_method = models.ForeignKey(PropogationMethod, on_delete=models.CASCADE)
    growing_medium = models.ForeignKey(GrowingMedium, on_delete=models.CASCADE)


class UserPlant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='plant_pictures/', blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    health_status = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    growing_medium = models.ForeignKey(GrowingMedium, on_delete=models.SET_NULL, blank=True, null=True)
    scientific_name = models.CharField(max_length=100, null=True, blank=True)
    cultivar_name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name or f"Plant {self.pk}"

        # You can add any additional processing or validation here


class PlantImage(models.Model):
    image = models.ImageField(upload_to='plant_images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Plant Image {self.pk}"


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    consent_data_processing = models.BooleanField(default=False)
    email_preferences = models.JSONField(default=dict)
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Ensure the parent class save() method is called
