import uuid

from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser, Group, Permission

from wagtail.models import Page, Collection, GroupCollectionPermission, Site
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
from wagtail.search import index


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

    def create_user_profile(self):
        profile, created = UserProfile.objects.get_or_create(user=self)
        if created:
            profile.save() 
        return created


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
    bio = RichTextField(
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

    def create_user_profile_page(self, parent):
        user_page = UserProfilePage(
            title=f"{self.user.username}'s Inventory",
            owner=self.user,
            slug=self.user.username.replace(' ', '-').lower(),
            profile=self
        )
        parent.add_child(instance=user_page)
        user_page.save_revision().publish()
        return user_page.url

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

    subpage_types = ['accounts.UserProfilePage']


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

    #subpage_types = [
    #    'digitization.DigitizedObjectRegistrationPage',
    #    'inventory.UserDigitizedObjectPage',
    #    'inventory.UserDigitizedObjectTagIndexPage'
    #]

    def create_user_collection(self, parent=None):
        if parent is None:
            parent = Collection.get_first_root_node()

        user_collection_name = f"{self.user.username}'s Collection"
        collection = parent.add_child(name=user_collection_name)
        self.set_collection_permissions(collection)
        return collection

    def set_collection_permissions(self, collection):
        user_group, _ = self.user.create_user_group()
        permissions = ['add', 'change', 'delete', 'view']
        for permission in permissions:
            permission_codename = f'{permission}_{collection._meta.model_name}'
            perm, _ = Permission.objects.get_or_create(codename=permission_codename)
            GroupCollectionPermission.objects.get_or_create(
                group=user_group,
                collection=collection,
                permission=perm
            )
    
    def get_username(self):
        """Method to return the username of the associated user."""
        if self.profile:
            return self.profile.user.username
        return "No User"

    class Meta:
        verbose_name = "User Profile Page"
