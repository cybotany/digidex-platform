from django.db import models
from django.contrib.auth import get_user_model
from .label import Label


User = get_user_model()


class Plant(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    label = models.ForeignKey(Label, on_delete=models.SET_NULL, null=True)
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
