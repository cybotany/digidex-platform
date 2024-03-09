from django.db import models
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.fields import RichTextField, StreamField
from wagtail.models import Page, Orderable
from modelcluster.fields import ParentalKey
# Project specific imports
from base import blocks

class HomePageSection(Orderable):
    page = ParentalKey(
        "HomePage",
        related_name="sections"
    )
    title = models.CharField(
        max_length=255,
        blank=True
    )
    content = StreamField(
        blocks.BaseStreamBlock(),
        use_json_field=True,
        blank=True
    )
    lottie_animation = models.CharField(
        max_length=255,
        blank=True,
        help_text="URL to the Lottie animation JSON file"
    )

    panels = [
        FieldPanel("title"),
        FieldPanel("content"),
        FieldPanel("lottie_animation"),
    ]


class HomePage(Page):
    body = StreamField(
        blocks.BaseStreamBlock(),
        null=True,
        blank=True,
        verbose_name="Page body",
        use_json_field=True
    )

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]
