from django.db import models
from django.utils import timezone
from apps.botany.models import Plant


class PlantFertilization(models.Model):
    """
    Represents a fertilization event for a plant.

    Attributes:
        plant (ForeignKey): The plant associated with this fertilization event.
        fertilized (BooleanField): Whether the plant was fertilized.
        timestamp (DateTimeField): The date and time when the plant was fertilized.
        duration_since_last_fertilization (DurationField): Duration since the last fertilization event.
    """

    plant = models.ForeignKey(
        Plant,
        related_name='fertilizations',
        on_delete=models.CASCADE,
        help_text="The plant associated with this fertilization event."
    )

    fertilized = models.BooleanField(
        default=False,
        help_text="Whether the plant was fertilized."
    )

    timestamp = models.DateTimeField(
        default=timezone.now,
        help_text="The date and time when the plant was fertilized."
    )

    duration_since_last_fertilization = models.DurationField(
        null=True,
        blank=True,
        help_text="Duration since the last fertilization event."
    )

    def save(self, *args, **kwargs):
        """
        Override the save method to calculate the duration since the last fertilization event.
        """
        last_fertilization = PlantFertilization.objects.filter(plant=self.plant).order_by('-timestamp').first()
        if last_fertilization:
            self.duration_since_last_fertilization = self.timestamp - last_fertilization.timestamp
        super().save(*args, **kwargs)

    def __str__(self):
        """
        Returns a string representation of the fertilization event,
        indicating which plant it is associated with and when it occurred.

        Returns:
            str: A string representation of the plant fertilization event.
        """
        return f'Fertilization for {self.plant.name} on {self.timestamp}'
