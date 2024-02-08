from django.urls import path
from digidex.main.views import (ErrorView,
                                CompanyView,
                                ContactView,
                                LandingView,
                                ThankYouView)

app_name = 'main'
urlpatterns = [
    path('', LandingView.as_view(), name='landing'),
    path('error/', ErrorView.as_view(), name='error'),
    path('company/', CompanyView.as_view(), name='company'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('thank-you/', ThankYouView.as_view(), name='thanks'),
]
