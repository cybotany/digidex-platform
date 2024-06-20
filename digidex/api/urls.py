from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import include, path

from wagtail.api.v2.views import PagesAPIViewSet
from wagtail.images.api.v2.views import ImagesAPIViewSet
from wagtail.documents.api.v2.views import DocumentsAPIViewSet
from wagtail.contrib.redirects.api import RedirectsAPIViewSet
from wagtail.api.v2.router import WagtailAPIRouter

from api.views import nfc, gbif

api_router = WagtailAPIRouter('v2/')

api_router.register_endpoint('pages', PagesAPIViewSet)
api_router.register_endpoint('images', ImagesAPIViewSet)
api_router.register_endpoint('documents', DocumentsAPIViewSet)
api_router.register_endpoint('redirects', RedirectsAPIViewSet)

token_urls = [
    path('', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

nfc_urls = [
    path('tag/registration/', nfc.RegisterNearFieldCommunicationTag.as_view(), name='register_ntag'),
]

gbif_urls = [
    path('species/suggestions/', gbif.species_suggestions_view, name='species_suggestions'),
    path('species/backbone/', gbif.species_backbone_view, name='species_backbone'),
]

app_name = 'api'
urlpatterns = [
    path('wagtail/', api_router.urls),
    path('token/', include(token_urls)),
    path('nfc/', include(nfc_urls)),
    path('gbif/', include(gbif_urls)),
]
