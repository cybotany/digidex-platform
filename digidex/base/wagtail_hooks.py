from wagtail.snippets.models import models as s_models
from wagtail.snippets.views import snippets as s_views
from wagtail.admin import panels

from base.models import snippets as _snippets

class HeaderAdvertisementViewSet(s_views.SnippetViewSet):
    model = _snippets.AdvertisementBannerSnippet

    panels = [
        panels.FieldPanel("url"),
        panels.FieldPanel("text"),
        panels.PublishingPanel(),
    ]

s_models.register_snippet(HeaderAdvertisementViewSet)


class PageFooterViewSet(s_views.SnippetViewSet):
    model = _snippets.PageFooterSnippet

    panels = [
        panels.FieldPanel("content"),
        panels.FieldPanel("copyright"),
        panels.FieldPanel("credit"),
        panels.PublishingPanel(),
    ]

s_models.register_snippet(PageFooterViewSet)
