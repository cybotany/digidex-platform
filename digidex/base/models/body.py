from django.db import models
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.models import Page

class HeadingMixin(models.Model):
    title = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )
    intro = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    panels = [
        MultiFieldPanel(
            [
                FieldPanel('title'),
                FieldPanel('intro'),
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
