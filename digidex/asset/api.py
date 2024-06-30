from wagtail.models import Page
from wagtail.api.v2.views import PagesAPIViewSet

from .models import AssetPage


class AssetPageViewSet(PagesAPIViewSet):
    model = AssetPage

    def get_queryset(self):
        queryset = super().get_queryset()
        uuid = self.request.GET.get('uuid', None)
        if uuid:
            try:
                asset_page = AssetPage.objects.get(uuid=uuid)
                queryset = asset_page.get_descendants().live().public()
            except AssetPage.DoesNotExist:
                queryset = Page.objects.none()
        return queryset
