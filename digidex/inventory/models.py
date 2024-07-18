import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _

from wagtail.documents import get_document_model
from wagtail.images import get_image_model
from wagtail.models import Page, Collection
from wagtail.contrib.routable_page.models import RoutablePageMixin, path, re_path
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel

from nearfieldcommunication.models import NearFieldCommunicationTag


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

    @path('add/')
    def add_child_page(self, request):
        pass

    @path('update/')
    def update_current_page(self, request):
        pass

    @path('delete/')
    def delete_current_page(self, request):
        pass

    def get_documents(self):
        return get_document_model().objects.filter(collection=self.collection)

    def get_images(self):
        return get_image_model().objects.filter(collection=self.collection)

    class Meta:
        abstract = True


class InventoryIndex(AbstractInventory):
    parent_page_types = []
    subpage_types = ['inventory.InventoryCategory']

    def get_categories(self, exclude_party=True):
        if exclude_party:
            return InventoryCategory.objects.child_of(self).exclude(slug='party')
        return InventoryCategory.objects.child_of(self)

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

    def get_header(self):
        from home.components import HeaderComponent
        from inventory.components import CategoryCollectionComponent
        header = {
            "heading": self.title,
            "categories": CategoryCollectionComponent(self.get_categories()),
        }
        return HeaderComponent(header)

    def get_navigation(self, request):
        from home.components import NavigationComponent
        return NavigationComponent(request.user)

    def get_context(self, request):
        context = super().get_context(request)
        context['header'] = self.get_header()
        context['navigation'] = self.get_navigation(request)
        return context

    class Meta:
        verbose_name = _("inventory")
        verbose_name_plural = _("inventories")


class InventoryCategory(AbstractInventory):
    parent_page_types = ['inventory.InventoryIndex']
    subpage_types = ['inventory.InventoryItem']

    def get_items(self):
        return InventoryItem.objects.child_of(self)

    def get_component_data(self):
        return {
            "url": self.url,
            "icon_source": None,
            "icon_alt": None,
            "name": self.name,
        }

    def get_component(self, current=False):
        from inventory.components import CategoryComponent
        return CategoryComponent(self.get_component_data(), current=current)

    def get_context(self, request):
        context = super().get_context(request)
        context['items'] = self.get_items()
        return context

    class Meta:
        verbose_name = _("category")
        verbose_name_plural = _("categories")


class InventoryItem(AbstractInventory):
    parent_page_types = ['inventory.InventoryCategory']
    subpage_types = []

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
        from inventory.components import ItemComponent
        return ItemComponent(self.get_component_data(), featured=featured)

    class Meta:
        verbose_name = _("item")
        verbose_name_plural = _("items")


class InventoryLink(models.Model):
    tag = models.OneToOneField(
        NearFieldCommunicationTag,
        on_delete=models.CASCADE,
        related_name='mapping'
    )
    resource = models.OneToOneField(
        Page,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='+'
    )

    def __str__(self):
        if self.resource:
            return f"{self.tag} -> {self.resource}"
        return f"{self.tag} -> None"

    class Meta:
        verbose_name = _("link")
        verbose_name_plural = _("links")
