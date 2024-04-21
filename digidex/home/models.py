from django.db import models

from wagtail.admin import panels
from wagtail import models as wt_models

class HomePage(wt_models.Page):
    hero_heading = models.CharField(
        blank=True,
        max_length=255,
        verbose_name="Hero Heading"
    )
    hero_paragraph = models.TextField(
        blank=True,
        verbose_name="Hero Paragraph"
    )
    hero_cta_text = models.CharField(
        blank=True,
        max_length=255,
        verbose_name="Hero CTA Text"
    )
    hero_cta_link = models.URLField(
        blank=True,
        verbose_name="Hero CTA Link"
    )


    content_panels = wt_models.Page.content_panels + [
        panels.FieldPanel('hero_heading'),
        panels.FieldPanel('hero_paragraph'),
        panels.FieldPanel('hero_cta_text'),
        panels.FieldPanel('hero_cta_link'),
    ]

    class Meta:
        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"
