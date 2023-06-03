from django.urls import path
from user.views import AccountLoginView, AccountSignupView, AccountLogoutView, DashboardView, AccountProfileView, SensorSetupView, AccountChatbotView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', AccountSignupView.as_view(), name='signup'),
    path('login/', AccountLoginView.as_view(), name='login'),
    path('logout/', AccountLogoutView.as_view(), name='logout'),
    path('profile/', AccountProfileView.as_view(), name='profile'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
