from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Label(models.Model):
    name = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    @property
    def plants(self):
        return self.plant_set.all()
