from wagtail import models
from wagtail import fields
from wagtail.admin import panels

from home import blocks

class HomePage(models.Page):
    body = fields.StreamField(
        [
            ('hero', blocks.HeroBlock()),  
        ],
        null=True,
        blank=True
    )

    content_panels = models.Page.content_panels + [
        panels.FieldPanel('body'),
    ]

    class Meta:
        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"
