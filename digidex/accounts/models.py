import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser

from base.models.body import BasePage

class User(AbstractUser):
    username = models.CharField(
        max_length=32
    )
    slug = models.SlugField(
        unique=True,
        verbose_name="User Slug",
        help_text="Used for it's SEO-friendly properties on the front-end."
    )
    uuid = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        db_index=True,
        verbose_name="User UUID",
        help_text="Used for it's universally unique identifying properties for external users."
    )

class AccountIndexPage(BasePage):
    pass

class AccountPage(BasePage):
    pass
