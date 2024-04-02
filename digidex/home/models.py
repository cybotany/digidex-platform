from django.db import models
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel, MultiFieldPanel

class HomePage(Page):
    hero_heading = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )
    hero_paragraph = models.TextField(
        blank=True,
        null=True
    )
    hero_cta_link = models.URLField(
        blank=True,
        null=True
    )
    hero_cta_text = models.CharField(
        blank=True,
        null=True
    )
    alt_hero_cta_link = models.URLField(
        blank=True,
        null=True
    )
    alt_hero_cta_text = models.CharField(
        blank=True,
        null=True
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel('hero_heading'),
                FieldPanel('hero_paragraph'),
            ],
            heading="Hero Content",
        ),
        MultiFieldPanel(
            [
                FieldPanel('hero_cta_link'),
                FieldPanel('hero_cta_text'),
            ],
            heading="Primary Hero Button",
        ),
        MultiFieldPanel(
            [
                FieldPanel('alt_hero_cta_link'),
                FieldPanel('alt_hero_cta_text'),
            ],
            heading="Secondary Hero Button",
        ),
    ]

    class Meta:
        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"
