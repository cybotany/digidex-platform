from wagtail.models import Page
from wagtail.api.v2.views import PagesAPIViewSet

from .models import TrainerPage


class TrainerPageViewSet(PagesAPIViewSet):
    model = TrainerPage

    def get_queryset(self):
        queryset = super().get_queryset()
        uuid = self.request.GET.get('uuid', None)
        if uuid:
            try:
                trainer_page = TrainerPage.objects.get(uuid=uuid)
                queryset = trainer_page.get_descendants().live().public()
            except TrainerPage.DoesNotExist:
                queryset = Page.objects.none()
        return queryset
