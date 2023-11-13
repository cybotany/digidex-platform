from django.db import models
from django.utils import timezone
from apps.botany.models import Plant


class PlantWatering(models.Model):
    """
    Represents a watering event for a plant.

    Attributes:
        plant (ForeignKey): The plant associated with this watering event.
        watered (BooleanField): Whether the plant was watered.
        timestamp (DateTimeField): The date and time when the plant was watered.
        duration_since_last_watering (DurationField): Duration since the last watering event.
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

    duration_since_last_watering = models.DurationField(
        null=True,
        blank=True,
        help_text="Duration since the last watering event."
    )

    def save(self, *args, **kwargs):
        """
        Override the save method to calculate the duration since the last watering event.
        """
        last_watering = PlantWatering.objects.filter(plant=self.plant).order_by('-timestamp').first()
        if last_watering:
            self.duration_since_last_watering = self.timestamp - last_watering.timestamp
        super().save(*args, **kwargs)

    def __str__(self):
        """
        Returns a string representation of the watering event,
        indicating which plant it is associated with and when it occurred.

        Returns:
            str: A string representation of the plant watering event.
        """
        return f'Watering for {self.plant.name} on {self.timestamp}'
