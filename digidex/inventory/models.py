import uuid

from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _

from wagtail.documents import get_document_model
from wagtail.images import get_image_model
from wagtail.models import Page, Collection

from inventory.panels import CategoryPanel, ItemPanel


class Inventory(Page):
    uuid = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False,
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

    def get_documents(self):
        return get_document_model().objects.filter(collection=self.collection)

    def get_images(self):
        return get_image_model().objects.filter(collection=self.collection)

    def get_categories(self, exclude_party=True):
        if exclude_party:
            return Category.objects.child_of(self).exclude(slug='party')
        return Category.objects.child_of(self)

    def get_category_items(self):
        category_items = {}
        for category in self.get_categories():
            category_items[category] = category.get_items()
        return category_items[category]

    def get_party(self):
        return self.get_categories(exclude_party=False).filter(slug='party').first()

    def get_items(self):
        items = []
        for category in self.get_categories():
            items.extend(category.get_items())
        return items

    class Meta:
        verbose_name = _("inventory")
        verbose_name_plural = _("inventories")


class Category(models.Model):
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
        null=True,
        blank=True,
        verbose_name=_("slug")
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='+',
    )
    collection = models.ForeignKey(
        Collection,
        on_delete=models.SET_NULL,
        null=True,
        related_name='+',
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

    def get_documents(self):
        return get_document_model().objects.filter(collection=self.collection)

    def get_images(self):
        return get_image_model().objects.filter(collection=self.collection)

    def get_items(self):
        return Item.objects.child_of(self)

    def get_component_data(self):
        return {
            "url": self.slug,
            "icon_source": None,
            "icon_alt": None,
            "name": self.name,
        }

    def get_component(self, current=False):
        return CategoryPanel(self.get_component_data(), current=current)

    class Meta:
        verbose_name = _("category")
        verbose_name_plural = _("categories")


class Item(models.Model):
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
        verbose_name=_("slug")
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='+',
    )
    collection = models.ForeignKey(
        Collection,
        on_delete=models.SET_NULL,
        null=True,
        related_name='+',
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

    def get_documents(self):
        return get_document_model().objects.filter(collection=self.collection)

    def get_images(self):
        return get_image_model().objects.filter(collection=self.collection)

    def get_thumbnail(self):
        images = self.get_images()
        if images:
            return images.first()
        return None

    def get_component_data(self):
        return {
            "date": self.created_at,
            "url": self.slug,
            "heading": self.name,
            "paragraph": self.body,
            "thumbnail": self.get_thumbnail(),
        }

    def get_component(self, featured=False):
        return ItemPanel(self.get_component_data())

    class Meta:
        verbose_name = _("item")
        verbose_name_plural = _("items")
