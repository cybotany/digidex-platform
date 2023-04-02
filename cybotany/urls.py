from django.urls import path
from .views import account_dashboard_view, account_login_view, account_signup_view, home_view


urlpatterns = [
    path('', home_view.as_view(), name='home'),
    path('login/', account_login_view.as_view(), name='login'),   
    path('signup/', account_signup_view.as_view(), name='signup'),      
    path('dashboard/', account_dashboard_view.as_view(), name='dashboard'),
]