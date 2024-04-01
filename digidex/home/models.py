from django.db import models
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel, MultiFieldPanel

from base import blocks as _bblocks

class HomePage(Page):
    hero_info_link = models.URLField(
        blank=True
    )
    hero_info_text = models.CharField(
        max_length=255,
        blank=True
    )
    hero_info_img = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    hero_heading = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )
    hero_paragraph = models.TextField(
        blank=True,
        null=True
    )
    hero_buttons = _bblocks.ButtonCollectionBlock()

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel('hero_heading'),
                FieldPanel('hero_paragraph'),
            ],
            heading="Landing Page Hero Text",
        ),
        MultiFieldPanel(
            [
                FieldPanel('hero_cta_link'),
                FieldPanel('alt_hero_cta_link'),
            ],
            heading="Landing Page Hero Buttons",
        ),
    ]

    class Meta:
        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"
