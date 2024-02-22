from django.db import models
from django.urls import reverse

from digidex.inventory.models import Digit
from digidex.utils.custom_storage import PublicMediaStorage

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
        is_public (BooleanField): A boolean field to determine if the profile is public or private.
        created_at (DateTimeField): The date and time when the profile was created.
        last_modified (DateTimeField): The date and time when the profile was last modified.
    """
    user = models.OneToOneField(
        'accounts.User',
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
        storage=PublicMediaStorage(), 
        null=True,
        blank=True,
        help_text='The avatar image of the profile.'
    )
    is_public = models.BooleanField(
        default=False,
        help_text='Indicates if the profile should be publicly visible or private.'
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
        return reverse('accounts:profile', kwargs={'username_slug': self.user.username_slug})

    def get_user_digits(self):
        """
        Retrieves all Digit objects associated with the user of this profile.

        Returns:
            QuerySet: A QuerySet of all Digit objects associated with the user.
        """
        return Digit.objects.filter(nfc_link__user=self.user)

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"
