from django.db import models
from django.contrib.auth import get_user_model
from .itis import TaxonomicUnits


class Plant(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='plants/', null=True, blank=True)
    registration_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    tsn = models.ForeignKey(TaxonomicUnits, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'Plant'
        verbose_name_plural = 'Plants'

    def __str__(self):
        return self.name
