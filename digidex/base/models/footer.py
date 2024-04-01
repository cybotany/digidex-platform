# base/models/footer.py
from wagtail.admin import panels
from wagtail import fields
from wagtail.contrib.settings import models
from wagtail import blocks

@models.register_setting
class FooterSettings(models.BaseGenericSetting):
    content = fields.StreamField(
        [
            ('paragraph', blocks.RichTextBlock()),
        ],
        null=True,
        blank=True
    )

    panels = [
        panels.FieldPanel('content'),
    ]

    class Meta:
        verbose_name = "Footer Settings"
