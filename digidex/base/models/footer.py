# base/models/footer.py
from django.db import models

from wagtail import models as wt_models
from wagtail.admin import panels
from wagtail.snippets.models import register_snippet


@register_snippet
class PageFooter(models.Model):
    paragraph = models.TextField(
        max_length=255,
        blank=True,
        null=True
    )
    copyright = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )
    credits = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )
    phone_number = models.CharField(
        verbose_name="Support Phone Number",
        max_length=50,
        blank=True,
        null=True
    )
    email = models.EmailField(
        verbose_name="Support Email Address",
        max_length=255,
        blank=True,
        null=True
    )
    chat = models.URLField(
        verbose_name="Support Chat URL",
        max_length=255,
        blank=True,
        null=True
    )
    blog = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="Blog Page"
    )
    company = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="Company Page"
    )
    solutions = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="Solutions Page"
    )
    support = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="Support Page"
    )
    github = models.URLField(
        verbose_name="GitHub URL",
        max_length=255,
        blank=True,
        null=True
    )
    twitter = models.URLField(
        verbose_name="Twitter URL",
        max_length=255,
        blank=True,
        null=True
    )

    panels = [
        panels.MultiFieldPanel(
            [
                panels.FieldPanel('paragraph'),
                panels.FieldPanel('copyright'),
                panels.FieldPanel('credits'),
            ],
            "Main Footer Contents"),
        panels.MultiFieldPanel(
            [
                panels.FieldPanel('phone_number'),
                panels.FieldPanel('email'),
                panels.FieldPanel('chat'),
            ],
            "Contact Information"),
        panels.MultiFieldPanel(
            [
                panels.PageChooserPanel('blog'),
                panels.PageChooserPanel('company'),
                panels.PageChooserPanel('solutions'),
                panels.PageChooserPanel('support'),
            ],
            "Useful Links"),
        panels.MultiFieldPanel(
            [
                panels.FieldPanel("twitter"),
                panels.FieldPanel("github"),
            ],
            "Social Media Links"),
    ]

    def __str__(self):
        return "Footer Settings"

    class Meta:
        verbose_name = "Footer"
        verbose_name_plural = "Footer Settings"


@register_snippet
class CallToActionBanner(wt_models.DraftStateMixin, wt_models.RevisionMixin, wt_models.PreviewableMixin, wt_models.TranslatableMixin, models.Model):
    url = models.URLField(
        null=True,
        blank=True
    )
    text = models.TextField(
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

    class Meta(wt_models.TranslatableMixin.Meta):
        verbose_name_plural = "Call To Action Banners"
