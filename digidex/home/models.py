from django.db import models

from wagtail.admin import panels
from wagtail import models as wt_models
from modelcluster import fields as mc_fields


class LottieFeature(wt_models.Orderable):
    page = mc_fields.ParentalKey(
        'HomePage', 
        on_delete=models.CASCADE,
        related_name='lottie_features'
    )
    icon = models.ForeignKey(
        'wagtailimages.Image', 
        on_delete=models.SET_NULL, 
        null=True,
        blank=True,
        related_name='+'
    )
    text = models.CharField(
        max_length=25,
        blank=True
    )

    panels = [
        panels.FieldPanel('icon'),
        panels.FieldPanel('text'),
    ]


class CompanyStatistic(wt_models.Orderable):
    page = mc_fields.ParentalKey(
        'HomePage', 
        on_delete=models.CASCADE,
        related_name='company_statistics'
    )
    icon = models.ForeignKey(
        'wagtailimages.Image', 
        on_delete=models.SET_NULL, 
        null=True,
        blank=True,
        related_name='+'
    )
    heading = models.CharField(
        max_length=25,
        blank=True
    )
    text = models.CharField(
        max_length=75,
        blank=True
    )
    color = models.CharField(
        max_length=25,
        blank=True
    )

    panels = [
        panels.FieldPanel('icon'),
        panels.FieldPanel('heading'),
        panels.FieldPanel('text'),
    ]


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
    hero_cta_text = models.CharField(
        blank=True,
        max_length=255,
        verbose_name="Hero CTA Text"
    )
    hero_cta_link = models.URLField(
        blank=True,
        verbose_name="Hero CTA Link"
    )
    company_subtitle = models.CharField(
        blank=True,
        max_length=255,
        verbose_name="Company Subtitle"
    )
    company_heading = models.CharField(
        blank=True,
        max_length=255,
        verbose_name="Company Heading"
    )
    company_paragraph = models.TextField(
        blank=True,
        verbose_name="Company Paragraph"
    )

    content_panels = wt_models.Page.content_panels + [
        panels.MultiFieldPanel(
            [
                panels.FieldPanel('hero_heading'),
                panels.FieldPanel('hero_paragraph'),
                panels.FieldPanel('hero_cta_text'),
                panels.FieldPanel('hero_cta_link'),
                panels.InlinePanel('lottie_features', label="Lottie Features"),
            ], heading="Hero Section"
        ),
        panels.MultiFieldPanel(
            [
                panels.FieldPanel('company_subtitle'),
                panels.FieldPanel('company_heading'),
                panels.FieldPanel('company_paragraph'),
                panels.InlinePanel('company_statistics', label="Company Statistics"),
            ], heading="Company Content Section"
        ),
    ]

    class Meta:
        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"
