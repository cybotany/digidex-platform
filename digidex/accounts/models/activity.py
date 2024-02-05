from django.db import models


class Activity(models.Model):
    """
    Represents an activity performed by a user, such as creating, updating, or deleting an item (e.g., a plant).
    
    Attributes:
        user (ForeignKey): Reference to the user who performed the activity.
        last_active (DateTimeField): The date and time when the activity was recorded.

    Methods:
        __str__: Returns a string representation of the activity.
    """

    user = models.ForeignKey(
        'accounts.User',
        related_name='recent_activities',
        on_delete=models.CASCADE,
        help_text='Reference to the user who performed the activity.'
    )
    last_active = models.DateTimeField(
        auto_now_add=True,
        help_text='The date and time when the activity was recorded.'
    )

    def __str__(self):
        return f"{self.user.username} - Last Active: {self.last_active}"
