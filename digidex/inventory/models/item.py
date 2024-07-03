from django.db import models

from .base import BaseInventory
from .category import InventoryCategory


class InventoryItem(BaseInventory):
    category = models.ForeignKey(
        InventoryCategory,
        on_delete=models.CASCADE,
        related_name='items'
    )
