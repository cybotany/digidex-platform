from django.urls import path
from digidex.accounts.views import (SignupUserView, LoginUserView, LogoutUserView, UserProfileView, DeleteUserView, ModifyProfileView, EmailVerificationView, EmailConfirmationView)

app_name = 'accounts'
urlpatterns = [
    path('signup/', SignupUserView.as_view(), name='signup'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', LogoutUserView.as_view(), name='logout'), 
    path('delete/', DeleteUserView.as_view(), name='delete'),
    path('email-confirmation/', EmailConfirmationView.as_view(), name='confirm-email'),
    path('email-verification/<uidb64>/<token>/', EmailVerificationView.as_view(), name='verify-email'),

    path('profile/<int:pk>/', UserProfileView.as_view(), name='profile'),
    path('profile/<int:pk>/modification/', ModifyProfileView.as_view(), name='profile-modification'),   
]
