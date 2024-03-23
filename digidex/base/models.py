from wagtail.models import Page
from wagtail.admin.panels import FieldPanel

from base.fields import wagtail_fields
from base.blocks import basics

class IndexPage(Page):
    introduction = wagtail_fields.BaseStreamField(
        [
            ('paragraph', basics.BaseRichTextBlock()),
        ],
        null=True,
        blank=True
    )

    content_panels = Page.content_panels + [
        FieldPanel('introduction'),
    ]

    class Meta:
        abstract = True
