from django.urls import path
from .views import UserDetailView


urlpatterns = [
    path('api/user_info/', UserDetailView.as_view(), name='user_info'),
]
