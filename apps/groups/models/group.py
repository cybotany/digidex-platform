from django.db import models
from django.contrib.auth import get_user_model
from apps.utils.constants import MAX_GROUP_CAPACITY 


class Group(models.Model):
    """
    Group model to represent various plant groups.

    Fields:
        name (CharField): The name of the group.
        user (ForeignKey): A reference to the user who created the group.
        position (PositiveIntegerField): The position/order of the group.
    """
    name = models.CharField(
        max_length=50,
        help_text='The name of the group.'
    )
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        help_text='The user who created the group.',
    )
    position = models.PositiveIntegerField(
        help_text="The position/order of the group."
    )

    class Meta:
        unique_together = (('name', 'user'), ('position', 'user'))
        verbose_name = 'group'
        verbose_name_plural = 'groups'
        ordering = ['position']

    @property
    def plants(self):
        """
        Property to get all plants associated with this group that belong to the same user.

        Returns:
            QuerySet: A QuerySet of plants associated with this group belonging to the same user.
        """
        return self.plant_set.filter(user=self.user)

    @property
    def current_count(self):
        """
        The current number of unique plants in this group.

        Returns:
            int: The number of unique plants in this group.
        """
        return self.plants.distinct().count()

    @property
    def is_full(self):
        return self.current_count >= MAX_GROUP_CAPACITY

    def display_name_with_count(self):
        """
        Returns the group name alongside its current_count in parentheses.

        Returns:
            str: The name of the group with its current_count in parentheses.
        """
        return f"{self.name} ({self.current_count})"

    def __str__(self):
        """
        Returns a string representation of the group.

        Returns:
            str: The name of the group.
        """
        return self.name
