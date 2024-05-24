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
    def user_profile(self):
        if hasattr(self, 'profile'):
            return self.profile
        return None

    @property
    def user_inventory(self):
        if hasattr(self, 'inventory'):
            return self.inventory
        return None

    @property
    def user_party(self):
        if hasattr(self, 'party'):
            return self.party
        return None

    @property
    def _username(self):
        return self.username.title()