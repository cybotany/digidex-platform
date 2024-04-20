# base/models/snippets.py
from django.db import models

from wagtail import fields
from wagtail import models as wg_models


class CopyrightSnippet(models.Model):
    text = models.TextField()
    year = models.IntegerField()

    def __str__(self):
        return f"Copyright {self.year} - {self.text}"


class CreditSnippet(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text


class PageFooter(wg_models.DraftStateMixin,
                 wg_models.RevisionMixin,
                 wg_models.PreviewableMixin,
                 wg_models.TranslatableMixin,
                 models.Model):

    content = fields.RichTextField()
    copyright = models.ForeignKey(
        CopyrightSnippet,
        on_delete=models.SET_NULL,
        null=True
    )
    credit = models.ForeignKey(
        CreditSnippet,
        on_delete=models.SET_NULL,
        null=True
    )

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
