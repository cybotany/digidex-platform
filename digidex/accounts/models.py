import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser

from base.models import AbstractIndexPage


class DigiDexUser(AbstractUser):
    uuid = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False,
        db_index=True,
        verbose_name="User UUID"
    )

    def __str__(self):
        return f"DigiDex User: {self.username}"


class AccountPage(AbstractIndexPage):
    class Meta:
        verbose_name = 'account page'
