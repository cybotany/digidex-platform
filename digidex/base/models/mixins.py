from django.db import models
from wagtail.admin.panels import FieldPanel, MultiFieldPanel

class HeadingMixin(models.Model):
    heading_title = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )
    heading_paragraph = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    panels = [
        MultiFieldPanel(
            [
                FieldPanel('heading_title'),
                FieldPanel('heading_paragraph'),
            ],
            heading="Page Heading",
        ),
    ]

    class Meta:
        abstract = True
