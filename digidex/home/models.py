from django.db import models
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel, MultiFieldPanel

class HomePage(Page):
    heading = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )
    paragraph = models.TextField(
        blank=True,
        null=True
    )
    cta_link = models.ForeignKey(
        'wagtailcore.Page', 
        null=True, 
        blank=True, 
        on_delete=models.SET_NULL, 
        related_name='+'
    )
    cta_text = models.CharField(
        blank=True,
        null=True
    )
    feature_1 = models.CharField(
        blank=True,
        null=True
    )
    feature_2 = models.CharField(
        blank=True,
        null=True
    )
    feature_3 = models.CharField(
        blank=True,
        null=True
    )
    feature_4 = models.CharField(
        blank=True,
        null=True
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel('heading'),
                FieldPanel('paragraph'),
            ],
            heading="Hero Content",
        ),
        MultiFieldPanel(
            [
                FieldPanel('cta_link'),
                FieldPanel('cta_text'),
            ],
            heading="Call To Action",
        ),
        MultiFieldPanel(
            [
                FieldPanel('feature_1'),
                FieldPanel('feature_2'),
                FieldPanel('feature_3'),
                FieldPanel('feature_4'),
            ],
            heading="Lottie Features",
        ),
    ]

    class Meta:
        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"
