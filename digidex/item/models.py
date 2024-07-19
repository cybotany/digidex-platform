import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _

from wagtail.documents import get_document_model
from wagtail.images import get_image_model
from wagtail.models import Page, Collection
from wagtail.contrib.routable_page.models import RoutablePageMixin, path
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel


class ItemPage(RoutablePageMixin, Page):
    parent_page_types = [
        'category.CategoryPage'
    ]
    subpage_types = []

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
        from item.components import ItemCard
        return ItemCard(self.get_component_data(), featured=featured)

    class Meta:
        verbose_name = _("item")
        verbose_name_plural = _("items")
