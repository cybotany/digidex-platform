from wagtail.snippets.models import models as s_models
from wagtail.snippets.views import snippets as s_views
from wagtail.admin import panels as _panels

from base.models import snippets as _snippets

class HeaderAdvertisementViewSet(s_views.SnippetViewSet):
    model = _snippets.AdvertisementBannerSnippet

    panels = [
        _panels.FieldPanel("url"),
        _panels.FieldPanel("text"),
        _panels.PublishingPanel(),
    ]

s_models.register_snippet(HeaderAdvertisementViewSet)


class PageFooterViewSet(s_views.SnippetViewSet):
    model = _snippets.PageFooterSnippet

    panels = [
        _panels.FieldPanel("content"),
        _panels.FieldPanel("copyright"),
        _panels.FieldPanel("credit"),
        _panels.PublishingPanel(),
    ]

s_models.register_snippet(PageFooterViewSet)
