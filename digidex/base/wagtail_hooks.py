from wagtail import hooks
from wagtail.admin.menu import Menu, MenuItem, SubmenuMenuItem
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, PublishingPanel
from wagtail.admin.viewsets.base import ViewSetGroup
from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet

from base.models import FooterBanner


class FooterBanner(SnippetViewSet):
    model = FooterBanner

    panels = [
        FieldPanel("subtitle"),
        FieldPanel("title"),
        MultiFieldPanel(
            [
                FieldPanel("cta_url"),
                FieldPanel("cta_text"),
            ],
            "Call to Action",
        )
    ]

register_snippet(FooterBanner)
