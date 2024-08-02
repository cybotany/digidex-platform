from wagtail.admin.panels import FieldPanel, MultiFieldPanel, PublishingPanel
from wagtail.snippets.views.snippets import SnippetViewSet, SnippetViewSetGroup
from wagtail.snippets.models import register_snippet

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
