from django.db import models
from .base_cea import BaseCEA


class Greenhouse(BaseCEA):
    location = models.CharField(max_length=200)
