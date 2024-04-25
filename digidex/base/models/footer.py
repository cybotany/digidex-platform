# base/models/footer.py
from django.db import models

from wagtail.admin import panels
from wagtail.models import DraftStateMixin, RevisionMixin, PreviewableMixin, TranslatableMixin
from wagtail.snippets.models import register_snippet


@register_snippet
class FooterInformation(
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
    phone_number = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )
    email = models.EmailField(
        max_length=255,
        blank=True,
        null=True
    )
    chat = models.URLField(
        max_length=255,
        blank=True,
        null=True
    )

    panels = [
        panels.FieldPanel('paragraph'),
        panels.FieldPanel('phone_number'),
        panels.FieldPanel('email'),
        panels.FieldPanel('chat'),
    ]

    def __str__(self):
        return "Footer Information"


@register_snippet
class FooterInternalLinks(
    DraftStateMixin,
    RevisionMixin,
    PreviewableMixin,
    models.Model,
):
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

    panels = [
        panels.PageChooserPanel('blog'),
        panels.PageChooserPanel('company'),
        panels.PageChooserPanel('solutions'),
        panels.PageChooserPanel('support'),
    ]

    def __str__(self):
        return "Footer Useful Links"

    def get_preview_template(self, request, mode_name):
        return "base.html"

    def get_preview_context(self, request, mode_name):
        return {
            "blog_page": self.blog,
            "company_page": self.company,
            "github_page": self.solutions,
            "support_page": self.support,
        }


@register_snippet
class FooterSocialLinks(
    DraftStateMixin,
    RevisionMixin,
    PreviewableMixin,
    models.Model,
):
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
        panels.FieldPanel("github"),
        panels.FieldPanel("twitter"),
    ]

    def __str__(self):
        return "Footer Social Links"

    def get_preview_template(self, request, mode_name):
        return "base.html"

    def get_preview_context(self, request, mode_name):
        return {
            "github_url": self.github,
            "twitter_url": self.twitter
        }
