from django.urls import path
from django.contrib.auth import views as auth_views

from apps.authentication.views import SignupUserView, LoginUserView, LogoutUserView, DisplayUserView, DeleteUserView

app_name = 'authentication'
urlpatterns = [
    path('signup/', SignupUserView.as_view(), name='signup'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', LogoutUserView.as_view(), name='logout'),
    path('profile/', DisplayUserView.as_view(), name='profile'),
    path('delete/', DeleteUserView.as_view(), name='delete'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
