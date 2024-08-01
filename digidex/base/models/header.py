from django.db import models
from django.utils.translation import gettext_lazy as _

from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel

from wagtail.models import (
    DraftStateMixin,
    PreviewableMixin,
    RevisionMixin,
    TranslatableMixin,
    Orderable,
)
from wagtail.admin.panels import (
    FieldPanel,
    MultiFieldPanel,
    PublishingPanel,
)
from wagtail.snippets.models import register_snippet


class FooterBanner(
    DraftStateMixin,
    RevisionMixin,
    PreviewableMixin,
    TranslatableMixin,
    models.Model,
):
    subtitle = models.CharField(
        max_length=50
    )
    title = models.CharField(
        max_length=100
    )
    cta_url = models.URLField(
        null=True,
        blank=True
    )
    cta_text = models.CharField(
        max_length=255
    )

    def __str__(self):
        return self.subtitle

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=('translation_key', 'locale'), name='unique_translation_key_locale_base_footerbanner')
        ]


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
