import uuid
from django.db import models 
from django.conf import settings
from django.contrib import messages
from django.urls import reverse

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel

from base.utils.storage import PublicMediaStorage


def user_avatar_path(instance, filename):
    extension = filename.split('.')[-1]
    return f'users/{instance.username}/avatar.{extension}'

class UserProfile(models.Model):
    uuid = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False,
        db_index=True,
        verbose_name="User Profile UUID"
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="profile",
    )
    image = models.ImageField(
        storage=PublicMediaStorage(),
        upload_to=user_avatar_path,
        null=True,
        blank=True,
        verbose_name="User Profile Avatar"
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

    def add_category(self, name):
        Category = self.card_model
        category = Category.objects.create(
            user=self,
            name=name,
            defaults={'is_party': name == "Party"}
        )
        category.save()
        return category

    def get_category(self, name):
        return self.inventory_categories.prefetch_related('itemized_digits').get(name=name)

    def remove_category(self, name):
        category = self.get_category(name)
        category.delete()
        message = f"Inventory category '{name}' was removed."
        messages.info(message)
        return category

    def list_categories(self):
        return self.inventory_categories.prefetch_related('itemized_digits')

    def get_panel_details(self):
        return {
            'name': self.display_name,
            'description': self.display_description,
            'date': self.display_date,
            'image_url': self.image_url,
            'delete_url': self.delete_url,
            'update_url': self.update_url
        }

    def get_card_details(self):
        return {
            'name': self.display_name,
            'description': self.display_description,
            'date': self.display_date,
            'page_url': self.page_url
        }

    @property
    def username(self):
        return self.user.username

    @property
    def display_name(self):
        return self.username.title()

    @property
    def display_description(self):
        return self.bio or 'No description available.'

    @property
    def display_date(self):
        return self.created_at.strftime('%b %d, %Y')

    @property
    def image_url(self):
        return self.image.url if self.image else None

    @property
    def slug_kwargs(self):
        return {
            'user_slug': self.user.slug,
        }

    @property
    def _page(self):
        if not hasattr(self, 'page'):
            from inventory.utils import get_or_create_user_profile_page
            get_or_create_user_profile_page(self)
        return self.page

    @property
    def page_url(self):
        return self._page.url

    @property
    def update_url(self):
        return reverse('inventory:update_profile', kwargs=self.slug_kwargs)

    @property
    def delete_url(self):
        return reverse('inventory:delete_profile', kwargs=self.slug_kwargs)

    @property
    def card_model(self):
        from inventory.models import Category
        return Category

    def __str__(self):
        return f"{self.display_name}'s Profile"

    class Meta:
        verbose_name = "User Profile"

    @classmethod
    def get_queryset(cls):
        return super().get_queryset().select_related('user')


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
        'inventory.UserProfilePage'
    ]


class UserProfilePage(Page):
    profile = models.OneToOneField(
        UserProfile,
        on_delete=models.PROTECT,
        related_name="page"
    )

    parent_page_types = [
        'inventory.UserProfileIndexPage'
    ]

    @property
    def page_panel(self):
        return self.profile.get_panel_details()

    @property
    def page_cards(self):
        card_list = []
        categories = self.profile.list_categories()
        for catagory in categories:
            card_list.append(catagory.get_card_details())
        return card_list

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['profile_panel'] = self.page_panel
        context['category_cards'] = self.page_cards
        return context

    @classmethod
    def get_queryset(cls):
        return super().get_queryset().select_related('profile')

    class Meta:
        verbose_name = "User Profile Page"
