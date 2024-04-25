# base/models/settings.py
from django.db import models

from wagtail.admin import panels
from wagtail.contrib.settings.models import register_setting, BaseGenericSetting

@register_setting
class SiteSettings(BaseGenericSetting):
    logo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Company Logo."
    )

    panels = [
        panels.FieldPanel('logo'),
    ]
