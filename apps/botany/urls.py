from django.urls import path
from .views import BotanyHomeView, RegisterPlant, CreateLabel

app_name = 'botany'
urlpatterns = [
    path('', BotanyHomeView.as_view(), name='home'),
    path('new_plant', RegisterPlant.as_view(), name='new_plant'),
    path('new_label', CreateLabel.as_view(), name='new_label'),
]
