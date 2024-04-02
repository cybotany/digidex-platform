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

    body = fields.RichTextField(
        help_text="Main content for the footer."
    )
    logo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Logo to display in the footer."
    )

    panels = [
        panels.FieldPanel("body"),
        panels.FieldPanel("logo"),
    ]

    def __str__(self):
        return "Footer content"

    def get_preview_template(self, request, mode_name):
        return "base.html"

    def get_preview_context(self, request, mode_name):
        return {
            "footer_body": self.body,
            "footer_logo": self.logo,
        }

    class Meta(wg_models.TranslatableMixin.Meta):
        verbose_name_plural = "Footer contents"


@snippets.register_snippet
class FooterNotice(
    wg_models.DraftStateMixin,
    wg_models.RevisionMixin,
    wg_models.PreviewableMixin,
    wg_models.TranslatableMixin,
    models.Model,
):
    copyright = fields.RichTextField(
        help_text="Copyright notices for the footer.",
        blank=True
    )
    credit = fields.RichTextField(
        help_text="Site credits for the footer.",
        blank=True
    )

    panels = [
        panels.FieldPanel("copyright"),
        panels.FieldPanel("credit"),
        panels.PublishingPanel(),
    ]

    def __str__(self):
        return "Footer notice"

    def get_preview_template(self, request, mode_name):
        return "base.html"

    def get_preview_context(self, request, mode_name):
        return {
            "footer_copyright": self.copyright,
            "footer_credit": self.credit
        }

    class Meta(wg_models.TranslatableMixin.Meta):
        verbose_name_plural = "Footer Notices"
