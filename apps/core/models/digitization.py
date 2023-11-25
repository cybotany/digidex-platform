from django.db import models
from apps.inventory.models import Link
from apps.taxonomy.models import Units


class Digitization(models.Model):
    """
    Model to represent the process of converting plant data to a digital format.
    """
    link = models.OneToOneField(
        Link,
        on_delete=models.CASCADE,
        related_name='digitization'
    )
    taxonomic_unit = models.ForeignKey(
        Units,
        on_delete=models.CASCADE,
        related_name='digitizations'
    )

    @property
    def group(self):
        return self.link.group

    def __str__(self):
        return f"{self.link} - {self.taxonomic_unit}"

    class Meta:
        verbose_name = "Digitization"
        verbose_name_plural = "Digitizations"
