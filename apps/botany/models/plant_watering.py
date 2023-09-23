from django.db import models
from django.utils import timezone
from .plant import Plant


class PlantWatering(models.Model):
    """
    Represents a watering event for a plant.

    Attributes:
        plant (ForeignKey): The plant associated with this watering event.
        watered (BooleanField): Whether the plant was watered.
        timestamp (DateTimeField): The date and time when the plant was watered.
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

    timestamp = models.DateTimeField(
        default=timezone.now,
        help_text="The date and time when the plant was watered."
    )

    def __str__(self):
        """
        Returns a string representation of the watering event,
        indicating which plant it is associated with and when it occurred.

        Returns:
            str: A string representation of the plant watering event.
        """
        return f'Watering for {self.plant.name} on {self.timestamp}'