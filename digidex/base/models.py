from wagtail.models import Page
from wagtail.admin.panels import FieldPanel

from base.fields import wagtail_fields
from base.blocks import basic_blocks as _bblocks

class IndexPage(Page):
    introduction = wagtail_fields.BaseStreamField(
        [
            ('paragraph', _bblocks.BaseRichTextBlock()),
        ],
        null=True,
        blank=True
    )

    content_panels = Page.content_panels + [
        FieldPanel('introduction'),
    ]

    class Meta:
        abstract = True
