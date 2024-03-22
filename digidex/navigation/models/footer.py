from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.contrib.settings.models import BaseGenericSetting, register_setting

from base.fields import django_fields as _dfields

@register_setting
class FooterNavigationSettings(BaseGenericSetting):
    twitter_url = _dfields.BaseURLField(
        verbose_name="Twitter URL",
        blank=True 
    )
    github_url = _dfields.BaseURLField(
        verbose_name="GitHub URL",
        blank=True
    )
    linkedin_url = _dfields.BaseURLField(
        verbose_name="LinkedIn URL",
        blank=True
    )

    panels = [
        MultiFieldPanel(
            [
                FieldPanel("twitter_url"),
                FieldPanel("github_url"),
                FieldPanel("linkedin_url"),
            ],
            "Social settings",
        )
    ]
