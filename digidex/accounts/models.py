import uuid

from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
from wagtail.search import index


class User(AbstractUser):
    username = models.CharField(
        max_length=32,
        unique=True
    )
    uuid = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False,
        db_index=True,
        verbose_name="User UUID"
    )


class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="profile"
    )
    avatar = models.ForeignKey(
        'wagtailimages.Image', 
        null=True, 
        blank=True, 
        on_delete=models.SET_NULL, 
        related_name='+'
    )
    biography = RichTextField(
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Created At"
    )
    last_modified = models.DateTimeField(
        auto_now=True,
        verbose_name="Last Modified"
    )

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "User Profile"


class UserProfileIndexPage(Page):
    body = RichTextField(
        blank=True
    )

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full")
    ]

    subpage_types = ['accounts.UserProfilePage']


class UserProfilePage(Page):
    user_profile = models.OneToOneField(
        UserProfile,
        on_delete=models.PROTECT,
        related_name="user_pages",
        help_text="Link to the associated user profile."
    )
    body = RichTextField(
        blank=True,
        help_text="Additional content about the user."
    )

    search_fields = Page.search_fields + [
        index.SearchField('get_username', partial_match=True, boost=2),
        index.SearchField('get_biography', partial_match=True, boost=1),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('user_profile'),
        FieldPanel('body'),
    ]

    subpage_types = [
        'digitization.DigitizedObjectRegistrationPage',
        'digitization.UserDigitizedObjectPage',
        'digitization.UserDigitizedObjectTagIndexPage'
    ]

    def get_username(self):
        """Method to return the username of the associated user."""
        if self.user_profile:
            return self.user_profile.user.username
        return "No User"

    def get_biography(self):
        """Method to return the biography of the associated user."""
        if self.user_profile:
            return self.user_profile.biography
        return "No Biography"

    class Meta:
        verbose_name = "User Profile Page"
