from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path

from api.views import nfc as nfc_views

app_name = 'api'
urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('ntag/register/', nfc_views.RegisterNearFieldCommunicationTag.as_view(), name='register-ntag'),
]
