from django.db import models
from .plant import Plant


class PlantWatering(models.Model):
    """
    Represents a watering event for a plant.

    Attributes:
        plant (ForeignKey): The plant associated with this watering event.
        watered (BooleanField): Whether the plant was watered.
        watering_date (DateField): The date when the plant was watered.
        notes (TextField): Optional notes about the watering event.
    """

    plant = models.ForeignKey(
        Plant,
        related_name='waterings',
        on_delete=models.CASCADE,
        help_text="The plant associated with this watering event."
    )

    watered = models.BooleanField(
        default=False,
        help_text="Whether the plant was watered."
    )

    watering_date = models.DateField(
        help_text="The date when the plant was watered."
    )

    notes = models.TextField(
        blank=True,
        help_text="Optional notes about the watering event."
    )

    def __str__(self):
        """
        Returns a string representation of the watering event,
        indicating which plant it is associated with and when it occurred.

        Returns:
            str: A string representation of the plant watering event.
        """
        return f'Watering for {self.plant.name} on {self.watering_date}'