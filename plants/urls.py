from django.urls import path
from plants.views import HomeView, AccountLoginView, AccountSignupView, AccountLogoutView, DashboardView, AccountProfileView, SensorSetupView, AccountChatbotView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('signup/', AccountSignupView.as_view(), name='signup'),
    path('login/', AccountLoginView.as_view(), name='login'),
    path('logout/', AccountLogoutView.as_view(), name='logout'),

    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    path('profile/', AccountProfileView.as_view(), name='profile'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('sensor-setup/', SensorSetupView.as_view(), name='sensor_setup'),

    path('chatbot/', AccountChatbotView.as_view(), name='chatbot'),
]
