from django.urls import path
from apps.botany.views import CreateLabelView, DescribePlantView, DeletePlantView, UpdatePlantView, PlantHomepageView, RegisterPlantView, SelectPlantView, UploadPlantImageView


app_name = 'botany'
urlpatterns = [
    path('', PlantHomepageView.as_view(), name='home'),
    path('create-label', CreateLabelView.as_view(), name='create_label'),
    path('register-plant', RegisterPlantView.as_view(), name='register_plant'),
    path('select-plant', SelectPlantView.as_view(), name='select_plant'),
    path('upload-plant-image', UploadPlantImageView.as_view(), name='upload_plant_image'),
    path('plants/<int:pk>/describe', DescribePlantView.as_view(), name='describe_plant'),
    path('plants/<int:pk>/update', UpdatePlantView.as_view(), name='update_plant'),
    path('plants/<int:pk>/delete', DeletePlantView.as_view(), name='delete_plant'),
]
