from django.urls import path
from .views import Home, RegisterPlant

app_name = 'botany'
urlpatterns = [
    path('home', Home.as_view(), name='home'),
    path('new_plant', RegisterPlant.as_view(), name='new_plant'),
]
