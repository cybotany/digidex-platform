from django.urls import path
from .views import Home, RegisterPlant, CreateLabel

app_name = 'botany'
urlpatterns = [
    path('home', Home.as_view(), name='home'),
    path('new_plant', RegisterPlant.as_view(), name='new_plant'),
    path('new_label', CreateLabel.as_view(), name='new_label'),
]
