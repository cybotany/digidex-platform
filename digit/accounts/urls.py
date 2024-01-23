from django.urls import path
from digit.accounts.views import (SignupUserView, LoginUserView, LogoutUserView, UserProfileView, DeleteUserView, ModifyProfileView, EmailVerificationView, EmailConfirmationView)

app_name = 'digit.accounts'
urlpatterns = [
    path('signup/', SignupUserView.as_view(), name='signup'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', LogoutUserView.as_view(), name='logout'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('delete/', DeleteUserView.as_view(), name='delete'),
    path('profile-modification/', ModifyProfileView.as_view(), name='modify-profile'),    
    path('email-confirmation/', EmailConfirmationView.as_view(), name='confirm-email'),
    path('email-verification/', EmailVerificationView.as_view(), name='verify-email'),
]
