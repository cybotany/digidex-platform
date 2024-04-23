from django.db import models

from wagtail.admin import panels
from wagtail import models as wt_models
from modelcluster import fields as mc_fields


class LottieFeature(wt_models.Orderable):
    page = mc_fields.ParentalKey(
        'HomePage', 
        on_delete=models.CASCADE,
        related_name='lottie_feature'
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
        related_name='company_statistic'
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


class ProductFeature(wt_models.Orderable):
    page = mc_fields.ParentalKey(
        'HomePage',
        related_name='feature'
    )
    icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    heading = models.CharField(
        max_length=255
    )
    paragraph = models.CharField(
        max_length=255
    )
    
    panels = [
        panels.FieldPanel('icon'),
        panels.FieldPanel('heading'),
        panels.FieldPanel('paragraph'),
    ]

    class Meta:
        verbose_name = "Product Feature"
        verbose_name_plural = "Product Features"


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
    feature_subtitle = models.CharField(
        blank=True,
        max_length=255,
        verbose_name="Feature Subtitle"
    )
    feature_heading = models.CharField(
        blank=True,
        max_length=255,
        verbose_name="Feature Heading"
    )

    content_panels = wt_models.Page.content_panels + [
        panels.MultiFieldPanel(
            [
                panels.FieldPanel('hero_heading'),
                panels.FieldPanel('hero_paragraph'),
                panels.FieldPanel('hero_cta_text'),
                panels.FieldPanel('hero_cta_link'),
                panels.InlinePanel('lottie_feature', label="Lottie Features"),
            ], heading="Hero Section"
        ),
        panels.MultiFieldPanel(
            [
                panels.FieldPanel('company_subtitle'),
                panels.FieldPanel('company_heading'),
                panels.FieldPanel('company_paragraph'),
                panels.InlinePanel('company_statistic', label="Company Statistics"),
            ], heading="Company Section"
        ),
        panels.MultiFieldPanel(
            [
                panels.FieldPanel('feature_subtitle'),
                panels.FieldPanel('feature_heading'),
                panels.InlinePanel('feature', label="Product Features"),
            ], heading="Feature Section"
        ),
    ]

    class Meta:
        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"
