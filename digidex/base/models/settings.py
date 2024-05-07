# base/models/settings.py
from django.db import models

from wagtail.admin import panels
from wagtail.contrib.settings.models import register_setting, BaseGenericSetting


@register_setting
class NavigationSettings(BaseGenericSetting):
    logo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Company Logo."
    )
    github = models.URLField(
        verbose_name="GitHub URL",
        max_length=255,
        blank=True,
        null=True
    )
    twitter = models.URLField(
        verbose_name="Twitter URL",
        max_length=255,
        blank=True,
        null=True
    )
    blog = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="Blog Page"
    )
    company = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="Company Page"
    )
    solutions = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="Solutions Page"
    )
    support = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="Support Page"
    )
    email = models.EmailField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="Email Address"
    )
    phone_number = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="Phone Number"
    )

    panels = [
        panels.FieldPanel('logo'),
        panels.MultiFieldPanel(
            [
                panels.FieldPanel('email'),
                panels.FieldPanel('phone_number'),
            ],
            heading="Contact Methods"
        ),
        panels.MultiFieldPanel(
            [
                panels.PageChooserPanel('blog'),
                panels.PageChooserPanel('company'),
                panels.PageChooserPanel('solutions'),
                panels.PageChooserPanel('support'),
            ],
            heading="Internal Site Pages"
        ),
        panels.MultiFieldPanel(
            [
                panels.FieldPanel('github'),
                panels.FieldPanel('twitter'),
            ],
            heading="Social Media Links"
        )
    ]
