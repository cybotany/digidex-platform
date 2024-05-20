import uuid
from django.db import models


class UserParty(models.Model):
    uuid = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False,
        db_index=True,
        verbose_name="Digitized Object UUID"
    )
    profile_page = models.OneToOneField(
        'profiles.UserProfilePage',
        on_delete=models.CASCADE,
        related_name='inventories'
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    last_modified = models.DateTimeField(
        auto_now=True
    )

    @property
    def profile(self):
        return self.profile_page.profile

    @property
    def user(self):
        return self.profile.user

    @property
    def username(self):
        return self.user.username

    @property
    def _username(self):
        return self.username.title()
