from base.fields import django
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel

from base.fields import wagtail
from base.blocks import basics as _blocks
from base import models as _models


class CompanyIndexPage(_models.BaseIndexPage):
    pass

class CompanyPage(_models.BasePage):
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
            ('paragraph', _blocks.BaseRichTextBlock()),
            ('image', _blocks.BaseImageBlock()),
            ('url', _blocks.BaseURLBlock()),
        ],
        null=True,
        blank=True
    )

    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        FieldPanel('description'),
        FieldPanel('body'),
    ]
