import uuid

from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from wagtail.documents import get_document_model
from wagtail.models import Page, Collection
from wagtail.contrib.routable_page.models import RoutablePageMixin, path, re_path
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel


class AbstractInventory(RoutablePageMixin, Page):
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

    @path('add/', name='add_child_page')
    def add_child_page(self, request):
        pass

    @path('update/', name='update_current_page')
    def update_current_page(self, request):
        pass

    @path('delete/', name='delete_current_page')
    def delete_current_page(self, request):
        pass

    def get_context(self, request):
        context = super().get_context(request)

        documents = get_document_model().objects.filter(collection=self.collection)
        context['documents'] = documents
        context['title'] = self.title 
        context['children'] = self.get_children()
        context['add_child_page'] = self.reverse_subpage('add_child_page')
        context['update_current_page'] = self.reverse_subpage('update_current_page')
        context['delete_current_page'] = self.reverse_subpage('delete_current_page')
        return context

    class Meta:
        abstract = True


class InventoryIndex(AbstractInventory):
    parent_page_types = []
    subpage_types = ['inventory.InventoryCategory']

    class Meta:
        verbose_name = _("inventory")
        verbose_name_plural = _("inventories")


class InventoryCategory(AbstractInventory):
    parent_page_types = ['inventory.InventoryIndex']
    subpage_types = ['inventory.InventoryItem']

    class Meta:
        verbose_name = _("category")
        verbose_name_plural = _("categories")


class InventoryItem(AbstractInventory):
    parent_page_types = ['inventory.InventoryCategory']
    subpage_types = []

    class Meta:
        verbose_name = _("item")
        verbose_name_plural = _("items")
