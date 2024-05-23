import uuid
from django.apps import apps
from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class UserParty(models.Model):
    uuid = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False,
        db_index=True,
        verbose_name="Digitized Object UUID"
    )
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='party'
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    last_modified = models.DateTimeField(
        auto_now=True
    )

    @property
    def profile(self):
        UserProfile = apps.get_model('profiles', 'UserProfile')
        user_profile = UserProfile.objects.get(user=self.user)
        return user_profile

    @property
    def profile_page(self):
        return self.profile.get_profile_page()

    @property
    def username(self):
        return self.user.username

    @property
    def _username(self):
        return self.username.title()
