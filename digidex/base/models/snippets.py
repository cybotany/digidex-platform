# base/models/snippets.py
from django.db import models

from wagtail import fields
from wagtail import models as wg_models


class _BaseSnippet(wg_models.DraftStateMixin, wg_models.RevisionMixin, wg_models.PreviewableMixin, wg_models.TranslatableMixin, models.Model):
    """
    Base class for all snippets.
    """
    class Meta:
        abstract = True


class AdvertisementBannerSnippet(_BaseSnippet):
    url = models.URLField(
        null=True,
        blank=True
    )
    text = models.CharField(
        max_length=255
    )

    def __str__(self):
        return self.text

    def get_preview_template(self, request, mode_name):
        return "base.html"

    def get_preview_context(self, request, mode_name):
        return {
            "header_text": self.text,
        }

    class Meta(wg_models.TranslatableMixin.Meta):
        verbose_name_plural = "Advertisements"



class PageFooterSnippet(_BaseSnippet):
    content = fields.RichTextField()
    copyright = fields.RichTextField()
    credit = fields.RichTextField()

    def __str__(self):
        return "Page Footer"

    def get_preview_template(self, request, mode_name):
        return "base.html"

    def get_preview_context(self, request, mode_name):
        return {
            "content": self.content,
            "copyright": self.copyright,
            "credit": self.credit,
        }

    class Meta(wg_models.TranslatableMixin.Meta):
        verbose_name_plural = "Footer Contents"
