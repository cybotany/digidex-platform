from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

from .label import Label


class Plant(models.Model):
    """
    Represents a plant owned by a user.

    Attributes:
        name (str): The name of the plant.
        label (Label): The label associated with the plant.
        description (str): The description of the plant.
        user (User): The user who owns the plant.
        added_on (datetime): The date and time when the plant was added.
    """

    name = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )
    label = models.ForeignKey(
        Label,
        on_delete=models.SET_NULL,
        null=True
    )
    description = models.TextField(
        null=True,
        blank=True
    )
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    added_on = models.DateTimeField(
        auto_now_add=True
    )

    def save(self, *args, **kwargs):
        """
        Override the save method to set a default name if not provided.
        """
        if not self.name:
            total_plants = Plant.objects.filter(user=self.user).count()
            self.name = f'Plant-{total_plants + 1}'
        super().save(*args, **kwargs)

    def __str__(self):
        """
        Returns a string representation of the plant, using its name.

        Returns:
            str: A string representation of the plant.
        """
        return self.name

    def get_absolute_url(self):
        """
        Get the URL to view the details of this plant.

        Returns:
            str: The URL to view the details of this plant.
        """
        return reverse('botany:describe_plant', args=[str(self.id)])
