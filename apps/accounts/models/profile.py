from django.db import models
from django.contrib.auth import get_user_model
from apps.utils.helpers import get_user_directory_path
from apps.utils.custom_storage import AvatarStorage
from apps.utils.validators import validate_image_size_and_dimensions


class Profile(models.Model):
    """
    User profile model for storing additional user information.

    Fields:
        user (OneToOneField): A one-to-one reference to the User model.
        email_confirmed (BooleanField): Indicates whether the user has confirmed their email address.
        bio (TextField): A text field for user biography, maximum length 500 characters.
        location (CharField): A char field for user location, maximum length 30 characters.
        birth_date (DateField): A date field for user's birth date.
        avatar (ImageField): An image field for user's profile picture.
        interests (CharField): A char field for user's interests.
        experience (CharField): A char field for user's experience.
        created_at (DateTimeField): The date and time when the profile was created.
        last_modified (DateTimeField): The date and time when the profile was last modified.
    """
    user = models.OneToOneField(
        get_user_model(),
        on_delete=models.CASCADE,
        help_text='The user associated with this profile.'
    )
    email_confirmed = models.BooleanField(
        default=False,
        help_text='Indicates whether the user has confirmed their email address.'
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
    birth_date = models.DateField(
        null=True,
        blank=True,
        help_text='The birth date of the user.'
    )
    avatar = models.ImageField(
        upload_to=AvatarStorage(get_user_directory_path),
        validators=[validate_image_size_and_dimensions],
        null=True,
        blank=True,
        help_text='The profile picture of the user.'
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

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"
