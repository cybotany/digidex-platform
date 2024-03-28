from django.db import models
from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel

from base.blocks import PageContentBlock

class HomePage(Page):
    heading_title = models.CharField(max_length=255, blank=True, null=True)
    heading_text = models.TextField(blank=True, null=True)
    body = StreamField(
        [
            ('content', PageContentBlock()),
        ],
        blank=True
    )

    content_panels = Page.content_panels + [
        FieldPanel('heading_title'),
        FieldPanel('heading_text'),
        FieldPanel('body'),
    ]

    class Meta:
        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"
