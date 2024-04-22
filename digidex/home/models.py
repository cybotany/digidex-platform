from django.db import models

from wagtail.admin import panels
from wagtail import models as wt_models
from wagtail import fields as wt_fields
from modelcluster import fields as mc_fields


class HomePageSection(wt_models.Orderable):
    _STYLES = (
        ('default', 'Default'),
        ('top-bar', 'Top Bar'),
        ('top', 'Top'),
        ('hero', 'Hero'),
        ('footer', 'Footer'),
        ('full', 'Full'),
    )

    page = mc_fields.ParentalKey(
        'HomePage',
        related_name='sections'
    )
    heading = models.CharField(
        max_length=75,
        blank=True
    )
    subtitle = models.CharField(
        max_length=25,
        blank=True
    )
    paragraph = models.CharField(
        max_length=255,
        blank=True
    )
    content = wt_fields.RichTextField(
        blank=True
    )
    style = models.CharField(
        max_length=10,
        choices=_STYLES,
        default='default',
        blank=True
    )
    
    panels = [
        panels.FieldPanel('heading'),
        panels.FieldPanel('subtitle'),
        panels.FieldPanel('paragraph'),
        panels.FieldPanel('content'),
        panels.FieldPanel('style'),
    ]

    class Meta:
        verbose_name = "section"
        verbose_name_plural = "sections"


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

    content_panels = wt_models.Page.content_panels + [
        panels.FieldPanel('hero_heading'),
        panels.FieldPanel('hero_paragraph'),
        panels.FieldPanel('hero_cta_text'),
        panels.FieldPanel('hero_cta_link'),
        panels.InlinePanel('lottie_features', label="Lottie Features"),
    ]

    class Meta:
        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"
