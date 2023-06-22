
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

from .label import Label

User = get_user_model()


class Plant(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    label = models.ForeignKey(Label, on_delete=models.SET_NULL, null=True)
    common_names = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    added_on = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.name:
            total_plants = Plant.objects.filter(owner=self.owner).count()
            self.name = f'Plant-{total_plants + 1}'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('describe_plant', args=[str(self.id)])
