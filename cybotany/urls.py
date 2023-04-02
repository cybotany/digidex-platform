from django.urls import path
from cybotany.views import HomeView, AccountLoginView, AccountSignupView, AccountDashboardView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login/', AccountLoginView.as_view(), name='login'),   
    path('signup/', AccountSignupView.as_view(), name='signup'),      
    path('dashboard/', AccountDashboardView.as_view(), name='dashboard'),
]