import uuid
from django.db import models
from django.contrib import messages
from django.apps import apps
from django.utils.text import slugify
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel

from base.utils.storage import PublicMediaStorage


def user_avatar_path(instance, filename):
    extension = filename.split('.')[-1]
    return f'users/{instance.username}/avatar.{extension}'


class UserIndexPage(Page):
    heading = models.CharField(max_length=255, blank=True)
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('heading'),
        FieldPanel('intro'),
    ]

    parent_page_types = ['home.HomePage']
    subpage_types = ['accounts.UserPage']


class User(AbstractUser):
    uuid = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False,
        db_index=True,
        verbose_name="User UUID"
    )
    slug = models.SlugField(
        unique=True,
        db_index=True,
        max_length=255,
        verbose_name="User Slug"
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._generate_unique_slug()
        super().save(*args, **kwargs)

    def _generate_unique_slug(self):
        base_slug = slugify(self.username)
        slug = base_slug
        counter = 1
        while User.objects.filter(slug=slug).exists():
            slug = f"{base_slug}-{counter}"
            counter += 1
        return slug

    def create_page(self):
        user_index_page = self._get_user_index_page()
        if not user_index_page:
            print('UserIndexPage does not exist. Please create it first.')
            return None

        if not UserPage.objects.filter(owner=self).exists():
            user_page = UserPage(
                title=f"{self}'s Page",
                slug=self.slug,
                owner=self
            )
            user_index_page.add_child(instance=user_page)
            user_page.save_revision().publish()
            print(f'UserPage for user {self.username} created and added successfully!')
            return user_page
        else:
            print(f'UserPage for user {self.username} already exists.')
            return UserPage.objects.get(owner=self)

    def get_page(self):
        try:
            return UserPage.objects.get(owner=self)
        except UserPage.DoesNotExist:
            return self.create_page()

    def _get_user_index_page(self):
        try:
            return UserIndexPage.objects.get(slug='u')
        except UserIndexPage.DoesNotExist:
            return None

    def create_profile(self):
        profile, created = UserProfile.objects.get_or_create(user=self)
        if created:
            profile.save()
        return profile

    def get_profile(self):
        if hasattr(self, 'profile'):
            return self.profile
        return self.create_profile()

    def add_category(self, name):
        Category = apps.get_model('inventory', 'Category')
        category, created = Category.objects.get_or_create(
            user=self,
            name=name,
            defaults={'is_party': name == "Party"}
        )
        if created:
            category.save()
            category.create_page()
        return category, created

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

    def create_party(self):
        party, created = self.add_category("Party")
        return party, created

    @property
    def page(self):
        return self.get_page()

    @property
    def template_cards(self):
        return [category.get_card_details() for category in self.list_categories()]

    @property
    def template_panel(self):
        return self.get_profile().get_panel_details()

    def __str__(self):
        return self.username.title()


class UserPage(Page):
    @property
    def user(self):
        return self.owner

    @property
    def username(self):
        return self.owner.username.title()

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['panel'] = self.user.template_panel
        context['cards'] = self.user.template_cards
        return context

    parent_page_types = ['accounts.UserIndexPage']

    @classmethod
    def get_queryset(cls):
        return super().get_queryset().select_related('owner')

    class Meta:
        verbose_name = "User Page"


class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.PROTECT,
        related_name="profile"
    )
    image = models.ImageField(
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

    @property
    def username(self):
        return self.user.username.title()

    def get_panel_details(self):
        return {
            'name': self.username,
            'description': self.bio or 'No description available.',
            'image': self.image.url if self.image else 'No image available.',
            'created_at': self.created_at.strftime('%b %d, %Y'),
            'detail_url': self.user.get_page().url if self.user.get_page() else '#',
            'delete_url': reverse('accounts:delete_account', kwargs={'user_slug': self.user.slug}),
            'update_url': reverse('accounts:update_account', kwargs={'user_slug': self.user.slug})
        }

    def get_card_details(self):
        return {
            'name': self.username,
            'description': self.bio or 'No description available.',
            'detail_url': self.user.get_page().url if self.user.get_page() else '#'
        }

    def __str__(self):
        return f"{self.username}'s Profile"

    class Meta:
        verbose_name = "User Profile"

    @classmethod
    def get_queryset(cls):
        return super().get_queryset().select_related('user')
