from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import GetTSN, CreateLink

app_name = 'api'
urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('tsn/', GetTSN.as_view(), name='get-tsn'),
    path('create/link/<str:uid>/', CreateLink.as_view(), name='create-link'),
]
