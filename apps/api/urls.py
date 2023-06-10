from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.views.decorators.csrf import csrf_exempt
from .views import UserList, ChatbotAPIView, CEAIdentification

app_name = 'api'
urlpatterns = [
    path('user_info/', UserList.as_view(), name='user_info'),
    path('identify_cea/', csrf_exempt(CEAIdentification.as_view()), name='identify_cea'),
    path('chatbot/', ChatbotAPIView.as_view(), name='chatbot'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
