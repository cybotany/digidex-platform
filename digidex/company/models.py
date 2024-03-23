from base.fields import django
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel

from base.blocks import basics as basic_blocks
from base.fields import wagtail
from base.models import basics as basic_models


class CompanyIndexPage(basic_models.IndexPage):
    pass

class CompanyPage(Page):
    # Metadata fields
    subtitle = django.BaseCharField(
        max_length=255,
        null=True,
        blank=True
    )
    description = wagtail.BaseRichTextField(
        blank=True
    )
    
    # Dynamic content blocks
    body = wagtail.BaseStreamField(
        [
            ('paragraph', basic_blocks.BaseRichTextBlock()),
            ('image', basic_blocks.BaseImageBlock()),
            ('url', basic_blocks.BaseURLBlock()),
        ],
        null=True,
        blank=True
    )

    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        FieldPanel('description'),
        FieldPanel('body'),
    ]
