from rest_framework.renderers import JSONRenderer

from wagtail.api.v2.views import PagesAPIViewSet
from wagtail.images.api.v2.views import ImagesAPIViewSet
from wagtail.documents.api.v2.views import DocumentsAPIViewSet
from wagtail.api.v2.router import WagtailAPIRouter

from home.models import TrainerPage, CategoryPage, AssetPage

api_router = WagtailAPIRouter('wagtailapi')

class TrainerPagesAPIViewSet(PagesAPIViewSet):
    model = TrainerPage


class CategoryPagesAPIViewSet(PagesAPIViewSet):
    model = CategoryPage


class AssetPagesAPIViewSet(PagesAPIViewSet):
    model = AssetPage


api_router.register_endpoint('pages', PagesAPIViewSet)
api_router.register_endpoint('images', ImagesAPIViewSet)
api_router.register_endpoint('documents', DocumentsAPIViewSet)
