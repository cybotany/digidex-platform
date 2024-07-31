from django.db import models
from django.shortcuts import redirect
from django.utils.translation import gettext_lazy as _

from wagtail.contrib.routable_page.models import RoutablePageMixin, path, re_path
from wagtail.models import Page, Collection
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField


class HomePage(RoutablePageMixin, Page):
    parent_page_types = [
        'wagtailcore.Page'
    ]
    child_page_types = [
        'blog.BlogIndexPage',
        'inventory.UserInventoryIndex'
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

    class Meta:
        verbose_name = _('homepage')
