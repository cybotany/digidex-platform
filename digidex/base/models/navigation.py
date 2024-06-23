from django.db import models

from wagtail.admin.panels import FieldPanel, MultiFieldPanel, PublishingPanel
from wagtail.models import DraftStateMixin, PreviewableMixin, RevisionMixin, TranslatableMixin
from wagtail.contrib.settings.models import BaseGenericSetting, register_setting
from wagtail.snippets.models import register_snippet


@register_setting
class Navigation(BaseGenericSetting):
    github_url = models.URLField(
        verbose_name="GitHub URL",
        blank=True
    )
    signup = models.URLField(
        verbose_name="Signup URL"
    )
    login = models.URLField(
        verbose_name="Login URL"
    )
    logout = models.URLField(
        verbose_name="Logout URL"
    )

    panels = [
        MultiFieldPanel(
            [
                FieldPanel("twitter_url"),
                FieldPanel("github_url"),
                FieldPanel("mastodon_url"),
            ],
            "Social settings",
        )
    ]


@register_snippet
class FooterCopyright(
    DraftStateMixin,
    RevisionMixin,
    PreviewableMixin,
    TranslatableMixin,
    models.Model,
):

    text = models.TextField()

    panels = [
        FieldPanel("text"),
        PublishingPanel(),
    ]

    def __str__(self):
        return "Footer Copyright"

    def get_preview_template(self, request, mode_name):
        return "base.html"

    def get_preview_context(self, request, mode_name):
        return {
            "footer_copyright": self.text
        }

    class Meta(TranslatableMixin.Meta):
        verbose_name_plural = "Footer Text"
