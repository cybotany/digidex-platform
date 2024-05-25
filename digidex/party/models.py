import uuid
from django.db import models
from django.conf import settings


class UserParty(models.Model):
    uuid = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False,
        db_index=True,
        verbose_name="Digitized Object UUID"
    )
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="party"
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    last_modified = models.DateTimeField(
        auto_now=True
    )


class UserPartyDigit(models.Model):
    user_party = models.ForeignKey(
        'party.UserParty',
        on_delete=models.CASCADE,
        related_name="digits"
    )
    digit = models.ForeignKey(
        'digitization.DigitalObject',
        on_delete=models.CASCADE,
        related_name="party"
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    last_modified = models.DateTimeField(
        auto_now=True
    )
