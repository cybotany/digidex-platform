from django.urls import path
from apps.chatbot.views import ChatbotView

app_name = 'chatbot'
urlpatterns = [
    path('', ChatbotView.as_view(), name='home'),
]
