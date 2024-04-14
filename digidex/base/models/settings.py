# base/models/settings.py
from django.db import models

from wagtail.admin import panels
from wagtail.contrib.settings import models as wg_settings


@wg_settings.register_setting
class NavigationSettings(wg_settings.BaseGenericSetting):
    logo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Company Logo."
    )
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
            [   panels.FieldPanel('logo'),
                panels.FieldPanel('company'),
                panels.FieldPanel('contact'),
            ],
            "About Us Links",
        ),
        panels.MultiFieldPanel(
            [
                panels.FieldPanel("email"),
                panels.FieldPanel("phone_number"),
                panels.FieldPanel("chat"),
            ],
            heading="Support Contact Information",
        ),
        panels.MultiFieldPanel(
            [
                panels.FieldPanel('blog'),
                panels.FieldPanel('solutions'),
            ],
            "News & Events Links",
        ),
        panels.MultiFieldPanel(
            [
                panels.FieldPanel("twitter"),
                panels.FieldPanel("github"),
            ],
            "Social Media Section Links",
        )
    ]
