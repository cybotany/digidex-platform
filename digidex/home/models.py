from django.db import models

from wagtail.admin.panels import MultiFieldPanel, FieldPanel
from wagtail.models import Page


class HomePage(Page):
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

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel('hero_heading'),
                FieldPanel('hero_paragraph'),
                FieldPanel('hero_cta_text'),
                FieldPanel('hero_cta_link'),
            ], heading="Hero Section"
        ),
    ]

    subpage_types = [
        'profiles.UserProfileIndexPage'
    ]

    class Meta:
        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"
