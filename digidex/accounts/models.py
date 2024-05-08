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
        max_length=255,
        verbose_name="User Slug"
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.username)
            unique_slug = base_slug
            num = 1
            while User.objects.filter(slug=unique_slug).exists():
                unique_slug = f'{base_slug}-{num}'
                num += 1
            self.slug = unique_slug
        super(User, self).save(*args, **kwargs)
