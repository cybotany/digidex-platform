from django.db import models
from wagtail.admin import panels
from wagtail.contrib.settings import models as _wsettings

@_wsettings.register_setting
class NavigationSettings(_wsettings.BaseGenericSetting):
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
