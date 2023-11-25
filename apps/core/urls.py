from django.urls import path
from .views import DigitizationView, LandingView

app_name = 'core'
urlpatterns = [
    path('', LandingView.as_view(), name='landing'),
    path('digitization/<str:secret_hash>/', DigitizationView.as_view(), name='digitization'),
]
