import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _

from wagtail.documents import get_document_model
from wagtail.images import get_image_model
from wagtail.models import Collection


class Category(models.Model):
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
    body = models.TextField( 
        blank=True,
        null=True,
        verbose_name=_("body")
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

    def get_items(self):
        from item.models import Item
        return Item.objects.child_of(self)

    def get_component_data(self):
        return {
            "url": self.url,
            "icon_source": None,
            "icon_alt": None,
            "name": self.name,
        }

    def get_component(self, current=False):
        from category.panels import CategoryPanel
        return CategoryPanel(self.get_component_data(), current=current)

    class Meta:
        verbose_name = _("category")
        verbose_name_plural = _("categories")
