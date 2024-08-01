from django.db import models

from wagtail.images import get_image_model_string
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.contrib.settings.models import BaseGenericSetting, register_setting


@register_setting
class NavigationSettings(BaseGenericSetting):
    logo = models.ForeignKey(
        get_image_model_string(),
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='+'
    )
    chat_link = models.URLField(
        blank=True,
        null=True
    )
    email_address = models.EmailField(
        blank=True,
        null=True
    )
    phone_number = models.CharField(
        max_length=15,
        blank=True,
        null=True
    )
    twitter_url = models.URLField(
        verbose_name="Twitter URL",
        blank=True,
        null=True
    )
    github_url = models.URLField(
        verbose_name="GitHub URL",
        blank=True,
        null=True
    )
    mastodon_url = models.URLField(
        verbose_name="Mastodon URL",
        blank=True,
        null=True
    )

    panels = [
        FieldPanel("logo"),
        MultiFieldPanel(
            [
                FieldPanel("chat_link"),
                FieldPanel("email_address"),
                FieldPanel("phone_number"),
            ],
            "Contact settings",
        ),
        MultiFieldPanel(
            [
                FieldPanel("twitter_url"),
                FieldPanel("github_url"),
                FieldPanel("mastodon_url"),
            ],
            "Social settings",
        )
    ]


