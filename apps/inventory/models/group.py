from django.db import models
from django.contrib.auth import get_user_model
from apps.utils.constants import MAX_GROUP_CAPACITY 


class Group(models.Model):
    """
    Group model to represent inventory groupings.

    Fields:
        name (CharField): The name of the group.
        user (ForeignKey): A reference to the user who created the group.
    """
    name = models.CharField(
        max_length=50,
        unique=True,
        help_text='The name of the group.'
    )
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        help_text='The user who created the group.',
    )

    class Meta:
        verbose_name = 'group'
        verbose_name_plural = 'groups'
        ordering = ['name']

    @property
    def links(self):
        """
        Property to get all resources associated with this group that belong to the same user.

        Returns:
            QuerySet: A QuerySet of plants associated with this group belonging to the same user.
        """
        return self.link_set.filter(user=self.user)

    @property
    def current_count(self):
        """
        The current number of unique links in this group.

        Returns:
            int: The number of unique links in this group.
        """
        return self.links.distinct().count()

    @property
    def is_full(self):
        return self.current_count >= MAX_GROUP_CAPACITY

    def __str__(self):
        """
        Returns a string representation of the group.

        Returns:
            str: The name of the group.
        """
        return self.name
