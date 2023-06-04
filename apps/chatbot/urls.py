from django.urls import path
from .views import Chat

app_name = 'chatbot'
urlpatterns = [
    path('chat/', Chat.as_view(), name='chat'),
]
