import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser

from wagtail.models import Collection


class User(AbstractUser):
    uuid = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False,
        db_index=True,
        verbose_name="User UUID"
    )
    slug = models.SlugField(
        unique=True,
        db_index=True,
        max_length=255,
        verbose_name="User Slug"
    )
    collection = models.ForeignKey(
        Collection,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='+'
    )

    @property
    def formatted_date(self):
        return self.date_joined.strftime('%B %d, %Y')
    
    @property
    def formatted_name(self):
        return self.username.title()

    def __str__(self):
        return f"User: {self.formatted_name}"
