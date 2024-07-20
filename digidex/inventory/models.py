import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _

from wagtail.documents import get_document_model
from wagtail.images import get_image_model
from wagtail.models import Page, Collection

from inventory.validators import validate_ntag_serial


class Inventory(Page):
    parent_page_types = [
        'home.HomePage',
        'Inventory'
    ]
    subpage_types = [
        'Inventory'
    ]

    collection = models.ForeignKey(
        Collection,
        on_delete=models.SET_NULL,
        null=True,
        related_name='+',
    )
    type = models.CharField(
        max_length=10,
        choices=[
            ('asset', 'Asset'),
            ('group', 'Group')
        ]
    )

    def __str__(self):
        return self.title

    def is_group(self):
        return self.type == 'group'

    def is_asset(self):
        return self.type == 'asset'

    def get_documents(self):
        return get_document_model().objects.filter(collection=self.collection)

    def get_images(self):
        return get_image_model().objects.filter(collection=self.collection)

    def get_thumbnail(self):
        images = self.get_images()
        if images:
            return images.first()
        return None

    def get_assets(self):
        return Asset.objects.filter(inventory=self)

    class Meta:
        verbose_name = 'Inventory Page'
        verbose_name_plural = 'Inventory Pages'


class Asset(models.Model):
    uuid = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False,
        db_index=True
    )
    inventory = models.ForeignKey(
        Inventory,
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


class InventoryTag(models.Model):
    uuid = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
        db_index=True
    )
    serial_number = models.CharField(
        max_length=32,
        editable=False,
        unique=True,
        db_index=True,
        validators=[validate_ntag_serial]
    )
    active = models.BooleanField(
        default=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    last_modified = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"Inventory Tag: {self.serial_number}"

    def activate_tag(self):
        self.active = True
        self.save()

    def deactivate_tag(self):
        self.active = False
        self.save()

    def create_link(self):
        from link.models import InventoryLink
        link, created = InventoryLink.objects.get_or_create(tag=self)
        if created:
            return link
        return link

    class Meta:
        verbose_name = "inventory tag"
        verbose_name_plural = "inventory tags"
