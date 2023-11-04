from django.urls import path
from apps.botany.views import (
    RegisterPlantView,
    DescribePlantView,
    DeletePlantView,
    UpdatePlantView,
    PlantHomepageView,
    DeletePlantImageView,
)


app_name = 'botany'
urlpatterns = [
    path('', PlantHomepageView.as_view(), name='home'),
    path('register/plant/', RegisterPlantView.as_view(), name='register_plant'),
    path('plant/<int:pk>/describe/', DescribePlantView.as_view(), name='describe_plant'),
    path('plant/<int:pk>/delete/', DeletePlantView.as_view(), name='delete_plant'),
    path('plant/<int:pk>/update/', UpdatePlantView.as_view(), name='update_plant'),
    path('plant/<int:pk>/delete/image', DeletePlantImageView.as_view(), name='delete_plant_image'),
]
