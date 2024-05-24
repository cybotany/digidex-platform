from django.apps import apps
from django.db import models
from django.conf import settings
from django.urls import reverse

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
from wagtail.search import index

from base.utils.storage import PublicMediaStorage


def user_avatar_path(instance, filename):
    extension = filename.split('.')[-1]
    return f'users/{instance.user.username}/avatar.{extension}'


class UserProfileIndexPage(Page):
    heading = models.CharField(
        max_length=255,
        blank=True
    )
    intro = RichTextField(
        blank=True
    )

    content_panels = Page.content_panels + [
        FieldPanel('heading'),
        FieldPanel('intro'),
    ]

    parent_page_types = [
        'home.HomePage'
    ]

    subpage_types = [
        'profiles.UserProfilePage'
    ]


class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="profile"
    )
    slug = models.SlugField(
        unique=True,
        db_index=True,
        max_length=255,
        verbose_name="User Slug"
    )
    avatar = models.ImageField(
        storage=PublicMediaStorage(),
        upload_to=user_avatar_path,
        null=True,
        blank=True
    )
    bio = models.TextField(
        null=True,
        blank=True,
        help_text="Short Biography about the user."
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Created At"
    )
    last_modified = models.DateTimeField(
        auto_now=True,
        verbose_name="Last Modified"
    )

    def get_profile_page(self):
        """
        Retrieves the associated UserProfilePage. Raises a specific exception if not found.
        """
        try:
            return UserProfilePage.objects.get(profile=self)
        except UserProfilePage.DoesNotExist:
            raise UserProfilePage.DoesNotExist("Profile page for user does not exist.")

    def create_profile_page(self):
        """
        Creates a new UserProfilePage for the user if it does not already exist.
        """
        try:
            return self.get_profile_page()
        except UserProfilePage.DoesNotExist:
            profile_page = UserProfilePage(
                title=f"{self.user._username}'s Profile",
                owner=self.user,
                slug=self.slug,
                heading=f"{self.user._username}",
                intro=f"Welcome to {self.user._username}'s Profile Page.",
                profile=self
            )

            try:
                profile_index_page = UserProfileIndexPage.objects.get(slug='u')
            except UserProfileIndexPage.DoesNotExist:
                raise UserProfileIndexPage.DoesNotExist("Default User Profile Index Page does not exist.")

            profile_index_page.add_child(instance=profile_page)
            profile_page.save_revision().publish()
            return profile_page

    def get_or_create_user_party(self):
        """
        Method to get or create a UserParty instance associated with this user profile.
        """
        UserParty = apps.get_model('party', 'UserParty')
        
        user_party, created = UserParty.objects.get_or_create(profile=self)
        return user_party

    def __str__(self):
        return self.user._username

    class Meta:
        verbose_name = "User Profile"


class UserProfilePage(Page):
    heading = models.CharField(
        max_length=255,
        blank=True
    )
    intro = RichTextField(
        blank=True
    )
    profile = models.OneToOneField(
        UserProfile,
        on_delete=models.PROTECT,
        related_name="profile_page",
        help_text="Link to the associated user profile."
    )

    search_fields = Page.search_fields + [
        index.SearchField('username', partial_match=True, boost=2),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('heading'),
        FieldPanel('intro'),
        FieldPanel('profile'),
    ]

    parent_page_types = [
        'profiles.UserProfileIndexPage'
    ]

    @property
    def user(self):
        """
        Method to return the content (User Profile) being managed in this page.
        """
        if self.profile:
            return self.profile.user
        return None

    @property
    def username(self):
        """
        Method to return the username of the associated owner.
        """
        if self.profile:
            return self.profile.user.username
        return None

    @property
    def _username(self):
        return self.username.title()

    @property
    def form_url(self):
        """
        Retrieve the URL for the profile form view.
        Assumes a named URL pattern 'profile_form' that handles the form.
        """
        return reverse('profiles:profile_form', kwargs={'profile_slug': self.profile.slug})

    class Meta:
        verbose_name = "User Profile Page"
