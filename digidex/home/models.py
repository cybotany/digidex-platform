from django.db import models
from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel

from base.blocks.page_content_block import PageContentBlock


class HomePage(Page):
    heading = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )
    paragraph = models.TextField(
        blank=True,
        null=True
    )
    body = StreamField(
        [
            ('content', PageContentBlock()),
        ],
        blank=True
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel('heading'),
                FieldPanel('paragraph'),
            ],
            heading="Page Heading",
        ),
        FieldPanel('body'),
    ]

    class Meta:
        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"
