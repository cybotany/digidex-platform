from django.urls import path
from cybotany.views import HomeView, AccountLoginView, AccountSignupView, AccountLogoutView, AccountDashboardView, AccountProfileView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login/', AccountLoginView.as_view(), name='login'),   
    path('signup/', AccountSignupView.as_view(), name='signup'),      
    path('logout/', AccountLogoutView.as_view(), name='logout'),
    path('profile/', AccountProfileView.as_view(), name='profile'),              
    path('dashboard/', AccountDashboardView.as_view(), name='dashboard'),
]