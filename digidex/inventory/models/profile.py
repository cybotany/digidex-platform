import uuid
from django.db import models 
from django.apps import apps
from django.contrib import messages
from django.urls import reverse
from django.utils.text import slugify

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
    slug = models.SlugField(
        unique=True,
        db_index=True,
        max_length=255,
        verbose_name="User Profile Slug"
    )
    user = models.OneToOneField(
        apps.get_model('accounts', 'User'),
        on_delete=models.PROTECT,
        related_name="profile"
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

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.user.username)
        super().save(*args, **kwargs)

    def add_category(self, name):
        Category = apps.get_model('inventory', 'Category')
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

    @property
    def _name(self):
        return self.user.username.title()

    @property
    def _description(self):
        return self.bio or 'No description available.'

    @property
    def _date(self):
        return self.created_at.strftime('%b %d, %Y')

    @property
    def _image_url(self):
        return self.image.url if self.image else None

    @property
    def _page(self):
        if not hasattr(self, 'page'):
            from inventory.utils import get_or_create_user_profile_page
            get_or_create_user_profile_page(self)
        return self.page

    @property
    def _page_url(self):
        return self._page.url

    @property
    def _update_url(self):
        return reverse('inventory:update_profile', kwargs={'user_slug': self.slug})

    @property
    def _delete_url(self):
        return reverse('inventory:delete_profile', kwargs={'user_slug': self.slug})

    def get_panel_details(self):
        return {
            'name': self._name,
            'description': self._description,
            'date': self._date,
            'image_url': self._image_url,
            'delete_url': self._delete_url,
            'update_url': self._update_url
        }

    def get_list_details(self):
        return {
            'name': self._name,
            'description': self._description,
            'date': self._date,
            'image_url': self._image_url,
            'delete_url': self._delete_url,
            'update_url': self._update_url
        }

    def get_card_details(self):
        return {
            'name': self._name,
            'description': self._description,
            'date': self._date,
            'page_url': self._page_url
        }

    def __str__(self):
        return f"{self._name}'s Profile"

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

    parent_page_types = ['home.HomePage']
    subpage_types = ['accounts.UserProfilePage']


class UserProfilePage(Page):
    profile = models.OneToOneField(
        UserProfile,
        on_delete=models.PROTECT,
        related_name="page"
    )

    @property
    def user(self):
        return self.owner

    @property
    def username(self):
        return self.owner.username.title()

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['profile_panel'] = self.user.template_panel
        context['category_cards'] = self.user.template_cards
        return context
    
    parent_page_types = ['accounts.UserProfileIndexPage']

    @classmethod
    def get_queryset(cls):
        return super().get_queryset().select_related('owner')

    class Meta:
        verbose_name = "User Page"
