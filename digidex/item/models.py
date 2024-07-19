import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _

from wagtail.documents import get_document_model
from wagtail.images import get_image_model
from wagtail.models import Collection


class Item(models.Model):
    uuid = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False,
        db_index=True
    )
    name = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name=_("name")
    )
    slug = models.SlugField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name=_("slug")
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
            "url": self.url,
            "heading": self.name,
            "paragraph": self.body,
            "thumbnail": self.get_thumbnail(),
        }

    def get_component(self, featured=False):
        from item.panels import ItemPanel
        return ItemPanel(self.get_component_data())

    class Meta:
        verbose_name = _("item")
        verbose_name_plural = _("items")
