from django.urls import path
from cybotany.views.home_view import HomeView
from cybotany.views.account_login_view import AccountLoginView
from cybotany.views.account_signup_view import AccountSignupView
from cybotany.views.account_dashboard_view import AccountDashboardView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login/', AccountLoginView.as_view(), name='login'),   
    path('signup/', AccountSignupView.as_view(), name='signup'),      
    path('dashboard/', AccountDashboardView.as_view(), name='dashboard'),
]