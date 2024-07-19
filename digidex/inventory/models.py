import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _

from wagtail.documents import get_document_model
from wagtail.images import get_image_model
from wagtail.models import Collection


class Inventory(models.Model):
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

    def get_categories(self, exclude_party=True):
        from category.models import Category
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
