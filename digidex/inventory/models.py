import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _

from wagtail.documents import get_document_model
from wagtail.images import get_image_model
from wagtail.models import Page, Collection

from inventory.validators import validate_ntag_serial


class InventoryPage(Page):
    parent_page_types = [
        'home.HomePage',
        'InventoryPage'
    ]
    subpage_types = [
        'InventoryPage'
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
        return InventoryAsset.objects.filter(inventory=self)

    class Meta:
        verbose_name = 'Inventory Page'
        verbose_name_plural = 'Inventory Pages'


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
        return f"NFC Tag: {self.serial_number}"

    def activate_tag(self):
        self.active = True
        self.save()

    def deactivate_tag(self):
        self.active = False
        self.save()

    def create_link(self):
        link, created = InventoryLink.objects.get_or_create(tag=self)
        if created:
            return link
        return link

    class Meta:
        verbose_name = "ntag"
        verbose_name_plural = "ntags"


class InventoryLink(models.Model):
    inventory = models.OneToOneField(
        InventoryPage,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='+'
    )
    tag = models.OneToOneField(
        InventoryTag,
        on_delete=models.CASCADE,
        related_name='link'
    )

    def __str__(self):
        if self.inventory:
            return f"{self.tag} -> {self.inventory}"
        return str(self.tag)

    def get_url(self):
        if self.inventory:
            return self.inventory.url
        return None

    @property
    def url(self):
        return self.get_url()
