from django.urls import path
from .views import ChatbotView, UserList


urlpatterns = [
    path('chatbot/', ChatbotView.as_view(), name='chatbot'),
    path('api/user_info/', UserList.as_view(), name='user_info'),
]
