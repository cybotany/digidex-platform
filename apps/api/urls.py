from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import UserList, ChatbotAPIView, CEARegister

app_name = 'api'
urlpatterns = [
    path('user_info/', UserList.as_view(), name='user_info'),
    path('identify_cea/', CEARegister.as_view(), name='identify_cea'),
    path('chatbot/', ChatbotAPIView.as_view(), name='chatbot'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
