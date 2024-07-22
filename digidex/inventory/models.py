import uuid

from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from wagtail.documents import get_document_model
from wagtail.images import get_image_model
from wagtail.admin.panels import FieldPanel

from base.models import AbstractDigiDexPage


class BaseInventory(AbstractDigiDexPage):
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

    def create_file(self, name):
        return self._create_child_inventory(name, 'file')

    def create_folder(self, name):
        return self._create_child_inventory(name, 'folder')

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
            ('file', 'File'),
            ('folder', 'Folder'),
        ]
    )

    content_panels = BaseInventory.content_panels + [
        FieldPanel('type'),
    ]

    def is_file(self):
        return self.type == 'file'

    def get_thumbnail(self):
        images = self.get_images()
        if images:
            return images.first()
        return None

    def get_files(self):
        return InventoryFile.objects.filter(inventory=self)

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

    def create_file(self, name):
        if self.is_file():
            return None
        inventory, _ = self._create_child_inventory(name, 'file')
        file = InventoryFile.objects.create(
            name=name,
            inventory=inventory
        )
        return file

    def create_folder(self, name):
        if self.is_file():
            return None
        folder, _ = self._create_child_inventory(name, 'folder')
        return folder

    class Meta:
        verbose_name = _('inventory page')
        verbose_name_plural = _('inventorie pages')


class InventoryFile(models.Model):
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
        related_name='file'
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
