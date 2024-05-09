from django.db import models
from django.conf import settings
from django.urls import reverse
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
from wagtail.search import index

from profiles.forms import UserProfileForm
from inventory.models import UserDigitizedObjectInventoryPage


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
    avatar = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    bio = models.TextField(
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
    slug = models.SlugField(
        unique=True,
        max_length=255,
        verbose_name="User Slug"
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
            _username = self.user.username.title()
            profile_page = UserProfilePage(
                title=f"{_username}'s Profile",
                owner=self.user,
                slug=self.slug,
                heading=f"{_username}",
                intro=f"Welcome to {_username}'s Profile Page.",
                profile=self
            )

            try:
                profile_index_page = UserProfileIndexPage.objects.get(slug='u')
            except UserProfileIndexPage.DoesNotExist:
                raise UserProfileIndexPage.DoesNotExist("Default User Profile Index Page does not exist.")

            profile_index_page.add_child(instance=profile_page)
            profile_page.save_revision().publish()
            return profile_page

    def __str__(self):
        return self.user.username

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
        index.SearchField('get_username', partial_match=True, boost=2),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('heading'),
        FieldPanel('intro'),
        FieldPanel('profile'),
    ]

    parent_page_types = [
        'profiles.UserProfileIndexPage'
    ]

    subpage_types = [
        'inventory.UserDigitizedObjectInventoryPage'
    ]

    def get_profile(self):
        """
        Method to return the content (User Profile) being managed in this page.
        """
        if self.profile:
            return self.profile
        return None

    def get_user(self):
        """
        Method to return the content (User Profile) being managed in this page.
        """
        if self.profile:
            return self.profile.user
        return None

    def get_username(self):
        """
        Method to return the username of the associated owner.
        """
        if self.profile:
            return self.profile.user.username
        return None

    def create_inventory_page(self):
        """
        Method to create a UserDigitizedObjectInventoryPage associated with this profile page.
        """
        existing_inventory_page = self.get_inventory_page()
        if existing_inventory_page:
            return existing_inventory_page

        owner = self.get_user()
        username = self.get_username().title()

        inventory_page = UserDigitizedObjectInventoryPage(
            title=f"{username}'s Inventory",
            owner=owner,
            slug='inventory',
            heading="Inventory",
            intro=f"Welcome to {username}'s Inventory Page.",

        )
        self.add_child(instance=inventory_page)
        inventory_page.save_revision().publish()
        return inventory_page

    def get_inventory_page(self):
        """
        Fetch the UserDigitizedObjectInventoryPage associated with this profile page.
        Assumes there is at most one such page per UserProfilePage.
        """
        inventory_page = self.get_children().type(UserDigitizedObjectInventoryPage).first()
        if inventory_page:
            return inventory_page.specific
        else:
            self.create_inventory_page()

    def get_profile_form(self):
        """
        Retrieve an instance of the profile form filled with the UserProfile data.
        """
        profile_data = {
            'bio': self.profile.bio,
            'avatar': self.profile.avatar if self.profile.avatar else None
        }
        return UserProfileForm(initial=profile_data)

    def get_profile_form_url(self):
        """
        Retrieve the URL for the profile form view.
        Assumes a named URL pattern 'profile_form' that handles the form.
        """
        profile = self.get_profile()
        return reverse('profiles:profile_form', kwargs={'profile_slug': profile.slug})

    class Meta:
        verbose_name = "User Profile Page"
