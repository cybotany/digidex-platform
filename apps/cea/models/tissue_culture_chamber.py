from django.db import models
from .base_cea import BaseCEA


class TissueCultureChamber(BaseCEA):
    column1 = models.CharField(max_length=2)