from django.urls import path
from digidex.taxonomy.views import LandingView

app_name = 'taxonomy'
urlpatterns = [
    path('', LandingView.as_view(), name='landing'),
]
