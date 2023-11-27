from django.db import models
from django.contrib.auth import get_user_model

class Group(models.Model):
    """
    Represents a grouping of digitized plants in the inventory system.

    Each group is created by a user and can contain multiple digitized plants (Digits). 
    Groups are used to categorize or organize digitized plants based on criteria set by the user, 
    such as plant type, location, or any other user-defined classification.

    Attributes:
        name (CharField): The name of the group, uniquely identifying it.
        user (ForeignKey): The user who created and owns the group.
    """

    name = models.CharField(
        max_length=50,
        unique=True,
        null=False,
        blank=False,
        help_text='The unique name identifying the group.'
    )
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        help_text='The user who created and owns the group.',
        related_name='groupings'
    )

    class Meta:
        unique_together = ('name', 'user')
        verbose_name = 'Group'
        verbose_name_plural = 'Groups'
        ordering = ['name']

    @property
    def digits(self):
        """
        Retrieves all digitized plants associated with this group.

        This property allows for easy access to all Digit instances that belong to this group, 
        providing a way to view and manage grouped digitized plants.

        Returns:
            QuerySet: A QuerySet of Digit instances associated with this group.
        """
        return self.digits_set.all()

    @property
    def current_count(self):
        """
        Calculates the current number of digitized plants in this group.

        Returns:
            int: The count of Digit instances associated with this group.
        """
        return self.digits.count()

    def __str__(self):
        """
        Returns a string representation of the group, using its name.

        Returns:
            str: A string representation of the group.
        """
        return self.name
