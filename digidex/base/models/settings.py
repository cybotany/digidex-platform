from django.db import models

from wagtail.images import get_image_model
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.contrib.settings.models import BaseGenericSetting, register_setting


@register_setting
class NavigationSettings(BaseGenericSetting):
    logo = models.ForeignKey(
        get_image_model(),
        on_delete=models.CASCADE,
        related_name='+'
    )
    twitter_url = models.URLField(
        verbose_name="Twitter URL",
        blank=True
    )
    github_url = models.URLField(
        verbose_name="GitHub URL",
        blank=True
    )
    mastodon_url = models.URLField(
        verbose_name="Mastodon URL",
        blank=True
    )

    panels = [
        FieldPanel("logo"),
        MultiFieldPanel(
            [
                FieldPanel("twitter_url"),
                FieldPanel("github_url"),
                FieldPanel("mastodon_url"),
            ],
            "Social settings",
        )
    ]
