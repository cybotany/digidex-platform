from django.db import models
from wagtail.admin.panels import FieldPanel, MultiFieldPanel

from base.models.body import BasePage

class SupportIndexPage(BasePage):
    body_heading_subtitle = models.CharField(
        blank=True,
        null=True
    )
    body_heading_title = models.CharField(
        blank=True,
        null=True
    )
    support_launch_chat = models.TextField(
        blank=True,
        null=True
    )
    support_chat = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )
    support_launch_email = models.TextField(
        blank=True,
        null=True
    )
    support_email = models.CharField(
        max_length=255,
        blank=True, 
        null=True
    )
    support_launch_call = models.TextField(
        blank=True,
        null=True
    )
    support_call = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    content_panels = BasePage.content_panels + [
        MultiFieldPanel([
            FieldPanel('body_heading_subtitle'),
            FieldPanel('body_heading_title'),
        ], heading="Page Body Heading"),
        MultiFieldPanel([
            FieldPanel('support_launch_chat'),
            FieldPanel('support_chat'),
        ], heading="Lottie Chat Support Bubble"),
        MultiFieldPanel([
            FieldPanel('support_launch_email'),
            FieldPanel('support_email'),
        ], heading="Lottie Email Support Bubble"),
        MultiFieldPanel([
            FieldPanel('support_launch_call'),
            FieldPanel('support_call'),
        ], heading="Lottie Call Support Bubble"),
    ]
