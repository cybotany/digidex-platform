from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


# Base Models for inheritance
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
    growth_habit = models.CharField(max_length=255)


class Animal(Organism):
    diet = models.CharField(max_length=255)


class UserPlant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='plant_pictures/', blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    health_status = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    growing_medium = models.ForeignKey(GrowingMedium, on_delete=models.SET_NULL, blank=True, null=True)
    experiment = models.ForeignKey(Experiment, on_delete=models.SET_NULL, null=True)
    scientific_name = models.CharField(max_length=100, null=True, blank=True)
    cultivar_name = models.CharField(max_length=100, null=True, blank=True)


    def __str__(self):
        return self.name or f"Plant {self.pk}"

        # You can add any additional processing or validation here


class Experiment(models.Model):
    title = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    # Add any other common attributes for experiments here

    # New field
    peer_reviewed_publication = models.BooleanField(default=False)

    class Meta:
        abstract = True


class UserExperiment(Experiment):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_plant = models.ForeignKey(UserPlant, on_delete=models.CASCADE)
    # Add any user-specific experiment attributes here


class CEA(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)

    class Meta:
        abstract = True


class Greenhouse(CEA):
    floor_area = models.DecimalField(max_digits=6, decimal_places=2)
    ridge_orientation = models.CharField(max_length=2, choices=[("NS", "North-South"), ("EW", "East-West")])

    def __str__(self):
        return self.name


class GrowthChamber(CEA):
    chamber_volume = models.DecimalField(max_digits=6, decimal_places=2)


class TissueCultureFacility(CEA):
    facility_area = models.DecimalField(max_digits=6, decimal_places=2)


class GreenhouseSection(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    cea = GenericForeignKey('content_type', 'object_id')
    name = models.CharField(max_length=100)
    floor_area = models.DecimalField(max_digits=6, decimal_places=2)
    bench_area = models.DecimalField(max_digits=6, decimal_places=2)
    eave_height = models.DecimalField(max_digits=4, decimal_places=2)
    ridge_height = models.DecimalField(max_digits=4, decimal_places=2)
    # ... other fields ...

    def __str__(self):
        return f"{self.greenhouse.name} - {self.name}"


class GrowingMedium(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    water_retention = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, help_text='Percentage of water retention capacity')
    air_porosity = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, help_text='Percentage of air porosity')
    ph_range = models.CharField(max_length=50, blank=True, null=True, help_text='Range of pH values, e.g., "5.5-6.5"')
    bulk_density = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, help_text='Bulk density in g/cm³')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class PlantImage(models.Model):
    image = models.ImageField(upload_to='plant_images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Plant Image {self.pk}"


# Fact tables (central tables with quantitative data)
class UserPlantLog(models.Model):
    user_plant = models.ForeignKey(UserPlant, on_delete=models.CASCADE)
    log_type = models.CharField(max_length=100)
    date = models.DateField()
    notes = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"{self.user_plant.nickname} {self.log_type} on {self.date}"
    

class UserCEA(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    cea = GenericForeignKey('content_type', 'object_id')
    role = models.CharField(max_length=50, choices=[("owner", "Owner"), ("researcher", "Researcher"), ("assistant", "Assistant")])

    def __str__(self):
        return f"{self.user.username} - {self.cea} - {self.role}"


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

        # You can add any additional processing or validation here