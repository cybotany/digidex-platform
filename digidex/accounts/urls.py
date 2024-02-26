from django.urls import path
from digidex.accounts.views import (SignupUser, LoginUser, LogoutUser, DeleteUser,
                                    VerificationEmail, VerificationCheck)

app_name = 'accounts'
urlpatterns = [
    path('signup/', SignupUser.as_view(), name='signup-user'),
    path('login/', LoginUser.as_view(), name='login-user'),
    path('logout/', LogoutUser.as_view(), name='logout-user'), 
    path('delete/', DeleteUser.as_view(), name='delete-user'),

    path('email-confirmation/', VerificationEmail.as_view(), name='email-user'),
    path('email-verification/<uidb64>/<token>/', VerificationCheck.as_view(), name='verify-user'),
]
