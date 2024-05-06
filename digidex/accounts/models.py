import uuid
from django.db import models, transaction
from django.conf import settings
from django.contrib.auth.models import AbstractUser, Group, Permission
from wagtail.models import Page, Collection, GroupCollectionPermission
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
from wagtail.search import index

from inventory.models import UserDigitizedObjectInventoryPage


class User(AbstractUser):
    uuid = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False,
        db_index=True,
        verbose_name="User UUID"
    )

    def create_user_group(self):
        user_group, created = Group.objects.get_or_create(name=f"user_{self.username}_group")
        if created:
            self.groups.add(user_group)
            self.save()
        return created

    def set_collection_permissions(self, collection):
        """
        Method to set permissions for the user collection.
        """
        user_group, _ = self.create_user_group()
        permissions = ['add', 'change', 'delete', 'view']
        for permission in permissions:
            permission_codename = f'{permission}_{collection._meta.model_name}'
            perm, _ = Permission.objects.get_or_create(codename=permission_codename)
            GroupCollectionPermission.objects.get_or_create(
                group=user_group,
                collection=collection,
                permission=perm
            )

    def create_user_collection(self):
        """
        Method to create a user collection for the associated user.
        """
        with transaction.atomic():
            users_root_collection, _ = Collection.objects.get_or_create(
                name='Users',
                defaults={'depth': 1}
            )
            user_collection_name = f"{self.username}'s Collection"
            collection, created = users_root_collection.add_child(
                name=user_collection_name
            )
            self.set_collection_permissions(collection)


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
                'slug': self.user.username.replace(' ', '-').lower()
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

    def get_content(self):
        """
        Method to return the content (User Profile) being managed in this page.
        """
        if self.profile:
            return self.profile
        return "No User"

    def get_username(self):
        """
        Method to return the username of the associated owner.
        """
        _profile = self.get_content()
        return _profile.user.username

    def create_inventory_page(self):
        """
        Method to create a UserDigitizedObjectInventoryPage associated with this profile page.
        """
        _username = self.get_username()
        inventory_page = UserDigitizedObjectInventoryPage(
            title=f"{_username}'s Inventory",
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
