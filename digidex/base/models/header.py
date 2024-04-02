# base/models/header.py
from wagtail.admin import panels
from wagtail import fields
from wagtail.contrib.settings import models

from base import blocks as _bblocks

@models.register_setting
class NotificationBarSettings(models.BaseGenericSetting):
    notification = fields.StreamField(
        [
            ('title', _bblocks.HeadingBlock()),
            ('icon', _bblocks.IconBlock()),
        ],
        null=True,
        blank=True,
    )

    panels = [
        panels.FieldPanel('notification'),
    ]

    class Meta:
        verbose_name = "Notification Bar Settings"
