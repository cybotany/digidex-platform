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
    hero_primary_cta_text = models.CharField(
        blank=True,
        max_length=255,
        verbose_name="Primary CTA Text"
    )
    hero_primary_cta_link = models.URLField(
        blank=True,
        verbose_name="Primary CTA Link"
    )
    hero_secondary_cta_text = models.CharField(
        blank=True,
        max_length=255,
        verbose_name="Secondary CTA Text"
    )
    hero_secondary_cta_link = models.URLField(
        blank=True,
        verbose_name="Secondary CTA Link"
    )


    content_panels = wt_models.Page.content_panels + [
        panels.FieldPanel('hero_heading'),
        panels.FieldPanel('hero_paragraph'),
        panels.FieldPanel('hero_primary_cta_text'),
        panels.FieldPanel('hero_primary_cta_link'),
        panels.FieldPanel('hero_secondary_cta_text'),
        panels.FieldPanel('hero_secondary_cta_link'),
    ]

    class Meta:
        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"
