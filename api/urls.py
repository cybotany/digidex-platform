from django.urls import path
from .views import UserList, CybotView


urlpatterns = [
    path('api/user_info/', UserList.as_view(), name='user_info'),
    path('api/cybot/', CybotView.as_view(), name='cybot'),
]
