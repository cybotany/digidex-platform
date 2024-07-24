from django.db import models
from django.utils.translation import gettext_lazy as _

from wagtail.models import (
    DraftStateMixin,
    PreviewableMixin,
    RevisionMixin,
    TranslatableMixin,
)
from wagtail.admin.panels import (
    FieldPanel,
    MultiFieldPanel,
    PublishingPanel,
)
from wagtail.snippets.models import register_snippet


@register_snippet
class FooterParagraph(
    DraftStateMixin,
    RevisionMixin,
    PreviewableMixin,
    TranslatableMixin,
    models.Model,
):
    paragraph = models.TextField(
        max_length=100
    )

    panels = [
        FieldPanel("paragraph"),
    ]

    def __str__(self):
        return "Footer Text"

    def get_preview_template(self, request, mode_name):
        return "index.html"

    def get_preview_context(self, request, mode_name):
        return {"footer_paragraph": self.paragraph}

    class Meta(TranslatableMixin.Meta):
        verbose_name = "Footer Paragraph"
        verbose_name_plural = "Footer Paragraphs"


@register_snippet
class FooterCopyright(
    DraftStateMixin,
    RevisionMixin,
    PreviewableMixin,
    TranslatableMixin,
    models.Model,
):
    copyright = models.TextField(
        max_length=100
    )

    panels = [
        FieldPanel("copyright"),
        PublishingPanel(),
    ]

    def __str__(self):
        return "Footer Copyright"

    def get_preview_template(self, request, mode_name):
        return "index.html"

    def get_preview_context(self, request, mode_name):
        return {"footer_copyright": self.copyright}

    class Meta(TranslatableMixin.Meta):
        verbose_name = "Footer Copyright"
        verbose_name_plural = "Footer Copyrights"
