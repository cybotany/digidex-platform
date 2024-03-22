from django.db import models
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel, StreamFieldPanel

from digidex.base.models import wagtail_fields as _bfields
from base.blocks import basic_blocks as _bblocks

class CompanyPage(Page):
    # Metadata fields
    subtitle = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    description = _bfields.BaseRichTextField(
        blank=True
    )
    
    # Dynamic content blocks
    body = _bfields.BaseStreamField(
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
