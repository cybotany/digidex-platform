from wagtail import models
from wagtail import fields
from wagtail.admin import panels

from base import blocks

class HomePage(models.Page):
    body = fields.StreamField(
        [
            ('heading', blocks.BasicHeadingBlock()),
            ('paragraph', blocks.BasicParagraphBlock()),
            ('image', blocks.BasicImageBlock()),
            ('document', blocks.BasicDocumentBlock()),
        ],
        null=True,
        blank=True,
        use_json_field=True
    )

    content_panels = models.Page.content_panels + [
        panels.FieldPanel('body'),
    ]

    class Meta:
        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"
