import uuid
from django.db import models
from django.conf import settings

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel

from base.utils.storage import PublicMediaStorage


def user_avatar_path(instance, filename):
    extension = filename.split('.')[-1]
    return f'users/{instance.owner.username}/avatar.{extension}'


class UserProfileIndexPage(Page):
    heading = models.CharField(
        max_length=255,
        blank=True
    )
    introduction = RichTextField(
        blank=True
    )

    content_panels = Page.content_panels + [
        FieldPanel('heading'),
        FieldPanel('introduction'),
    ]

    parent_page_types = [
        'home.HomePage'
    ]

    subpage_types = [
        'inventory.UserProfilePage'
    ]


class UserProfilePage(Page):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        db_index=True,
        null=True,
        related_name='profile',
        verbose_name="User Profile User"
    )
    uuid = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False,
        db_index=True,
        verbose_name="User Profile UUID"
    )
    image = models.ImageField(
        storage=PublicMediaStorage(),
        upload_to=user_avatar_path,
        null=True,
        blank=True,
        verbose_name="User Profile Avatar"
    )
    heading = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="User Profile Heading"
    )
    introduction = models.TextField(
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

    parent_page_types = [
        'inventory.UserProfileIndexPage'
    ]

    subpage_types = [
        'inventory.InventoryCategoryPage'
    ]

    def get_upload_to_base_path(self):
        return f'users/{self.uuid}'

    def get_upload_to(self, subdirectory, filename):
        extension = filename.split('.')[-1]
        return f'{self.get_upload_to_base_path()}/{subdirectory}/{uuid.uuid4()}.{extension}'

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)     
        return context

    class Meta:
        verbose_name = "User Profile Page"
