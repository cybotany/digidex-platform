from wagtail.models import Page
from wagtail.admin.panels import FieldPanel

from base.blocks import basic
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
            ('paragraph', basic.BaseRichTextBlock()),
            ('image', basic.BaseImageBlock()),
            ('url', basic.BaseURLBlock()),
        ],
        null=True,
        blank=True
    )

    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        FieldPanel('description'),
        FieldPanel('body'),
    ]
