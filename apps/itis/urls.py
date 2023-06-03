from django.urls import path
from authentication.views import AccountLoginView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
