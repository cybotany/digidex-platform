import uuid

from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from wagtail.documents import get_document_model
from wagtail.models import Page, Collection
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel


class AbstractInventory(Page):
    """
    Abstract class for all inventory members.
    """
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
    body = RichTextField( 
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

    content_panels = Page.content_panels + [
        FieldPanel("name"),
        FieldPanel("body"),
        FieldPanel("collection"),
    ]

    def get_context(self, request):
        context = super().get_context(request)
        documents = get_document_model().objects.filter(collection=self.collection)
        context['documents'] = documents
        return context

    def save(self):
        self.slug = slugify(self.name)
        self.collection = self.get_parent().collection
        super().save()

    class Meta:
        abstract = True


class InventoryIndex(AbstractInventory):
    """
    Acts as the index for all user-specific inventory members.
    """
    class Meta:
        verbose_name = _("inventory")
        verbose_name_plural = _("inventories")


class InventoryCategory(AbstractInventory):
    class Meta:
        verbose_name = _("category")
        verbose_name_plural = _("categories")


class InventoryItem(AbstractInventory):
    class Meta:
        verbose_name = _("item")
        verbose_name_plural = _("items")
