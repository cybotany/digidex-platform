from django.urls import path
from .views import Chat

urlpatterns = [
    path('chat/', Chat.as_view(), name='chat'),
]
