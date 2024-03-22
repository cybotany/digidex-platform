from django.db import models
from wagtail.admin.panels import FieldPanel, PublishingPanel
from wagtail.models import DraftStateMixin, PreviewableMixin, RevisionMixin, TranslatableMixin
from wagtail.snippets.models import register_snippet

from base.fields import wagtail_fields as _wfields

@register_snippet
class FooterText( DraftStateMixin, RevisionMixin, PreviewableMixin, TranslatableMixin, models.Model):
    body = _wfields.BaseRichTextField(
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
