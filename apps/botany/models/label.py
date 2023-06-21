from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Label(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    is_common = models.BooleanField(default=False)

    class Meta:
        unique_together = (('name', 'user'),)  # label names must be unique per user

    @classmethod
    def get_common_labels(cls):
        return cls.objects.filter(is_common=True)

    @property
    def plants(self):
        return self.plant_set.all()

    def __str__(self):
        return self.name
