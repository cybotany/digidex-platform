from django.db import models
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.models import Page

class HeadingMixin(models.Model):
    heading_title = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )
    heading_intro = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    panels = [
        MultiFieldPanel(
            [
                FieldPanel('heading_title'),
                FieldPanel('heading_intro'),
            ],
            heading="Page Heading",
        ),
    ]

    class Meta:
        abstract = True


class BasePage(HeadingMixin, Page):
    content_panels = Page.content_panels + HeadingMixin.panels

    class Meta:
        abstract = True
