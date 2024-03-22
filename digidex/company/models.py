from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel, StreamFieldPanel

from base.blocks import basic_blocks as _bblocks

class CompanyPage(Page):
    # Metadata fields
    subtitle = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    description = RichTextField(
        blank=True
    )
    
    # Dynamic content blocks
    body = StreamField(
        [
            ('paragraph', _bblocks.BaseRichTextBlock()),
            ('image', _bblocks.BaseImageBlock()),
            ('url', _bblocks.BaseURLBlock()),
        ],
        null=True,
        blank=True
    )

    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        FieldPanel('description'),
        StreamFieldPanel('body'),
    ]
