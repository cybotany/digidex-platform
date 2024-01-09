from django.urls import path
from .views import (SignupUserView, LoginUserView, LogoutUserView, UserProfileView, EmailVerificationView, EmailConfirmationView, PasswordResetView, PasswordResetCompleteView, PasswordResetSentView, PasswordResetConfirmationView)

app_name = 'accounts'
urlpatterns = [
    path('signup/', SignupUserView.as_view(), name='signup'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', LogoutUserView.as_view(), name='logout'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('email-confirmation/', EmailConfirmationView.as_view(), name='confirm-email'),
    path('email-verification/<str:token>/', EmailVerificationView.as_view(), name='verify-email'),
    path('reset-password/', PasswordResetView.as_view(), name ='password-reset'),
    path('reset-password-sent/', PasswordResetSentView.as_view(), name ='password-reset-sent'),
    path('reset-password/<uidb64>/<token>/', PasswordResetConfirmationView.as_view(), name ='password-reset-confirm'),
    path('reset-password-complete/', PasswordResetCompleteView.as_view(), name ='password-reset-complete'),
]
