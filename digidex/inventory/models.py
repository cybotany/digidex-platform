import uuid
from django.apps import apps
from django.db import models
from django.utils.text import slugify

from modelcluster.fields import ParentalKey
from wagtail.models import Page, Orderable
from wagtail.admin.panels import FieldPanel, InlinePanel


class UserInventory(Orderable):
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
    profile_page = ParentalKey(
        'profiles.UserProfilePage',
        on_delete=models.CASCADE,
        related_name='inventories'
    )
    detail_page = models.OneToOneField(
        'inventory.UserInventoryPage',
        on_delete=models.PROTECT,
        related_name='detailed_digit',
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    last_modified = models.DateTimeField(
        auto_now=True
    )

    @property
    def profile(self):
        return self.profile_page.profile

    @property
    def user(self):
        return self.profile.user

    @property
    def username(self):
        return self.user.username

    @property
    def _username(self):
        return self.username.title()

    def save(self, *args, **kwargs):
        original_name = self.name
        unique_name = original_name
        num = 1
        while UserInventory.objects.filter(profile_page=self.profile_page, name=unique_name).exclude(pk=self.pk).exists():
            unique_name = f"{original_name} ({num})"
            num += 1
        self.name = unique_name
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def create_page(self):
        """
        Method to create a UserInventoryPage associated with this UserInventory instance.
        """
        UserInventoryPage = apps.get_model('inventory', 'UserInventoryPage')
        
        inventory_page = UserInventoryPage(
            title=f"{self._username}'s Inventory: {self.name}",
            slug=slugify(self.name),
            heading="Inventory",
            intro=f"Welcome to {self._username}'s Inventory Page.",
        )
        self.profile_page.add_child(instance=inventory_page)
        inventory_page.save_revision().publish()
        
        # Link the UserInventory to the created UserInventoryPage
        self.detail_page = inventory_page
        self.save()

        return inventory_page

    class Meta:
        unique_together = ('profile_page', 'name')


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
        related_name='inventory_page'
    )

    @property
    def profile_page(self):
        UserProfilePage = apps.get_model('profiles', 'UserProfilePage')
        parent = self.get_parent()
        if isinstance(parent.specific, UserProfilePage):
            return parent.specific
        return None

    @property
    def profile(self):
        return self.profile_page.profile

    content_panels = Page.content_panels + [
        FieldPanel('heading'),
        FieldPanel('intro'),
        InlinePanel('itemized_digits', label="Itemized Digits"),
    ]

    parent_page_types = [
        'profiles.UserProfilePage'
    ]

    subpage_types = [
        'digitization.UserDigitPage'
    ]
