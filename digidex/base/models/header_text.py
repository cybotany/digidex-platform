from django.db import models
from wagtail.admin.panels import FieldPanel, PublishingPanel
from wagtail.models import DraftStateMixin, PreviewableMixin, RevisionMixin, TranslatableMixin
from wagtail.snippets.models import register_snippet

from base.fields import django_fields as _dfields,\
                        wagtail_fields as _wfields

@register_snippet
class HeaderText(DraftStateMixin, RevisionMixin, PreviewableMixin, TranslatableMixin, models.Model):
    heading = _dfields.BaseCharField(
        max_length=75,
    )
    body = _wfields.BaseRichTextField(
        max_length=150,
    )

    panels = [
        FieldPanel('heading'),
        FieldPanel('body'),
        PublishingPanel(),
    ]

    def __str__(self):
        return "Header text"

    def get_preview_template(self, request, mode_name):
        return "base.html"

    def get_preview_context(self, request, mode_name):
        return {"header_text": self.body}

    class Meta(TranslatableMixin.Meta):
        verbose_name_plural = "Header Text"