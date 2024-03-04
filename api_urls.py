from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from digidex.api.views import GetTSN, CreateLink, GetItisGeography

app_name = 'api'
urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('get-tsn/', GetTSN.as_view(), name='get-tsn'),
    path('create-link/', CreateLink.as_view(), name='create-link'),
    path('get-geography/<int:id>/', GetItisGeography.as_view(), name='get-geography'),
]
