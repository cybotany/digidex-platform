from django.db import models
from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel

from base.blocks.page_content_block import PageContentBlock


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
    hero_cta_link = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="Primary Hero CTA link",
        help_text="Choose a page to link to for the Primary Call to Action",
    )
    alt_hero_cta_link = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="Alternate Hero CTA link",
        help_text="Choose a page to link to for the Alternate Call to Action",
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel('heading'),
                FieldPanel('paragraph'),
            ],
            heading="Landing Page Hero Text",
        ),
        MultiFieldPanel(
            [
                FieldPanel('primary_hero_cta'),
                FieldPanel('alternate_hero_cta'),
            ],
            heading="Landing Page Hero Buttons",
        ),
    ]

    class Meta:
        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"
