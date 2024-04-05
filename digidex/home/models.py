from wagtail import models
from wagtail import fields
from wagtail.admin import panels

from home import blocks

class HomePage(models.Page):
    page = fields.StreamField(
        [
            ('hero_section', blocks.HeroSection()),
        ],
        blank=True,
        null=True,
        use_json_field=True
    )

    content_panels = models.Page.content_panels + [
        panels.FieldPanel('page'),
    ]

    class Meta:
        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"
