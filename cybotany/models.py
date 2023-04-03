from datetime import datetime
from django.db import models
from django.contrib.auth.models import User


class Plant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='plants/', blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    health_status = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name or f"Plant {self.pk}"