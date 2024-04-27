import uuid
from django.utils.text import slugify
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(
        max_length=32,
        unique=True
    )
    slug = models.SlugField(
        unique=True,
        db_index=True,
        verbose_name="Username Slug",
        help_text="Used for it's SEO-friendly properties on the front-end."
    )
    uuid = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        db_index=True,
        verbose_name="User UUID",
        help_text="Used for it's universally unique identifying properties for external users."
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.username)
            original_slug = self.slug
            count = 0

            while User.objects.filter(slug=self.slug).exists():
                count += 1
                self.slug = f'{original_slug}-{count}'

        super(User, self).save(*args, **kwargs)
