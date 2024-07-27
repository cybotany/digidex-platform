import uuid

from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from wagtail.models import Collection
from wagtail.documents import get_document_model
from wagtail.images import get_image_model
from wagtail.admin.panels import FieldPanel


class AbstractInventory(models.Model):
    uuid = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False,
        db_index=True
    )
    name = models.CharField(
        max_length=255,
        verbose_name=_("name")
    )
    slug = models.SlugField(
        max_length=255,
        db_index=True
    )
    collection = models.ForeignKey(
        Collection,
        on_delete=models.SET_NULL,
        null=True,
        related_name='+',
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    last_modified = models.DateTimeField(
        auto_now=True
    )

    @property
    def url(self):
        return self.get_url()

    def get_documents(self):
        return get_document_model().objects.filter(collection=self.collection)

    def get_images(self):
        return get_image_model().objects.filter(collection=self.collection)

    def get_thumbnail(self):
        images = self.get_images()
        if images:
            return images.first()
        return None

    def get_url(self):
        pass

    content_panels = [
        FieldPanel('collection'),
    ]

    class Meta:
        abstract = True


class UserInventory(AbstractInventory):
    owner = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='inventory',
        verbose_name=_("owner")
    )

    def __str__(self):
        return f"{self.owner}'s inventory"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.owner.username)
        super().save(*args, **kwargs)

    def get_url(self):
        return f"/{self.slug}"

    class Meta:
        verbose_name = _('user inventory')
        verbose_name_plural = _('user inventories')
        constraints = [
            models.UniqueConstraint(
                fields=['slug'],
                name='unique_user_inventory_slug'
            )
        ]


class InventoryCategory(AbstractInventory):
    name = models.CharField(
        max_length=255,
        verbose_name=_("name")
    )
    inventory = models.ForeignKey(
        UserInventory,
        on_delete=models.CASCADE,
        related_name='categories',
        verbose_name=_("inventory")
    )

    RESERVED_KEYWORDS = ['add', 'update', 'delete', 'admin']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.name.lower() in self.RESERVED_KEYWORDS:
            raise ValueError(f"The name '{self.name}' is reserved and cannot be used.")
        
        if not self.slug:
            self.slug = slugify(self.name)        
        super().save(*args, **kwargs)

    def get_url(self):
        return f"{self.inventory.url}/{self.slug}"

    class Meta:
        verbose_name = _('inventory category')
        verbose_name_plural = _('inventory categories')
        constraints = [
            models.UniqueConstraint(
                fields=['inventory', 'slug'],
                name='unique_inventory_asset_slug'
            )
        ]


class InventoryAsset(AbstractInventory):
    name = models.CharField(
        max_length=255,
        verbose_name=_("name")
    )
    inventory = models.ForeignKey(
        UserInventory,
        on_delete=models.CASCADE,
        related_name='assets',
        verbose_name=_("inventory")
    )
    category = models.ForeignKey(
        InventoryCategory,
        on_delete=models.CASCADE,
        related_name='assets',
        verbose_name=_("category")
    )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)        
        super().save(*args, **kwargs)

    def get_url(self):
        if self.category:
            return f"{self.category.url}/{self.slug}"
        return f"{self.inventory.url}/{self.slug}"

    class Meta:
        verbose_name = _("inventory asset")
        verbose_name_plural = _("inventory assets")
        constraints = [
            models.UniqueConstraint(
                fields=['inventory', 'category', 'slug'],
                name='unique_inventory_asset_slug'
            )
        ]
