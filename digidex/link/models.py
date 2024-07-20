from django.db import models

from inventory.models import Inventory, InventoryTag


class InventoryLink(models.Model):
    inventory = models.OneToOneField(
        Inventory,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='+'
    )
    tag = models.OneToOneField(
        InventoryTag,
        on_delete=models.CASCADE,
        related_name='link'
    )

    def __str__(self):
        if self.inventory:
            return f"{self.tag} -> {self.inventory}"
        return str(self.tag)

    def get_url(self):
        if self.inventory:
            return self.inventory.url
        return None

    @property
    def url(self):
        return self.get_url()
