from django.db import models
from accounts.models import User
from utils.constants import ACTIVITY_STATUS, ACTIVITY_TYPE


class Activity(models.Model):
    """
    Represents an activity performed by a user, such as creating, updating, or deleting an item (e.g., a plant).
    
    Attributes:
        user (ForeignKey): A reference to the User model, indicating which user performed the activity.
        activity_type (CharField): Describes the type of item involved in the activity. The type is limited to 
                                   predefined choices, such as 'plant' or 'cea'.
        activity_status (CharField): Indicates the nature of the activity (e.g., 'created', 'updated', 'deleted'). 
                                     This field uses predefined choices.
        content (TextField): A brief textual description of the activity, detailing what was done.
        timestamp (DateTimeField): Records the date and time when the activity occurred, automatically set to the 
                                   current time when the activity is created.

    Methods:
        save: Overrides the save method to automatically set the content field if it is not provided.
        __str__: Returns a string representation of the activity, which is the content of the activity.
    """

    user = models.ForeignKey(
        User,
        related_name='recent_activities',
        on_delete=models.CASCADE,
        help_text='Reference to the user who performed the activity.'
    )
    activity_type = models.CharField(
        max_length=25,
        choices=ACTIVITY_TYPE,
        help_text='Type of the item involved in the activity, such as "plant" or "cea".'
    )
    activity_status = models.CharField(
        max_length=20,
        choices=ACTIVITY_STATUS,
        help_text='Nature of the activity (e.g., "created", "updated", "deleted").'
    )
    content = models.TextField(
        help_text='Detailed description of the activity.'
    )
    timestamp = models.DateTimeField(
        auto_now_add=True,
        help_text='The date and time when the activity was recorded.'
    )

    def save(self, *args, **kwargs):
        """
        Overrides the save method of the model. If content is not provided, it sets a default content 
        based on the user's username, activity status, and type.
        """
        if not self.content:
            self.content = f"{self.user.username} {self.activity_status} a {self.activity_type}"
        super().save(*args, **kwargs)

    def __str__(self):
        """
        Returns a string representation of the user activity, which is primarily the content of the activity.
        """
        return self.content

    class Meta:
        ordering = ['-timestamp']
