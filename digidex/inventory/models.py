import uuid

from django.db import models, transaction
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
    slug = models.SlugField(
        max_length=255,
        null=True,
        blank=True,
        db_index=True
    )
    name = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name=_("name")
    )
    collection = models.ForeignKey(
        Collection,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='+',
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    last_modified = models.DateTimeField(
        auto_now=True
    )

    def _get_parent_collection(self):
        raise NotImplementedError("Subclasses must implement _get_parent_collection method")

    def _set_slug(self):
        raise NotImplementedError("Subclasses must implement _set_slug method")

    def _create_collection(self):
        parent = self._get_parent_collection()
        uuid = str(self.uuid)
        children = parent.get_children()
        try:
            collection = children.get(name=uuid)
        except Collection.DoesNotExist:
            collection = parent.add_child(name=uuid)
        return collection

    @transaction.atomic
    def _set_collection(self):
        self.collection = self._create_collection()

    def get_documents(self):
        return get_document_model().objects.filter(collection=self.collection)

    def get_images(self):
        return get_image_model().objects.filter(collection=self.collection)

    def get_thumbnail(self):
        images = self.get_images()
        if images:
            return images.first()
        return None

    def get_template_context_data(self):
        raise NotImplementedError("Subclasses must implement get_template_context_data method")

    def get_url(self):
        raise NotImplementedError("Subclasses must implement get_url method")

    @property
    def url(self):
        return self.get_url()

    def save(self, *args, **kwargs):
        if not self.slug:
            self._set_slug()
        if not self.collection:
            self._set_collection()
        super().save(*args, **kwargs)

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

    def _set_slug(self):
        self.slug = slugify(self.owner.username)

    def _get_parent_collection(self):
        parent = Collection.get_first_root_node()
        parent_children = parent.get_children()
        try:
            collection = parent_children.get(name='Inventory')
        except Collection.DoesNotExist:
            collection = parent.add_child(name="Inventory")
        return collection

    def get_url(self):
        return f"/{self.slug}"

    def get_categories(self):
        return self.categories.all()

    def get_assets(self):
        return self.assets.all()

    def get_template_context_data(self):
        return {
            'title': self.name,
            'heading': self.name,
            'categories': self.get_categories(),
            'assets': self.get_assets()
        }

    def save(self, *args, **kwargs):
        if not self.name:
            self.name = f"{self.owner.username.title()}'s Inventory"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.owner.username.title()}'s inventory"

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
    inventory = models.ForeignKey(
        UserInventory,
        on_delete=models.CASCADE,
        related_name='categories',
        verbose_name=_("inventory")
    )
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name=_("description")
    )

    RESERVED_KEYWORDS = ['add', 'update', 'delete', 'admin']

    def _set_slug(self):
        if self.name:
            self.slug = slugify(self.name)

    def _get_parent_collection(self):
        return self.inventory.collection

    def get_url(self):
        return f"{self.inventory.url}/{self.slug}"

    def get_assets(self):
        return self.assets.all()

    def get_template_context_data(self):
        return {
            'title': self.name,
            'heading': self.name,
            'description': self.description,
            'assets': self.get_assets()
        }

    def save(self, *args, **kwargs):
        if self.name and self.name.lower() in self.RESERVED_KEYWORDS:
            raise ValueError(f"The name '{self.name}' is reserved and cannot be used.")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('inventory category')
        verbose_name_plural = _('inventory categories')
        constraints = [
            models.UniqueConstraint(
                fields=['inventory', 'slug'],
                name='unique_inventory_category_slug'
            )
        ]


class InventoryAsset(AbstractInventory):
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
        null=True,
        blank=True,
        verbose_name=_("category")
    )
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name=_("description")
    )

    def _set_slug(self):
        if self.name:
            self.slug = slugify(self.name)

    def _get_parent_collection(self):
        if self.category:
            return self.category.collection
        return self.inventory.collection

    def get_url(self):
        if self.category:
            return f"{self.category.url}/{self.slug}"
        return f"{self.inventory.url}/{self.slug}"

    def get_template_context_data(self):
        return {
            'title': self.name,
            'heading': self.name,
            'image': self.get_thumbnail(),
            'url': self.get_url(),
        }

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("inventory asset")
        verbose_name_plural = _("inventory assets")
        constraints = [
            models.UniqueConstraint(
                fields=['inventory', 'category', 'slug'],
                name='unique_inventory_asset_slug'
            )
        ]
