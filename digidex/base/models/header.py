# base/models/header.py
from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField
from wagtail.contrib.settings.models import BaseGenericSetting, register_setting
from wagtail.blocks import StructBlock, TextBlock, ChoiceBlock, CharBlock
from wagtail.images.blocks import ImageChooserBlock

from base import blocks as _bblocks

@register_setting
class HeaderSettings(BaseGenericSetting):
    content = StreamField(
        [
            ('logo', ImageChooserBlock(icon="image")),
            ('link', _bblocks.LinkBlock(icon="link")),
            ('copyright', CharBlock(required=False)),
            ('credits', CharBlock(required=False)),
        ],
        null=True,
        blank=True
    )

    panels = [
        FieldPanel('content'),
    ]

    class Meta:
        verbose_name = "Header Settings"
