from django.db import models
from wagtail.admin.panels import (
    FieldPanel,
    MultiFieldPanel,
    PublishingPanel,
)
from wagtail.models import (
    DraftStateMixin,
    PreviewableMixin,
    RevisionMixin,
    TranslatableMixin,
)
from wagtail.snippets.models import register_snippet
from wagtail.contrib.settings.models import (
    BaseGenericSetting,
    register_setting,
)

from digidex.base.models import wagtail_fields as _bfields

@register_setting
class FooterNavigationSettings(BaseGenericSetting):
    twitter_url = models.URLField(
        verbose_name="Twitter URL",
        blank=True
    )
    github_url = models.URLField(
        verbose_name="GitHub URL",
        blank=True
    )
    linkedin_url = models.URLField(
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
class FooterText(
    DraftStateMixin,
    RevisionMixin,
    PreviewableMixin,
    TranslatableMixin,
    models.Model,
):
    body = _bfields.BaseRichTextField()

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
