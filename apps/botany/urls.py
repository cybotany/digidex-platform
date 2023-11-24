from django.urls import path
from apps.botany.views import PlantView

app_name = 'botany'
urlpatterns = [
    path('<int:pk>/', PlantView.as_view(), name='plant_view'),
]
