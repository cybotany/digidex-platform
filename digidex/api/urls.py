from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import include, path

from api.views import nfc, gbif


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
    path('token/', include(token_urls)),
    path('nfc/', include(nfc_urls)),
    path('gbif/', include(gbif_urls)),
]
