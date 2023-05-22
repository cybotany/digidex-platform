from django.urls import path
from .views import UserList


urlpatterns = [
    path('api/user_info/', UserList.as_view(), name='user_info'),
]
