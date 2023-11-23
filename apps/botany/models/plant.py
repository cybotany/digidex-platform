from django.db import models
from django.urls import reverse
from django.db.models import Max, F, ExpressionWrapper, fields
from django.utils import timezone
from django.core.exceptions import ValidationError
from apps.itis.models import TaxonomicUnits
from apps.botany.models import Group


class Plant(models.Model):
    """
    Represents a plant owned.

    Attributes:
        name (str): The name of the plant.
        description (str): The description of the plant.
        added_on (datetime): The date and time when the plant was added.
        quantity (int): The quantity of the plant being managed.
        tsn (int): The TSN (Taxonomic Serial Number) of the plant.
        group (int): The grouping of the plant.
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
    tsn = models.ForeignKey(
        TaxonomicUnits,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text='The TSN (Taxonomic Serial Number) of the plant.',
        related_name='plants'
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="plants",
    )

    def save(self, *args, **kwargs):
        """
        Override the save method to:
         - Handle group count incrementation/decrementation.
        """
        if self.group:
            if self.group.is_full:
                raise ValidationError("The selected group is full!")
        
        # If the plant has changed groups, decrement the count in the old group
        old_group = Plant.objects.filter(pk=self.pk).first().group if self.pk else None
        if old_group and old_group != self.group:
            old_group.current_count -= 1
            old_group.save()

        # If the plant is newly associated with a group or has changed groups, increment the new group's count
        if not old_group or (old_group and old_group != self.group):
            self.group.current_count += 1
            self.group.save()        
        
        super().save(*args, **kwargs)
        

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
