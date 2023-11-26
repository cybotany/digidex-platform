from django.db import models
from apps.inventory.models import Link
from apps.taxonomy.models import Unit


class Digit(models.Model):
    """
    Model to represent the process of converting plant data to a digital format.
    """
    link = models.OneToOneField(
        Link,
        on_delete=models.CASCADE,
        related_name='digit'
    )
    taxonomic_unit = models.ForeignKey(
        Unit,
        on_delete=models.CASCADE,
        related_name='digits'
    )

    @property
    def group(self):
        return self.link.group

    def __str__(self):
        return f"{self.link} - {self.taxonomic_unit}"

    class Meta:
        verbose_name = "Digit"
        verbose_name_plural = "Digits"
