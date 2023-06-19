from django.urls import path
from .views import BotanyHomeView, RegisterPlant, CreateLabel, PlantDetail, EditPlant, DeletePlant

app_name = 'botany'
urlpatterns = [
    path('', BotanyHomeView.as_view(), name='home'),
    path('new_label', CreateLabel.as_view(), name='new_label'),
    path('new_plant', RegisterPlant.as_view(), name='new_plant'),
    path('plants/<int:pk>/', PlantDetail.as_view(), name='plant_detail'),
    path('plants/<int:pk>/edit/', EditPlant.as_view(), name='plant_edit'),
    path('plants/<int:pk>/delete/', DeletePlant.as_view(), name='plant_delete'),
]
