from django.urls import path
from django.contrib.auth import views as auth_views
from .views import LinkView, LandingView, SignupUserView, LoginUserView, LogoutUserView, UserProfileView, DeleteUserView, ChangeProfileView

app_name = 'core'
urlpatterns = [
    path('', LandingView.as_view(), name='landing'),
    path('link/<str:serial_number>/', LinkView.as_view(), name='link'),
    path('digitize/<str:serial_number>/', DigitizeView.as_view(), name='digitize'),
    path('digit/<int:pk>/', DigitView.as_view(), name='digit'),

    path('signup/', SignupUserView.as_view(), name='signup'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', LogoutUserView.as_view(), name='logout'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('profile-change/', ChangeProfileView.as_view(), name='profile_change'),
    path('delete/', DeleteUserView.as_view(), name='delete'),
    path('password-reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
