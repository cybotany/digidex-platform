from django.db import models
from django.utils.translation import gettext_lazy as _

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel

from home.components import NavigationComponent


class HomePage(Page):
    subpage_types = [
        'inventory.InventoryPage'
    ]

    body = RichTextField( 
        blank=True,
        null=True,
        verbose_name=_("body")
    )

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]

    def get_navigation(self, request):
        return NavigationComponent(request.user)

    def get_body(self, request):
        pass

    def get_context(self, request):
        context = super().get_context(request)
        context['navigation'] = self.get_navigation(request)
        context['body'] = self.get_body(request)
        return context
