# base/models/footer.py
from django.db import models

from wagtail.admin import panels
from wagtail.models import DraftStateMixin, RevisionMixin, PreviewableMixin
from wagtail.snippets.models import register_snippet


@register_snippet
class FooterParagraph(
    DraftStateMixin,
    RevisionMixin,
    PreviewableMixin,
    models.Model,
):
    paragraph = models.TextField(
        max_length=255,
        blank=True,
        null=True
    )

    panels = [
        panels.FieldPanel('paragraph'),
    ]

    def __str__(self):
        return "Footer Paragraph"

    def get_preview_template(self, request, mode_name):
        return 'base.html'

    def get_preview_context(self, request, mode_name):
        return {
            "footer_paragraph": self.paragraph
        }


@register_snippet
class FooterCopyright(
    DraftStateMixin,
    RevisionMixin,
    PreviewableMixin,
    models.Model,
):
    copyright = models.TextField(
        max_length=255,
        blank=True,
        null=True
    )

    panels = [
        panels.FieldPanel("copyright"),
    ]

    def __str__(self):
        return "Footer Copyright"

    def get_preview_template(self, request, mode_name):
        return "base.html"

    def get_preview_context(self, request, mode_name):
        return {
            "copyright_text": self.copyright
        }
