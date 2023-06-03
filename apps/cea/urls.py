from django.urls import path
from authentication.views import AccountSignupView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', AccountSignupView.as_view(), name='signup'),
]
