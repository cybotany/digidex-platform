import uuid

from django.conf import settings
from django.db import models

from wagtail.models import Collection


class Entity(models.Model):
    uuid = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False,
        db_index=True
    )
    slug = models.SlugField(
        max_length=100,
        blank=True,
        null=True
    )
    owner = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="entity_owner",
        null=True,
        blank=True
    )
    name =  models.CharField(
        max_length=100,
        blank=True,
        null=True
    )
    description = models.TextField(
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    last_modified = models.DateTimeField(
        auto_now=True
    )


class UserProfile(Entity):
    class Meta:
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'


class InventoryCategory(Entity):
    class Meta:
        verbose_name = 'Inventory Category'
        verbose_name_plural = 'Inventory Categories'


class InventoryItem(Entity):
    class Meta:
        verbose_name = 'Inventory Item'
        verbose_name_plural = 'Inventory Items'


class InventoryCategoryCollection(Collection):
    category = models.OneToOneField(
        InventoryCategory,
        on_delete=models.CASCADE,
        related_name="collection"
    )
