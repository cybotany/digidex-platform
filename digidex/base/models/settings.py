# base/models/settings.py
from django.db import models
from wagtail.admin import panels
from wagtail.contrib.settings import models as wg_settings

@wg_settings.register_setting
class AboutUsSettings(wg_settings.BaseGenericSetting):
    company = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    contact = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    panels = [
        panels.MultiFieldPanel(
            [
                panels.FieldPanel('company'),
                panels.FieldPanel('contact'),
            ],
            "About Us Links",
        ),
    ]


@wg_settings.register_setting
class NewsAndEventsSettings(wg_settings.BaseGenericSetting):
    solutions = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    blog = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    panels = [
        panels.MultiFieldPanel(
            [
                panels.FieldPanel('blog'),
                panels.FieldPanel('solutions'),
            ],
            "News & Events Links",
        ),
    ]


@wg_settings.register_setting
class SocialMediaSettings(wg_settings.BaseGenericSetting):
    twitter = models.URLField(
        verbose_name="Twitter URL",
        blank=True
    )
    github = models.URLField(
        verbose_name="GitHub URL",
        blank=True
    )

    panels = [       
        panels.MultiFieldPanel(
            [
                panels.FieldPanel("twitter"),
                panels.FieldPanel("github"),
            ],
            "Social Media Section Links",
        )
    ]
