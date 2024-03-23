from django.db import models
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel, MultiFieldPanel

from base.fields import django_fields, wagtail_fields


class HomePage(Page):
    hero_heading = django_fields.BaseCharField(
        blank=True,
        max_length=75
    )
    hero_text = django_fields.BaseCharField(
        blank=True,
        max_length=150
    )
    hero_cta = django_fields.BaseCharField(
        blank=True,
        verbose_name="Hero CTA",
        max_length=75
    )
    hero_cta_link = django_fields.BaseForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="Hero CTA link"
    )
    lottie = wagtail_fields.BaseRichTextField(
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
