from django.urls import path
from .views import (SignupUserView, LoginUserView, LogoutUserView, UserProfileView, EmailVerificationView, EmailConfirmationView)

app_name = 'accounts'
urlpatterns = [
    path('signup/', SignupUserView.as_view(), name='signup'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', LogoutUserView.as_view(), name='logout'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('email-confirmation/', EmailConfirmationView.as_view(), name='confirm-email'),
    path('email-verification/<str:token>/', EmailVerificationView.as_view(), name='verify-email'),
]
