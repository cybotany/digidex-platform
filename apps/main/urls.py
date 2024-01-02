from django.urls import path
from apps.main.views import (ContactUsView,
                             AboutUsView,
                             LandingView)

app_name = 'main'
urlpatterns = [
    path('', LandingView.as_view(), name='landing'),
    path('contact/', ContactUsView.as_view(), name='contact'),
    path('company/', AboutUsView.as_view(), name='company'),
]
