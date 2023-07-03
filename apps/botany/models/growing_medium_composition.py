from django.db import models

from .growing_medium import GrowingMedium
from .growing_medium_component import GrowingMediumComponent


class GrowingMediumComposition(models.Model):
    """
    Represents the relationship between a GrowingMedium and a GrowingMediumComponent
    and stores the ratio of that component in the medium.

    Fields:
        growing_medium (ForeignKey): A reference to the GrowingMedium model, representing
            the growing medium in which the component is used. This field cannot be blank
            or null and will cascade on deletion.
        growing_medium_component (ForeignKey): A reference to the GrowingMediumComponent model,
            representing the component used in the growing medium. This field cannot be blank
            or null and will cascade on deletion.
        percentage (DecimalField): A decimal field representing the percentage of the 
            growing_medium_component in the growing_medium. This field cannot be blank or null,
            has a maximum of 5 digits and 2 decimal places.
    """
    growing_medium = models.ForeignKey(
        GrowingMedium,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        help_text='Reference to the growing medium in which the component is used.'
    )
    growing_medium_component = models.ForeignKey(
        GrowingMediumComponent,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        help_text='Reference to the component used in the growing medium.'
    )
    percentage = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        blank=False,
        null=False,
        help_text='Percentage of the component in the growing medium.'
    )

    def __str__(self):
        return f"{self.growing_medium_component} ({self.percentage}%) in {self.growing_medium}"
