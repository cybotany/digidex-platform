import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify


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

    @property
    def page(self):
        if hasattr(self, 'profile'):
            return self.profile.page
        return None

    @property
    def parent_slug(self):
        return 'u'

    @property
    def base_slug(self):
        return slugify(self.username)

    @property
    def full_slug(self):
        return f'{self.parent_slug}/{self.base_slug}'

    @property
    def slug_kwargs(self):
        return {
            'user_slug': self.base_slug
        }

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.full_slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username.title()
