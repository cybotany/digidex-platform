from django.urls import path
from digidex.accounts.views import (UserSignupView,
                                    UserLoginView,
                                    UserLogoutView,
                                    UserDeletionView,
                                    UserProfileView,
                                    ProfileModificationView,
                                    EmailSentView,
                                    EmailVerificationView,)

app_name = 'accounts'
urlpatterns = [
    path('signup/', UserSignupView.as_view(), name='signup'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'), 
    path('delete/', UserDeletionView.as_view(), name='delete'),

    path('<slug:username_slug>/', UserProfileView.as_view(), name='profile'),
    path('<slug:username_slug>/modification/', ProfileModificationView.as_view(), name='profile-modification'),

    path('email-confirmation/', EmailSentView.as_view(), name='confirm-email'),
    path('email-verification/<uidb64>/<token>/', EmailVerificationView.as_view(), name='verify-email'),
]
