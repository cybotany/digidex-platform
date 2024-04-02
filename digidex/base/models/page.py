# base/models/page.py
from django.db import models
from wagtail.admin import panels
from wagtail.models import Page

class BasePage(models.Model):
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
        panels.MultiFieldPanel(
            [
                panels.FieldPanel('heading_title'),
                panels.FieldPanel('heading_intro'),
            ],
            heading="Page Heading",
        ),
    ]
    content_panels = Page.content_panels + panels

    class Meta:
        abstract = True
