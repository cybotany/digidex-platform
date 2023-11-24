from django.db import models
from django.contrib.auth import get_user_model
from apps.utils.constants import ACTIVITY_STATUS, ACTIVITY_TYPE


class Activity(models.Model):
    """
    Represents an activity performed by a user. Should be upated whenever a user creates, updates, or deletes a plant.

    Attributes:
        user (ForeignKey): A foreign key reference to the User model.
        activity_type (str): The account type (e.g., 'plant', 'cea').
        activity_status (str): The status of activity performed (e.g., 'created', 'updated', 'deleted').
        content (str): A brief description of the activity.
        timestamp (datetime): The date and time when the activity occurred.
    """

    user = models.ForeignKey(
        get_user_model(),
        related_name='recent_activities',
        on_delete=models.CASCADE
    )
    activity_status = models.CharField(
        max_length=20,
        choices=ACTIVITY_STATUS
    )
    activity_type = models.CharField(
        max_length=25,
        choices=ACTIVITY_TYPE
    )
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        """
        Override the save method to set a default content if not provided.
        """
        if not self.content:
            self.content = f"{self.user.username} {self.activity_status} a {self.activity_type}"
        super().save(*args, **kwargs)

    def __str__(self):
        """
        Returns a string representation of the user activity.
        """
        return self.content

    class Meta:
        ordering = ['-timestamp']
