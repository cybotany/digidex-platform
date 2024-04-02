from django.db import models
from wagtail import fields
from wagtail import models as wg_models
from wagtail.snippets import models as snippets
from wagtail.admin import panels

@snippets.register_snippet
class FooterText(
    wg_models.DraftStateMixin,
    wg_models.RevisionMixin,
    wg_models.PreviewableMixin,
    wg_models.TranslatableMixin,
    models.Model,
):

    body = fields.RichTextField()

    panels = [
        panels.FieldPanel("body"),
        panels.PublishingPanel(),
    ]

    def __str__(self):
        return "Footer text"

    def get_preview_template(self, request, mode_name):
        return "base.html"

    def get_preview_context(self, request, mode_name):
        return {"footer_text": self.body}

    class Meta(wg_models.TranslatableMixin.Meta):
        verbose_name_plural = "Footer Text"
