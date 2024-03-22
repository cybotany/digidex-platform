from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel, StreamFieldPanel
from wagtail.blocks import RichTextBlock, URLBlock, ImageChooserBlock

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
            ('paragraph', RichTextBlock()),
            ('image', ImageChooserBlock()),
            ('url', URLBlock()),
        ],
        null=True,
        blank=True
    )

    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        FieldPanel('description'),
        StreamFieldPanel('body'),
    ]
