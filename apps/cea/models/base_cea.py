from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone


User = get_user_model()

class BaseCEA(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, default=timezone.now)

    class Meta:
        abstract = True
