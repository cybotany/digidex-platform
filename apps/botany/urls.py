from django.urls import path
from .views import Home

app_name = 'botany'
urlpatterns = [
    path('home', Home.as_view(), name='home'),
]
