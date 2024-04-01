# base/models/footer.py
from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField
from wagtail.contrib.settings.models import BaseGenericSetting, register_setting
from wagtail import blocks

from base import blocks as _bblocks


@register_setting
class FooterSettings(BaseGenericSetting):
    content = StreamField(
        [
            ('logo', _bblocks.LogoBlock()),
            ('paragraph', blocks.CharBlock()),
            ('copyright', blocks.CharBlock(required=False)),
            ('credits', blocks.CharBlock(required=False)),
        ],
        null=True,
        blank=True
    )

    panels = [
        FieldPanel('content'),
    ]

    class Meta:
        verbose_name = "Footer Settings"
