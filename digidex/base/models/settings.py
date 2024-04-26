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
    signup = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="Signup User Page"
    )
    login = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="Login User Page"
    )
    profile = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="User Profile Page"
    )
    logout = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="Logout User Page"
    )

    panels = [
        panels.ImageChooserPanel('logo'),
        panels.MultiFieldPanel(
            [
                panels.FieldPanel('email'),
                panels.FieldPanel('phone_number'),
            ],
            heading="Contact Methods"
        ),
        panels.MultiFieldPanel(
            [
                panels.FieldPanel('signup'),
                panels.FieldPanel('login'),
                panels.FieldPanel('profile'),
                panels.FieldPanel('logout'),
            ],
            heading="User Management Pages"
        ),
        panels.MultiFieldPanel(
            [
                panels.FieldPanel('blog'),
                panels.FieldPanel('company'),
                panels.FieldPanel('solutions'),
                panels.FieldPanel('support'),
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
