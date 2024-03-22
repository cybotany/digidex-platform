from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel

class HomePage(Page):
    hero_heading = models.CharField(
        blank=True,
        max_length=75
    )
    hero_text = models.CharField(
        blank=True,
        max_length=150
    )
    hero_cta = models.CharField(
        blank=True,
        verbose_name="Hero CTA",
        max_length=75
    )
    hero_cta_link = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="Hero CTA link"
    )
    lottie = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel("hero_heading"),
                FieldPanel("hero_text"),
                FieldPanel("hero_cta"),
                FieldPanel("hero_cta_link"),
            ],
            heading="Hero section",
        ),
        FieldPanel('lottie'),
    ]
