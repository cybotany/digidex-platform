from django.urls import path
from .views import Chat

app_name = 'chatbot'
urlpatterns = [
    path('/', Chat.as_view(), name='home'),
]
