from django.db import models
from django.utils.translation import gettext_lazy as _
from django.shortcuts import get_object_or_404, render

from wagtail.contrib.routable_page.models import RoutablePageMixin, path, re_path
from wagtail.models import Page, Collection
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField

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

    @path('<slug:inventory_slug>/')
    def user_inventory(self, request, inventory_slug):
        inventory = get_object_or_404(UserInventory, slug=inventory_slug)		
        return self.render(
            request,
            template='inventory/user_inventory_index.html',
            context_overrides={
                'heading': inventory.name,
                'categories': inventory.get_categories(),
                'assets': inventory.get_assets(),
            }
        )


    class Meta:
        verbose_name = _('homepage')
