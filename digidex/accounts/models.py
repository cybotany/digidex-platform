import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    uuid = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False,
        db_index=True,
        verbose_name="User UUID"
    )

    @property
    def _username(self):
        return self.username.title()

    def get_party_digits(self):
        if hasattr(self, 'party'):
            return self.party.get_all_digits()
        return None
