# base/models/header.py
from wagtail.admin import panels
from wagtail import fields
from wagtail.contrib.settings import models
from wagtail.images import blocks as img_blocks

@models.register_setting
class HeaderSettings(models.BaseGenericSetting):
    content = fields.StreamField(
        [
            ('logo', img_blocks.ImageChooserBlock(icon="image")),
        ],
        null=True,
        blank=True
    )

    panels = [
        panels.FieldPanel('content'),
    ]

    class Meta:
        verbose_name = "Header Settings"
