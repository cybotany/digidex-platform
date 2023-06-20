from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import ChatbotAPIView, CEAMappingAPIView, PlantIdentificationAPIView

app_name = 'api'
urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('cea-mapping/', CEAMappingAPIView.as_view(), name='map_cea'),
    path('chatbot/', ChatbotAPIView.as_view(), name='chatbot'),
    path('plant-id/', PlantIdentificationAPIView.as_view(), name='plant_id_api'),
]
