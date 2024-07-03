import uuid

from django.conf import settings
from django.db import models
from wagtail.models import Collection


class BaseInventory(Collection):
    uuid = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False,
        db_index=True
    )
    name = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )
    description = models.TextField(
        blank=True,
        null=True
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='owner'
    )
    slug = models.SlugField(
        max_length=100,
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    last_modified = models.DateTimeField(
        auto_now=True
    )
