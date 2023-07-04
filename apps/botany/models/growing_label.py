from django.db import models
from django.contrib.auth import get_user_model


class GrowingLabel(models.Model):
    """
    Label model to represent plant labels. Labels can be unique to a user
    or common across the application.

    Fields:
        name (CharField): The name of the label.
        user (ForeignKey): A reference to the user who created the label.
        is_common (BooleanField): Whether this label is common across the application.
    """

    name = models.CharField(
        max_length=50,
        help_text='The name of the label.'
    )
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        help_text='The user who created the label. Null for common labels.',
    )
    is_common = models.BooleanField(
        default=False,
        help_text='Is this a common label.'
    )

    class Meta:
        unique_together = ('name', 'user')
        verbose_name = 'label'
        verbose_name_plural = 'labels'

    @classmethod
    def get_common_labels(cls):
        """
        Class method to get all common labels.

        Returns:
            QuerySet: A QuerySet of common labels.
        """
        return cls.objects.filter(is_common=True)

    @property
    def plants(self):
        """
        Property to get all plants associated with this label that belong to the same user.

        Returns:
            QuerySet: A QuerySet of plants associated with this label belonging to the same user.
        """
        return self.plant_set.filter(user=self.user)

    def __str__(self):
        """
        Returns a string representation of the label.

        Returns:
            str: The name of the label.
        """
        return self.name
