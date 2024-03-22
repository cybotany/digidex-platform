from logging import getLogger
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.conf import settings
# Project specific imports
from base.utils import storage
from base.fields import django_fields as _dfields

logger = getLogger(__name__)

def profile_avatar_directory_path(instance, filename):
    return f'profile_{instance.id}/avatar.jpeg'

class DigiDexProfile(models.Model):
    """
    User profile model for storing additional user information.

    Fields:
        user (OneToOneField): A one-to-one reference to the User model.
        slug (SlugField): A slugified version of the username for URL usage.
        bio (TextField): A text field for user biography, maximum length 500 characters.
        location (CharField): A char field for user location, maximum length 30 characters.
        avatar (ImageField): An image field for user's profile picture.
        is_public (BooleanField): A boolean field to determine if the profile is public or private. Profile is private by default.
        created_at (DateTimeField): The date and time when the profile was created.
        last_modified (DateTimeField): The date and time when the profile was last modified.
    """
    user = _dfields.BaseOneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        help_text='The user associated with this profile.'
    )
    slug = _dfields.BaseSlugField(
        unique=True,
        max_length=255,
        editable=False,
        db_index=True,
        help_text="Slugified version of the username for URL usage."
    )
    bio = _dfields.BaseTextField(
        max_length=500,
        blank=True,
        help_text='A short biography of the user.'
    )
    location = _dfields.BaseCharField(
        max_length=30,
        blank=True,
        help_text='The location of the user.'
    )
    avatar = _dfields.BaseImageField(
        upload_to=profile_avatar_directory_path,
        storage=storage.PublicMediaStorage,
        null=True,
        blank=True,
        help_text='The avatar image of the profile.'
    )
    is_public = _dfields.BaseBooleanField(
        default=False,
        help_text='Indicates if the profile should be publicly visible to the public or private. Profile is private by default.'
    )
    created_at = _dfields.BaseDateTimeField(
        auto_now_add=True,
        verbose_name="Created At",
        help_text="The date and time when the profile was created."
    )
    last_modified = _dfields.BaseDateTimeField(
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

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.user.username)
            unique_slug = base_slug
            num = 1
            while DigiDexProfile.objects.filter(slug=unique_slug).exists():
                unique_slug = f'{base_slug}-{num}'
                num += 1
            self.slug = unique_slug
        
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """
        Get the URL to view the details of this profile.

        Returns:
            str: The URL to view the details of this profile.
        """
        return reverse('profile', kwargs={'username_slug': self.slug})

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"


class PersonaIndexPage(models.IndexPage):
    pass