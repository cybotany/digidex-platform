from django.conf import settings
from django.db import models
from django.urls import reverse
from .digit import Plant, Pet

class Grouping(models.Model):
    """
    Model for organizing digitized entities into groups.

    Attributes:
        name (CharField): A human-readable name for the digitized entity.
        description (TextField): A short description of the digitized entity.
        user (ForeignKey): A relationship to the User model.
        created_at (DateTimeField): The date and time when the Digit instance was created.
        last_modified (DateTimeField): The date and time when the Digit instance was last modified.
    """
    name = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        help_text="The name of the group."
    )
    description = models.TextField(
        blank=True,
        null=True,
        help_text="The description of the group."
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='digit_groups',
        on_delete=models.CASCADE,
        help_text="A relationship to the User model."
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Created At",
        help_text="The date and time when the grouping instance was created."
    )
    last_modified = models.DateTimeField(
        auto_now=True,
        verbose_name="Last Modified",
        help_text="The date and time when the grouping instance was last modified."
    )
    class Meta:
        unique_together = ('user', 'name')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """
        Returns the absolute URL to the Grouping's detail page.
        """
        return reverse('inventory:detail-grouping', kwargs={'pk': self.pk})

    def get_user_profile_url(self):
        """
        Returns the URL to the associated user's profile detail page.
        """
        username_slug = self.user.username_slug
        return reverse('accounts:detail-profile', kwargs={'username_slug': username_slug})

    def get_user_plants(self):
        """
        Retrieves all Plant objects associated with the user of this profile.
        """
        return Plant.objects.filter(grouping=self)

    def get_user_pets(self):
        """
        Retrieves all Pet objects associated with the user of this profile.
        """
        return Pet.objects.filter(grouping=self)

    def get_user_digits(self):
        """
        Retrieves all Plant and Pet objects associated with this grouping,
        combining them into a single QuerySet.
        """
        user_plants = self.get_user_plants()
        user_pets = self.get_user_pets()
        return user_plants.union(user_pets)
