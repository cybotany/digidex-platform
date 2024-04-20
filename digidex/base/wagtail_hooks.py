from wagtail.snippets.models import models as s_models
from wagtail.snippets.views import snippets as s_views
from wagtail.admin import panels

from base.models import header, footer

class AdvertisementBannerViewSet(s_views.SnippetViewSet):
    model = header.AdvertisementBanner

    panels = [
        panels.FieldPanel("url"),
        panels.FieldPanel("text"),
        panels.PublishingPanel(),
    ]

s_models.register_snippet(AdvertisementBannerViewSet)


class PageFooterViewSet(s_views.SnippetViewSet):
    model = footer.PageFooter

    panels = [
        panels.FieldPanel("content"),
        panels.FieldPanel("copyright"),
        panels.FieldPanel("credit"),
        panels.PublishingPanel(),
    ]

s_models.register_snippet(PageFooterViewSet)
