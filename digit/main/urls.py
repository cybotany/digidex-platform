from django.urls import path
from digit.main.views import (ContactUsView,
                              AboutUsView,
                              LandingView,
                              ThankYouView)

app_name = 'digit.main'
urlpatterns = [
    path('', LandingView.as_view(), name='landing'),
    path('contact/', ContactUsView.as_view(), name='contact'),
    path('company/', AboutUsView.as_view(), name='company'),
    path('thank-you/', ThankYouView.as_view(), name='thanks')
]
