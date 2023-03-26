from django.db import models
from django.core.files.base import ContentFile


class Plant(models.Model):
    name = models.CharField(max_length=50, default='')
