from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import include, path

from api.views.nfc import RegisterNearFieldCommunicationTag

token_urls = [
    path('', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

app_name = 'api'
urlpatterns = [
    path('token/', include(token_urls)),
    path('nfc/tag/registration/', RegisterNearFieldCommunicationTag.as_view(), name='register_ntag'),
]
