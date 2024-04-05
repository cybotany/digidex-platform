from wagtail import models
from wagtail import fields
from wagtail.admin import panels

from home import blocks

class HomePage(models.Page):
    hero = fields.StreamField(
        blocks.HeroSection(),
        blank=True,
        null=True,
        use_json_field=True
    )

    content_panels = models.Page.content_panels + [
        panels.FieldPanel('hero'),
    ]

    class Meta:
        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"
