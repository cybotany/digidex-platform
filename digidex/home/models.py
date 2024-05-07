from django.db import models

from wagtail.fields import StreamField
from wagtail.admin.panels import MultiFieldPanel, FieldPanel
from wagtail.models import Page

from home.blocks import HomeStreamBlock


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
    body = StreamField(
        HomeStreamBlock(),
        blank=True,
        use_json_field=True,
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
        FieldPanel("body"),
    ]

    subpage_types = [
        'accounts.UserProfileIndexPage'
    ]

    class Meta:
        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"
