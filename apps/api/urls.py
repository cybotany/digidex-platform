from django.urls import path
from .views import UserList, ChatbotAPIView


urlpatterns = [
    path('user_info/', UserList.as_view(), name='user_info'),
    path('chatbot/', ChatbotAPIView.as_view(), name='chatbot'),
]
