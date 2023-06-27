from django.db import models
from django.contrib.auth import get_user_model


class UserActivity(models.Model):
    """
    Represents an activity performed by a user.

    Attributes:
        user (ForeignKey): A foreign key reference to the User model.
        activity_type (str): The type of activity performed (e.g., 'created', 'updated', 'deleted').
        content (str): A brief description of the activity.
        timestamp (datetime): The date and time when the activity occurred.
    """

    ACTIVITY_TYPES = [
        ('created', 'Created'),
        ('updated', 'Updated'),
        ('deleted', 'Deleted'),
    ]

    user = models.ForeignKey(
        get_user_model(),
        related_name='recent_activities',
        on_delete=models.CASCADE
    )
    activity_type = models.CharField(
        max_length=20,
        choices=ACTIVITY_TYPES
    )
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        Returns a string representation of the user activity.
        """
        return f"{self.user.username} {self.activity_type} a plant - {self.timestamp}"

    class Meta:
        ordering = ['-timestamp']
