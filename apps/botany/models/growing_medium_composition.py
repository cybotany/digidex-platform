from django.db import models

from .growing_medium import GrowingMedium
from .growing_medium_component import GrowingMediumComponent


class GrowingMediumComposition(models.Model):
    """
    Represents the relationship between a GrowingMedium and a GrowingMediumComponent
    and stores the ratio of that component in the medium.

    Fields:
    """
    growing_medium = models.ForeignKey(
        GrowingMedium,
        on_delete=models.CASCADE,
        blank=False,
        null=False
    )
    component = models.ForeignKey(
        GrowingMediumComponent,
        on_delete=models.CASCADE,
        blank=False,
        null=False
    )
    ratio = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        blank=False,
        null=False
    )
    
    def __str__(self):
        return f"{self.component} ({self.ratio}%) in {self.growing_medium}"