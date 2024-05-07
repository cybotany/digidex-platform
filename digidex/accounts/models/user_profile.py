from django.db import models
from django.conf import settings
from django.utils.text import slugify
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
from wagtail.search import index

from inventory.models import UserDigitizedObjectInventoryPage


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

    def create_user_profile_page(self):
        profile_page, created = UserProfilePage.objects.get_or_create(
            profile=self,
            defaults={
                'title': f"{self.user.username}'s Profile",
                'owner': self.user,
                'slug': slugify(self.user.username)
            }
        )
        if created:
            profile_index_page = UserProfileIndexPage.objects.get(title="User Profiles")
            profile_index_page.add_child(instance=profile_page)
            profile_page.save_revision().publish()

        return profile_page

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "User Profile"


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
        'accounts.UserProfilePage'
    ]


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
        'accounts.UserProfileIndexPage'
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
        return "No User Profile Found."

    def get_username(self):
        """
        Method to return the username of the associated owner.
        """
        _profile = self.get_profile()
        return _profile.user.username

    def create_inventory_page(self):
        """
        Method to create a UserDigitizedObjectInventoryPage associated with this profile page.
        """
        _username = self.get_username()
        inventory_page = UserDigitizedObjectInventoryPage(
            title=f"{_username}'s Inventory",
            owner=self.profile.user,
            slug='inventory'
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

    def get_child_page(self):
        """
        Method to return the UserDigitizedObjectInventoryPage associated with this profile page.
        """
        self.get_inventory_page()

    class Meta:
        verbose_name = "User Profile Page"
