# base/models/header.py
from django.db import models

from wagtail import models as wg_models
from wagtail.admin import panels


class HeaderAdvertisement(
    wg_models.DraftStateMixin,
    wg_models.RevisionMixin,
    wg_models.PreviewableMixin,
    wg_models.TranslatableMixin,
    models.Model,
):
    url = models.URLField(
        null=True,
        blank=True
    )
    text = models.CharField(
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
            "header_text": self.text,
        }

    class Meta(wg_models.TranslatableMixin.Meta):
        verbose_name_plural = "Header Advert"
