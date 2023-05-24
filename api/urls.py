from django.urls import path
from .views import ChatBotView, UserList


urlpatterns = [
    path('chatbot/', ChatBotView.as_view(), name='chatbot'),
    path('api/user_info/', UserList.as_view(), name='user_info'),
]
