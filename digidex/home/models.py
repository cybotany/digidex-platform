from django.db import models
from django.utils.translation import gettext_lazy as _
from django.shortcuts import get_object_or_404, render

from wagtail.contrib.routable_page.models import RoutablePageMixin, path, re_path
from wagtail.models import Page, Collection
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField
from wagtail.documents import get_document_model
from wagtail.images import get_image_model

from inventory.models import UserInventory, InventoryCategory, InventoryAsset


class HomePage(RoutablePageMixin, Page):
    parent_page_types = [
        'wagtailcore.Page'
    ]

    collection = models.ForeignKey(
        Collection,
        on_delete=models.SET_NULL,
        null=True,
        related_name='+',
    )
    body = RichTextField(
        blank=True,
        null=True,
        verbose_name=_("body")
    )

    content_panels = Page.content_panels + [
        FieldPanel('collection'),
        FieldPanel('body'),
    ]

    def __str__(self):
        return self.title

    def get_documents(self):
        return get_document_model().objects.filter(collection=self.collection)

    def get_images(self):
        return get_image_model().objects.filter(collection=self.collection)

    @re_path(r'^<slug:inventory_slug>/$')
    def inventory_index(self, request, inventory_slug):
        inventory = get_object_or_404(UserInventory, slug=inventory_slug)		
        context = {
            'page': self,
            'request': request,
            'inventory': inventory,
        }
        return render(request, 'inventory/user_inventory.html', context)

    class Meta:
        verbose_name = _('homepage')
