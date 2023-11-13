from django.db import models
from django.utils import timezone
from apps.botany.models import Plant


class PlantJournaling(models.Model):
    """
    Represents a journal entry for a plant owned by a user.

    Attributes:
        plant (ForeignKey): Reference to the Plant this entry is about.
        timestamp (DateTimeField): The date and time when the journal entry was made.
        notes (TextField): Notes or details about the plant at the time of the journal entry.
    """
    plant = models.ForeignKey(
        Plant,
        on_delete=models.CASCADE,
        related_name='journal_entries'
    )
    timestamp = models.DateTimeField(
        auto_now_add=True,
        help_text='The date and time when the journal entry was made.'
    )
    notes = models.TextField(
        help_text='Notes or details about the plant.'
    )

    def __str__(self):
        """
        Returns a string representation of the journal entry.

        Returns:
            str: A string representation of the journal entry, including the plant name and entry date.
        """
        return f'{self.plant.name} - {self.timestamp.strftime("%Y-%m-%d %H:%M")}'

    class Meta:
        ordering = ['timestamp']
