from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path

from api.views import RegisterNearFieldCommunicationTag

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('ntag/register/', RegisterNearFieldCommunicationTag.as_view(), name='register-ntag'),
]
