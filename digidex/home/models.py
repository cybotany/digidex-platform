from django.utils.translation import gettext_lazy as _

from wagtail.models import Page, Site
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel


class HomePage(Page):
    parent_page_types = [
        'wagtailcore.Page'
    ]
    subpage_types = [
        'inventory.InventoryPage'
    ]

    body = RichTextField(
        blank=True,
        verbose_name=_('Body'),
    )

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]
