from django.conf import settings
from django.db import models
from django.urls import reverse

from wagtail import models as wt_models
from wagtail.admin import panels


class UserProfile(models.Model):
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

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"


class UserProfilePage(wt_models.Page):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='profile_page',
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
    avatar = models.ForeignKey(
        'wagtailimages.Image', 
        null=True, 
        blank=True, 
        on_delete=models.SET_NULL, 
        related_name='+'
    )
    is_public = models.BooleanField(
        default=False,
        help_text='Indicates if the profile should be publicly visible.'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Created At"
    )
    last_modified = models.DateTimeField(
        auto_now=True,
        verbose_name="Last Modified"
    )

    content_panels = wt_models.Page.content_panels + [
        panels.FieldPanel('user'),
        panels.FieldPanel('bio'),
        panels.FieldPanel('location'),
        panels.FieldPanel('avatar'),
        panels.FieldPanel('is_public'),
    ]

    def __str__(self):
        return f"{self.user.username}'s Profile"

    def get_url_parts(self, request=None):
        site_id, root_url, page_path = super().get_url_parts(request=request)
        custom_url = reverse('profile_view', kwargs={'username': self.user.username})
        return (site_id, root_url, custom_url)

    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"
