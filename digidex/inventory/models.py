import uuid

from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from wagtail.documents import get_document_model
from wagtail.images import get_image_model
from wagtail.admin.panels import FieldPanel

from base.models import AbstractSitePage


class BaseInventory(AbstractSitePage):
    """
    Base class for inventory pages.
    """
    def is_asset(self):
        return False

    def _create_child_collection(self, name):
        return self.collection.get_children().get_or_create(name=name)

    def _create_child_inventory(self, name, type):
        child_collection, _ = self._create_child_collection(name)
        child_inventory = UserInventory(
            title=name,
            slug=slugify(name),
            owner=self.owner,
            collection=child_collection,
            type=type
        )
        self.add_child(instance=child_inventory)
        child_inventory.save_revision().publish()
        return child_inventory

    def _create_child(self, name, type):
        if self.is_asset():
            return None
        return self._create_child_inventory(name, type)

    def create_asset(self, name):
        inventory_asset = self._create_child(name, 'asset')
        _ = InventoryAsset.objects.create(
            name=name,
            inventory=inventory_asset
        )
        return inventory_asset

    def create_category(self, name):
        inventory_category = self._create_child(name, 'category')
        return inventory_category

    def get_specific_children(self):
        if self.is_asset():
            return UserInventory.objects.none()
        return self.get_children().specific()
    
    def get_categories(self):
        children = self.get_specific_children()
        return children.filter(type='category')

    def get_assets(self):
        children = self.get_specific_children()
        return children.filter(type='asset')

    def get_header(self):
        from inventory.panels import InventoryHeaderPanel
        return InventoryHeaderPanel(inventory=self)

    def get_context(self, request):
        context = super().get_context(request)
        context['inventory_header'] = self.get_header()
        return context

    class Meta:
        verbose_name = _('inventory')
        verbose_name_plural = _('inventories')


class UserInventoryIndex(BaseInventory):
    parent_page_types = [
        'home.HomePage'
    ]
    subpage_types = [
        'inventory.UserInventory'
    ]

    class Meta:
        verbose_name = _('user inventory index')
        verbose_name_plural = _('user inventory indexes')


class UserInventory(BaseInventory):
    parent_page_types = [
        'inventory.UserInventoryIndex',
        'inventory.UserInventory'
    ]
    subpage_types = [
        'inventory.UserInventory'
    ]

    type = models.CharField(
        max_length=10,
        choices=[
            ('asset', 'Asset'),
            ('category', 'Category'),
        ]
    )

    content_panels = BaseInventory.content_panels + [
        FieldPanel('type'),
    ]

    def is_asset(self):
        return self.type == 'asset'

    def get_thumbnail(self):
        images = self.get_images()
        if images:
            return images.first()
        return None

    def get_panel_data(self):
        if self.is_asset():
            return {}
        return {
            'name': self.title,
            'url': self.url,
            'thumbnail': self.get_thumbnail(),
        }

    class Meta:
        verbose_name = _('inventory page')
        verbose_name_plural = _('inventory pages')


class InventoryAsset(models.Model):
    uuid = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False,
        db_index=True
    )
    inventory = models.OneToOneField(
        UserInventory,
        on_delete=models.CASCADE,
        verbose_name=_("inventory"),
        related_name='asset'
    )
    name = models.CharField(
        max_length=255,
        verbose_name=_("name")
    )
    body = models.TextField( 
        blank=True,
        null=True,
        verbose_name=_("body")
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    last_modified = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.name

    def get_documents(self):
        return get_document_model().objects.filter(collection=self.inventory.collection)

    def get_images(self):
        return get_image_model().objects.filter(collection=self.inventory.collection)

    def get_thumbnail(self):
        images = self.get_images()
        if images:
            return images.first()
        return None

    class Meta:
        verbose_name = _("inventory asset")
        verbose_name_plural = _("inventory assets")
