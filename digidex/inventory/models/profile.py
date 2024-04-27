from django.db import models
from django.conf import settings

from wagtail import models as wt_models
from wagtail.admin import panels


class ProfileIndexPage(wt_models.Page):
    subpage_types = ['inventory.ProfilePage']


class ProfilePage(wt_models.Page):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
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

    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"
