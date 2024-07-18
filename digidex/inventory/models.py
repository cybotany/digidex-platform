import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _

from wagtail.documents import get_document_model
from wagtail.images import get_image_model
from wagtail.models import Page, Collection
from wagtail.contrib.routable_page.models import RoutablePageMixin, path
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel

from nearfieldcommunication.models import NearFieldCommunicationTag


class InventoryPage(RoutablePageMixin, Page):
    parent_page_types = [
        'home.HomePage'
    ]
    subpage_types = [
        'category.CategoryPage'
    ]

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

    def get_categories(self, exclude_party=True):
        from category.models import CategoryPage
        if exclude_party:
            return CategoryPage.objects.child_of(self).exclude(slug='party')
        return CategoryPage.objects.child_of(self)

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
        from category.components import CategoryCollectionComponent
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
