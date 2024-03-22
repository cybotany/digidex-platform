from django.db import models

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel, MultiFieldPanel

from base.fields import django as _dfields,\
                        wagtail as _wfields

class HomePage(Page):
    hero_heading = _dfields.BaseCharField(
        blank=True,
        max_length=75
    )
    hero_text = _dfields.BaseCharField(
        blank=True,
        max_length=150
    )
    hero_cta = _dfields.BaseCharField(
        blank=True,
        verbose_name="Hero CTA",
        max_length=75
    )
    hero_cta_link = _dfields.BaseForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="Hero CTA link"
    )
    lottie = _wfields.BaseRichTextField(
        blank=True
    )

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
