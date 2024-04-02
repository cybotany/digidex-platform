from django.db import models
from wagtail.admin import panels
from wagtail.contrib.settings import models as settings

@settings.register_setting
class SupportContactSettings(settings.BaseGenericSetting):
    email = models.EmailField(
        null=True,
        blank=True,
        help_text='Support Email Address'
    )
    phone_number = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        help_text='Support Phone Number'
    )
    chat = models.URLField(
        null=True,
        blank=True,
        help_text='URL to launch Support Chat'
    )

    panels = [
        panels.MultiFieldPanel(
            [
                panels.FieldPanel("email"),
                panels.FieldPanel("phone_number"),
                panels.FieldPanel("chat"),
            ],
            heading="Support Contact Information",
        ),
    ]
