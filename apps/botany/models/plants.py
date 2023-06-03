from django.db import models
from django.contrib.auth.models import User


class Plant(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    gbif_id = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='plant_images', blank=True)
    propogation = models.TextField()
    common_name = models.CharField(max_length=150, blank=True)
    scientific_name = models.CharField(max_length=150, blank=True)
    taxonomy = models.TextField()
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
