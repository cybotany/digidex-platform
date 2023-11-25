from django.db import models
from django.contrib.auth import get_user_model


class Group(models.Model):
    """
    Group model to represent inventory groupings.

    Attributes:
        name (str): The name of the link.
        user (User): The user of the group.
    """
    name = models.CharField(
        max_length=50,
        unique=True,
        null=False,
        blank=False,
        help_text='The name of the group.'
    )
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        help_text='The user who created the group.',
    )

    class Meta:
        unique_together = ('name', 'user')
        verbose_name = 'group'
        verbose_name_plural = 'groups'
        ordering = ['name']

    @property
    def links(self):
        """
        Property to get all links associated with this group that belong to the same user.
        """
        return self.link_set.filter(group__user=self.user)

    @property
    def current_count(self):
        """
        The current number of unique links in this group.
        """
        return self.links.count()

    def __str__(self):
        """
        Returns a string representation of the group.
        """
        return self.name
