import uuid
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
