# base/models/footer.py
from django.db import models
from wagtail import fields
from wagtail import models as wg_models
from wagtail.snippets import models as snippets
from wagtail.admin import panels

@snippets.register_snippet
class FooterContent(
    wg_models.DraftStateMixin,
    wg_models.RevisionMixin,
    wg_models.PreviewableMixin,
    wg_models.TranslatableMixin,
    models.Model,
):
    paragraph = fields.RichTextField(
        help_text="Main content for the footer."
    )

    panels = [
        panels.FieldPanel("paragraph"),
    ]

    def __str__(self):
        return "Footer content"

    def get_preview_template(self, request, mode_name):
        return "base.html"

    def get_preview_context(self, request, mode_name):
        return {
            "footer_content": self.paragraph,
        }

    class Meta(wg_models.TranslatableMixin.Meta):
        verbose_name_plural = "Footer Content"


@snippets.register_snippet
class FooterNotice(
    wg_models.DraftStateMixin,
    wg_models.RevisionMixin,
    wg_models.PreviewableMixin,
    wg_models.TranslatableMixin,
    models.Model,
):
    notice = fields.RichTextField(
        help_text="Copyright and Credit notices for the footer.",
        blank=True
    )

    panels = [
        panels.FieldPanel("notice"),
        panels.PublishingPanel(),
    ]

    def __str__(self):
        return "Footer notice"

    def get_preview_template(self, request, mode_name):
        return "base.html"

    def get_preview_context(self, request, mode_name):
        return {
            "footer_notice": self.notice
        }

    class Meta(wg_models.TranslatableMixin.Meta):
        verbose_name_plural = "Footer Notices"
