from django.urls import path
from .views import BotanyHomeView, RegisterPlant, CreateLabel, AutoPlantRegistration, ManualPlantRegistration

app_name = 'botany'
urlpatterns = [
    path('', BotanyHomeView.as_view(), name='home'),
    path('new_label', CreateLabel.as_view(), name='new_label'),
    path('new_plant', RegisterPlant.as_view(), name='new_plant'),
    path('auto_plant_registration', AutoPlantRegistration.as_view(), name='auto_plant_form'),
    path('manual_plant_registration', ManualPlantRegistration.as_view(), name='manual_plant_form'),

]
