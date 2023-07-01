from django.db import models

from .growing_method import GrowingMethod


class GrowingMedium(models.Model):
    name = models.CharField(max_length=100)
    growing_methods = models.ManyToManyField(GrowingMethod, related_name="growing_mediums")
