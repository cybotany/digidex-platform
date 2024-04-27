from django.urls import path

from .views import user_profile

urlpatterns = [
    path('<slug:slug>/', user_profile, name='user_profile'),
]
