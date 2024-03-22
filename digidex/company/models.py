from wagtail.models import Page
from wagtail.admin.panels import FieldPanel, StreamFieldPanel

from base.blocks import basic_blocks as _bblocks
from base.models import wagtail_fields as _wfields,\
                        django_fields as _dfields

class CompanyPage(Page):
    # Metadata fields
    subtitle = _dfields.BaseCharField(
        max_length=255,
        null=True,
        blank=True
    )
    description = _wfields.BaseRichTextField(
        blank=True
    )
    
    # Dynamic content blocks
    body = _wfields.BaseStreamField(
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
