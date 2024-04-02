# base/models/header.py
from django.db import models
from wagtail.admin import panels
from wagtail.contrib.settings import models as wg_settings


@wg_settings.register_setting
class SocialMediaSettings(wg_settings.BaseGenericSetting):
    twitter_url = models.URLField(
        verbose_name="Twitter URL",
        blank=True
    )
    github_url = models.URLField(
        verbose_name="GitHub URL",
        blank=True
    )

    panels = [       
        panels.MultiFieldPanel(
            [
                panels.FieldPanel("twitter_url"),
                panels.FieldPanel("github_url"),
            ],
            "Social Media Section Links",
        )
    ]
