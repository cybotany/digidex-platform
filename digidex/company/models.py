from wagtail.models import Page
from wagtail.admin.panels import FieldPanel

from base.blocks import basic_blocks as _bblocks
from base.fields import django_fields, wagtail_fields
from base import models as base_models


class CompanyIndexPage(base_models.IndexPage):
    pass

class CompanyPage(Page):
    # Metadata fields
    subtitle = django_fields.BaseCharField(
        max_length=255,
        null=True,
        blank=True
    )
    description = wagtail_fields.BaseRichTextField(
        blank=True
    )
    
    # Dynamic content blocks
    body = wagtail_fields.BaseStreamField(
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
        FieldPanel('body'),
    ]
