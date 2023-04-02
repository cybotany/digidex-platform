from django.urls import path
from .views import DashboardView, HomeView, SignupView, LoginView


urlpatterns = [
    path('', HomeView.home, name='home'),
    path('signup/', SignupView.signup, name='signup'),      
    path('login/', LoginView.as_view(), name='login'),   
    path('dashboard/', DashboardView.dashboard, name='dashboard'),
]