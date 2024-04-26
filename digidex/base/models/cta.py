# base/models/cta.py
from django.db import models

from wagtail import models as wt_models
from wagtail.admin import panels
from wagtail.snippets.models import register_snippet


@register_snippet
class CallToActionBanner(wt_models.DraftStateMixin, wt_models.RevisionMixin, wt_models.PreviewableMixin, wt_models.TranslatableMixin, models.Model):
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
            "cta_text": self.text,
        }

    class Meta(wt_models.TranslatableMixin.Meta):
        verbose_name = "Call To Action Banner"