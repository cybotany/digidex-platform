from django.urls import path
from digidex.accounts.views import (SignupDigidexUser, LoginDigidexUser, LogoutDigidexUser, DeleteDigidexUser, VerificationEmail, VerificationCheck)

app_name = 'accounts'
urlpatterns = [
    path('signup/', SignupDigidexUser.as_view(), name='signup-user'),
    path('login/', LoginDigidexUser.as_view(), name='login-user'),
    path('logout/', LogoutDigidexUser.as_view(), name='logout-user'), 
    path('delete/', DeleteDigidexUser.as_view(), name='delete-user'),
    path('email-confirmation/', VerificationEmail.as_view(), name='email-user'),
    path('email-verification/<uidb64>/<token>/', VerificationCheck.as_view(), name='verify-user'),
]
