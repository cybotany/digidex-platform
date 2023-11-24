from django.db import models
from django.urls import reverse
from django.db.models import Max, F, ExpressionWrapper, fields
from django.utils import timezone
from django.core.exceptions import ValidationError


class Plant(models.Model):
    """
    Represents a plant owned.

    Attributes:
        name (str): The name of the plant.
        description (str): The description of the plant.
        added_on (datetime): The date and time when the plant was added.
        quantity (int): The quantity of the plant being managed.
    """
    name = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )
    description = models.CharField(
        max_length=200,
        null=True,
        blank=True
    )
    added_on = models.DateTimeField(
        auto_now_add=True
    )
    quantity = models.PositiveIntegerField(
        default=1,
        help_text='The plant quantity.'
    )    

    def __str__(self):
        """
        Returns a string representation of the plant, using its name.
        """
        return self.name

    def get_absolute_url(self):
        """
        Get the URL to view the details of this plant.
        """
        return reverse('botany:describe_plant', args=[str(self.id)])

    def days_since_last_watering(self):
        """
        Returns the number of days since the last watering event for this plant using annotation.
        """
        plant_with_last_watering = Plant.objects.filter(id=self.id).annotate(
            last_watering_timestamp=Max('waterings__timestamp')
        ).first()

        if not plant_with_last_watering or not plant_with_last_watering.last_watering_timestamp:
            return None

        delta = timezone.now() - plant_with_last_watering.last_watering_timestamp
        return delta.days

    def delete(self, *args, **kwargs):
        """
        Custom delete method to deactivate the associated NFC tag before deleting the plant.
        """
        if hasattr(self, 'nfc_tag'):
            tag = self.nfc_tag
            tag.active = False
            tag.save()

        super().delete(*args, **kwargs)
