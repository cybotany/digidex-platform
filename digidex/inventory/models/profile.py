from django.conf import settings
from django.db import models
from django.urls import reverse

from digidex.inventory.models import grouping as digit_grouping
from digidex.utils import custom_storage

def profile_avatar_directory_path(instance, filename):
    return f'profile_{instance.id}/avatar.jpeg'


class Profile(models.Model):
    """
    User profile model for storing additional user information.

    Fields:
        user (OneToOneField): A one-to-one reference to the User model.
        bio (TextField): A text field for user biography, maximum length 500 characters.
        location (CharField): A char field for user location, maximum length 30 characters.
        avatar (ImageField): An image field for user's profile picture.
        is_public (BooleanField): A boolean field to determine if the profile is public or private. Profile is private by default.
        created_at (DateTimeField): The date and time when the profile was created.
        last_modified (DateTimeField): The date and time when the profile was last modified.
    """
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        help_text='The user associated with this profile.'
    )
    bio = models.TextField(
        max_length=500,
        blank=True,
        help_text='A short biography of the user.'
    )
    location = models.CharField(
        max_length=30,
        blank=True,
        help_text='The location of the user.'
    )
    avatar = models.ImageField(
        upload_to=profile_avatar_directory_path,
        storage=custom_storage.PublicMediaStorage(), 
        null=True,
        blank=True,
        help_text='The avatar image of the profile.'
    )
    is_public = models.BooleanField(
        default=False,
        help_text='Indicates if the profile should be publicly visible to the public or private. Profile is private by default.'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Created At",
        help_text="The date and time when the profile was created."
    )
    last_modified = models.DateTimeField(
        auto_now=True,
        verbose_name="Last Modified",
        help_text="The date and time when the profile was last modified."
    )

    def __str__(self):
        """
        Returns a string representation of the user's profile.

        Returns:
            str: A string in the format "<username>'s Profile".
        """
        return f"{self.user.username}'s Profile"

    def get_absolute_url(self):
        """
        Get the URL to view the details of this profile.

        Returns:
            str: The URL to view the details of this profile.
        """
        return reverse('inventory:detail-profile', kwargs={'user_slug': self.user.slug})

    def get_default_digits(self):
        """
        Retrieves the default Grouping object for the user (marked with is_default=True),
        including prefetched related plants and pets, and all other Grouping objects 
        associated with the user without prefetching related objects for them.

        Returns:
            dict: A dictionary with 'default_grouping' for the default grouping object (or None if not set),
                and 'other_groupings' for a list of all other grouping objects associated with the user.
        """
        grouping = digit_grouping.Grouping.objects.filter(user=self.user, is_default=True)\
            .prefetch_related('plants', 'pets').first()

        if not grouping:
            return {
                'plants': {'items': [], 'count': 0},
                'pets': {'items': [], 'count': 0},
            }
        return grouping.get_digits()

    def get_groupings(self):
        """
        Retrieves the default Grouping object for the user (marked with is_default=True),
        including prefetched related plants and pets, and all other Grouping objects 
        associated with the user without prefetching related objects for them.

        Returns:
            dict: A dictionary with 'default_grouping' for the default grouping object (or None if not set),
                and 'other_groupings' for a list of all other grouping objects associated with the user.
        """
        groupings = digit_grouping.Grouping.objects.filter(user=self.user, is_default=False).all()
        return {
            'groupings': groupings,
            'grouping_count': groupings.count(),
        }

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"
