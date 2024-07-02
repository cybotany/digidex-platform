import uuid

from django.db import models

from wagtail.models import Collection


class InventoryCategory(models.Model):
    uuid = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False,
        db_index=True
    )
    slug = models.SlugField(
        max_length=100,
        blank=False,
        null=False
    )
    collection = models.ForeignKey(
        Collection,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    owner = models.ForeignKey(
        'UserProfile',
        on_delete=models.CASCADE,
        related_name='inventory_categories'
    )
    name = models.CharField(
        max_length=100,
        blank=False,
        null=False
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

    def __str__(self):
        return f"Inventory Category: {self.name}"
