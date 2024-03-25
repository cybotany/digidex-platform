from django.db import models

from wagtail.admin.panels import FieldPanel, MultiFieldPanel, PageChooserPanel, PublishingPanel
from wagtail.contrib.settings.models import BaseGenericSetting, register_setting
from wagtail.models import DraftStateMixin, PreviewableMixin, RevisionMixin, TranslatableMixin
from wagtail.snippets.models import register_snippet

from base.models import basics as _models
from base.fields import basics as _fields


@register_setting
class CallToActionFooter(BaseGenericSetting):
    subtitle = _fields.BaseCharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="Subtitle text"
    )
    heading = _fields.BaseCharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="Main heading text"
    )

    panels = [
        FieldPanel('subtitle'),
        FieldPanel('heading'),
    ]


@register_setting
class PageFooterNavigationSettings(BaseGenericSetting):
    twitter_url = _fields.BaseURLField(
        verbose_name="Twitter URL",
        blank=True 
    )
    github_url = _fields.BaseURLField(
        verbose_name="GitHub URL",
        blank=True
    )
    linkedin_url = _fields.BaseURLField(
        verbose_name="LinkedIn URL",
        blank=True
    )

    panels = [
        MultiFieldPanel(
            [
                FieldPanel("twitter_url"),
                FieldPanel("github_url"),
                FieldPanel("linkedin_url"),
            ],
            "Social settings",
        )
    ]


@register_snippet
class PageFooterText( DraftStateMixin, RevisionMixin, PreviewableMixin, TranslatableMixin, models.Model):
    body = _fields.BaseRichTextField(
        max_length=150,
    )

    panels = [
        FieldPanel("body"),
        PublishingPanel(),
    ]

    def __str__(self):
        return "Footer text"

    def get_preview_template(self, request, mode_name):
        return "base.html"

    def get_preview_context(self, request, mode_name):
        return {"footer_text": self.body}

    class Meta(TranslatableMixin.Meta):
        verbose_name_plural = "Footer Text"
