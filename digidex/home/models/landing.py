from django.db import models

from wagtail.admin.panels import MultiFieldPanel, FieldPanel
from wagtail.models import Page


class LandingPage(Page):
    hero_heading = models.CharField(
        blank=True,
        max_length=255,
    )
    hero_paragraph = models.TextField(
        blank=True,
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel('hero_heading'),
                FieldPanel('hero_paragraph'),
            ], heading="Hero Section"
        ),
    ]

    subpage_types = [
        'home.TrainerPage'
    ]

    class Meta:
        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"
