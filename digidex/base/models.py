# base/models/snippets.py
from django.db import models

from wagtail import models as wt_models
from wagtail.admin import panels
from wagtail.contrib.settings import models as wt_settings
from wagtail.snippets import models as wt_snippets


@wt_settings.register_setting
class SiteSettings(wt_settings.BaseGenericSetting):
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
            "Support Contact Information",
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


@wt_snippets.register_snippet
class HeaderAdvertisement(wt_models.DraftStateMixin, wt_models.RevisionMixin, wt_models.PreviewableMixin, wt_models.TranslatableMixin, models.Model):
    url = models.URLField(
        null=True,
        blank=True
    )
    text = models.TextField(
        max_length=255
    )

    panels = [
        panels.FieldPanel("url"),
        panels.FieldPanel("text"),
        panels.PublishingPanel(),
    ]

    def __str__(self):
        return self.text

    def get_preview_template(self, request, mode_name):
        return "base.html"

    def get_preview_context(self, request, mode_name):
        return {
            "header_text": self.text,
        }

    class Meta(wt_models.TranslatableMixin.Meta):
        verbose_name_plural = "Advertisements"


@wt_snippets.register_snippet
class PageFooter(wt_models.DraftStateMixin, wt_models.RevisionMixin, wt_models.PreviewableMixin, wt_models.TranslatableMixin, models.Model):
    paragraph = models.TextField(
        max_length=255,
        null=True
    )
    copyright = models.TextField(
        max_length=50,
        null=True
    )
    credit = models.TextField(
        max_length=50,
        null=True
    )

    panels = [
        panels.FieldPanel("paragraph"),
        panels.FieldPanel("copyright"),
        panels.FieldPanel("credit"),
        panels.PublishingPanel(),
    ]

    def __str__(self):
        return "Page Footer"

    def get_preview_template(self, request, mode_name):
        return "base.html"

    def get_preview_context(self, request, mode_name):
        return {
            "paragraph": self.paragraph,
            "copyright": self.copyright,
            "credit": self.credit,
        }

    class Meta(wt_models.TranslatableMixin.Meta):
        verbose_name_plural = "Footer Contents"
