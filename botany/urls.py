from django.urls import path
from botany.views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
]
