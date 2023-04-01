from django.urls import path
from .views import DashboardView, HomeView, SignupView


urlpatterns = [
    path('', HomeView.home, name='home'),
    path('signup/', SignupView.signup, name='signup'),   
    path('dashboard/', DashboardView.dashboard, name='dashboard'),
]