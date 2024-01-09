from django.urls import path
from .views import (SignupUserView, LoginUserView, LogoutUserView, UserProfileView, EmailVerificationView, EmailConfirmationView, DigitPasswordResetView, DigitPasswordResetCompleteView, DigitPasswordResetSentView, DigitPasswordResetConfirmationView)

app_name = 'accounts'
urlpatterns = [
    path('signup/', SignupUserView.as_view(), name='signup'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', LogoutUserView.as_view(), name='logout'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('email-confirmation/', EmailConfirmationView.as_view(), name='confirm-email'),
    path('email-verification/<str:token>/', EmailVerificationView.as_view(), name='verify-email'),
    path('reset_password/', DigitPasswordResetView.as_view(), name ='password_reset'),
    path('reset_password_sent/', DigitPasswordResetSentView.as_view(), name ='password_reset_done'),
    path('reset/<uidb64>/<token>', DigitPasswordResetConfirmationView.as_view(), name ='password_reset_confirm'),
    path('reset_password_complete/', DigitPasswordResetCompleteView.as_view(), name ='password_reset_complete'),
]
