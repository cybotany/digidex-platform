from django.db import models
from django.contrib.auth import get_user_model


class BaseCEA(models.Model):
    name = models.CharField(max_length=255)
    identifier = models.CharField(max_length=255)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
