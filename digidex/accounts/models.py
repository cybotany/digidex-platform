import uuid
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth.models import AbstractUser

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel

from base.utils.storage import PublicMediaStorage


def user_avatar_path(instance, filename):
    extension = filename.split('.')[-1]
    return f'users/{instance.username}/avatar.{extension}'


class UserIndexPage(Page):
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
        'accounts.UserPage'
    ]


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
            base_slug = slugify(self.username)
            slug = base_slug
            counter = 1
            while User.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def create_page(self):
        try:
            user_index_page = UserIndexPage.objects.get(slug='u')
        except UserIndexPage.DoesNotExist:
            print('UserIndexPage does not exist. Please create it first.')
            return None

        if not UserPage.objects.filter(user=self).exists():
            user_page = UserPage(
                title=f"{self.username}'s Profile",
                slug=self.slug,
                user=self
            )
            user_index_page.add_child(instance=user_page)
            user_page.save_revision().publish()

            print(f'UserPage for user {self.username} created and added successfully!')
            return user_page
        else:
            print(f'UserPage for user {self.username} already exists.')
            return UserPage.objects.get(user=self)

    def create_profile(self):
        profile, created = UserProfile.objects.get_or_create(user=self)
        if created:
            profile.save()
        return profile

    def get_digits(self):
        return None
        #return self.user.get_inventory_digits()

    @property
    def _username(self):
        return self.username.title()


class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.PROTECT,
        related_name="profile"
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

    def __str__(self):
        return self.user._username

    class Meta:
        verbose_name = "User Profile"


class UserPage(Page):
    user = models.OneToOneField(
        User,
        on_delete=models.PROTECT,
        help_text="Link to the associated user profile.",
        related_name="page"
    )

    @property
    def username(self):
        return self.user.username

    @property
    def form_url(self):
        return reverse('accounts:profile_form', kwargs={'profile_slug': self.slug})

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['digits'] = self.get_digits()
        return context

    parent_page_types = [
        'accounts.UserIndexPage'
    ]

    class Meta:
        verbose_name = "User Page"
