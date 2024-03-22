from wagtail.models import Page
from wagtail.admin.panels import FieldPanel

from base.fields import wagtail_fields as _wfields
from base.blocks import basic_blocks as _bblocks

class IndexPage(Page):
    introduction = _wfields.BaseStreamField(
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
