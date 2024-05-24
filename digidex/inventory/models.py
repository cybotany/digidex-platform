import uuid
from django.db import models
from django.conf import settings
from django.utils.text import slugify

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel


class UserInventory(models.Model):
    uuid = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False,
        db_index=True,
        verbose_name="Digitized Object UUID"
    )
    name = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        default='Inventory',
        help_text="Digitized Object Inventory name."
    )
    description = models.TextField(
        blank=True,
        null=True,
        help_text="Digitized object Inventory description."
    )
    slug = models.SlugField(
        unique=True,
        db_index=True,
        max_length=255,
        verbose_name="Digitized Object Inventory Slug"
    )
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="inventory"
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    last_modified = models.DateTimeField(
        auto_now=True
    )

    def save(self, *args, **kwargs):
        original_name = self.name
        unique_name = original_name
        num = 1
        while UserInventory.objects.filter(user=self.user, name=unique_name).exclude(pk=self.pk).exists():
            unique_name = f"{original_name} ({num})"
            num += 1
        self.name = unique_name
        self.slug = f"inv/{slugify(self.name)}"
        super().save(*args, **kwargs)

    class Meta:
        unique_together = ('user', 'name')


class UserInventoryPage(Page):
    heading = models.CharField(
        max_length=255,
        blank=True
    )
    intro = models.TextField(
        blank=True,
        help_text="Introduction text to display at the top of the index page."
    )
    inventory = models.OneToOneField(
        UserInventory,
        on_delete=models.PROTECT,
        related_name='page'
    )

    content_panels = Page.content_panels + [
        FieldPanel('heading'),
        FieldPanel('intro'),
    ]

    parent_page_types = [
        'profiles.UserProfilePage'
    ]

    subpage_types = [
        'digitization.DigitalObjectPage'
    ]
