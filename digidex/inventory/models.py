import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _

from wagtail.documents import get_document_model
from wagtail.images import get_image_model

from base.models import AbstractIndexPage


class InventoryPage(AbstractIndexPage):
    parent_page_types = AbstractIndexPage.parent_page_types + [
        'inventory.InventoryPage'
    ]
    subpage_types = [
        'inventory.InventoryPage'
    ]

    type = models.CharField(
        max_length=10,
        choices=[
            ('file', 'File'),
            ('folder', 'Folder'),
            ('root', 'Root'),
        ]
    )

    def is_file(self):
        return self.type == 'file'

    def is_folder(self):
        return self.type == 'folder'

    def is_root(self):
        return self.type == 'root'

    def get_thumbnail(self):
        images = self.get_images()
        if images:
            return images.first()
        return None

    def get_assets(self):
        return InventoryAsset.objects.filter(inventory=self)

    class Meta:
        verbose_name = _('inventory page')
        verbose_name_plural = _('inventorie pages')


class InventoryAsset(models.Model):
    uuid = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False,
        db_index=True
    )
    inventory = models.ForeignKey(
        InventoryPage,
        on_delete=models.CASCADE,
        verbose_name=_("inventory"),
        related_name='assets'
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
        verbose_name = _("asset")
        verbose_name_plural = _("assets")
